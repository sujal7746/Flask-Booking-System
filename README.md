**Overview:**
The Flask Booking System is a web application designed to simplify appointment scheduling with a modern interface and real-time admin notifications.
Built with Flask, this project allows users to register, log in, select date/time slots, and submit booking details, which are stored in an SQLite database. 
Administrators receive instant WhatsApp notifications for each new booking via Twilio's API, ensuring efficient management. 
The UI features a sleek, responsive design with animations, making it both functional and visually appealing.

**Features:**
User Authentication: Secure registration and login with password hashing (Werkzeug).<br/>
Role-Based Access: Separate views for users and admins (admin panel for booking oversight).<br/>
Graphical UI: Responsive design with gradient backgrounds, card layouts, and animations (CSS, Font Awesome, Google Fonts).<br/>


**Booking Workflow:**
Select date/time slots via a styled datetime picker.<br/>
Submit detailed booking forms (name, contact, address, organization, email).<br/>
Database Storage: SQLite backend for persisting user and booking data.<br/>
WhatsApp Notifications: Instant admin alerts for new bookings using Twilio's WhatsApp API.<br/>
Admin Panel: View all bookings with user details in a tabular format.<br/>


**Prerequisites:**
Python 3.8+<br/>
Twilio Account (for WhatsApp integration)<br/>
SQLite (included with Python)<br/>
Git (for cloning the repository)<br/>

**Installation**

Clone the Repository:<br/>
git clone https://github.com/sujal7746/flask-booking-system.git.<br/>
cd flask-booking-system<br/>

**Set Up a Virtual Environment:**
python -m venv venv<br/>
source venv/bin/activate  # On Windows: venv\Scripts\activate<br/>

**Install Dependencies:**
pip install -r requirements.txt<br/>

**Configure Environment Variables:**
Create a .env file in the project root:<br/>

TWILIO_ACCOUNT_SID=your_twilio_sid<br/>
TWILIO_AUTH_TOKEN=your_twilio_auth_token<br/>
TWILIO_PHONE_NUMBER=whatsapp:+your_twilio_number<br/>
ADMIN_PHONE_NUMBER=whatsapp:+admin_number<br/>
FLASK_SECRET_KEY=your_secret_key<br/>
Replace placeholders with your Twilio credentials and a random secret key.<br/>


**Initialize the Database:**
Run the app once to create the SQLite database (booking.db):<br/>
python app.py<br/>

**Create an Admin User:**
Run the provided script to add an admin:<br/>
python create_admin.py<br/>

**Run the Application:**<br/>
python app.py<br/>
Access the app at http://localhost:5000.<br/>

**User Flow:**
Register at /register.<br/>
Log in at /login.<br/>
Select a date/time at /dashboard.<br/>
Submit booking details at /booking_form.<br/>

**Admin Flow:**

Log in as admin at /admin_login (default: admin / admin).<br/>
View bookings at /admin_panel.<br/>
Receive WhatsApp notifications for new bookings.<br/>
