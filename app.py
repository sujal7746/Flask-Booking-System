from flask import Flask, render_template, request, redirect, url_for, session, flash
from database import db, User, Booking
from werkzeug.security import generate_password_hash, check_password_hash
from twilio.rest import Client
import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///booking.db'
db.init_app(app)
#change from your twilio account

TWILIO_ACCOUNT_SID = 'xxxxxxxxxxx'
TWILIO_AUTH_TOKEN = 'xxxxxxxxxxx'
TWILIO_PHONE_NUMBER = 'whatsapp:+14155238886'  
ADMIN_PHONE_NUMBER = 'whatsapp:+917746919069'    

twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        email = request.form['email']
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists')
            return redirect(url_for('register'))
        
        user = User(username=username, password=password, email=email)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful! Please login.')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['is_admin'] = user.is_admin
            return redirect(url_for('dashboard'))
        flash('Invalid credentials')
    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        date_time = request.form['datetime']
        session['selected_datetime'] = date_time
        return redirect(url_for('booking_form'))
    return render_template('dashboard.html')

@app.route('/booking_form', methods=['GET', 'POST'])
def booking_form():
    if 'user_id' not in session or 'selected_datetime' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        booking = Booking(
            user_id=session['user_id'],
            date_time=session['selected_datetime'],
            name=request.form['name'],
            contact=request.form['contact'],
            address=request.form['address'],
            organization=request.form['organization'],
            email=request.form['email']
        )
        db.session.add(booking)
        db.session.commit()

        username = User.query.get(session['user_id']).username
        message_body = (
            f"New Booking Received:\n"
            f"User: {username}\n"
            f"Date & Time: {session['selected_datetime']}\n"
            f"Name: {request.form['name']}\n"
            f"Contact: {request.form['contact']}\n"
            f"Address: {request.form['address']}\n"
            f"Organization: {request.form['organization']}\n"
            f"Email: {request.form['email']}\n"
            f"Submitted: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )
        try:
            twilio_client.messages.create(
                body=message_body,
                from_=TWILIO_PHONE_NUMBER,
                to=ADMIN_PHONE_NUMBER
            )
            print("WhatsApp message sent to admin successfully!")
        except Exception as e:
            print(f"Failed to send WhatsApp message: {str(e)}")
            flash('Booking saved, but failed to notify admin via WhatsApp.')

        flash('Booking successful!')
        return redirect(url_for('dashboard'))
    return render_template('booking_form.html')

@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, is_admin=True).first()
        
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['is_admin'] = True
            return redirect(url_for('admin_panel'))
        flash('Invalid admin credentials')
    return render_template('admin_login.html')

@app.route('/admin_panel')
def admin_panel():
    if 'user_id' not in session or not session['is_admin']:
        return redirect(url_for('admin_login'))
    
    bookings = Booking.query.all()
    users = User.query.all()
    return render_template('admin_panel.html', bookings=bookings, users=users)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)