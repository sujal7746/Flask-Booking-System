Overview-
The Flask Booking System is a web application designed to simplify appointment scheduling with a modern interface and real-time admin notifications.
Built with Flask, this project allows users to register, log in, select date/time slots, and submit booking details, which are stored in an SQLite database. 
Administrators receive instant WhatsApp notifications for each new booking via Twilio's API, ensuring efficient management. 
The UI features a sleek, responsive design with animations, making it both functional and visually appealing.

Features
User Authentication: Secure registration and login with password hashing (Werkzeug).
Role-Based Access: Separate views for users and admins (admin panel for booking oversight).
Graphical UI: Responsive design with gradient backgrounds, card layouts, and animations (CSS, Font Awesome, Google Fonts).


Booking Workflow:
Select date/time slots via a styled datetime picker.
Submit detailed booking forms (name, contact, address, organization, email).
Database Storage: SQLite backend for persisting user and booking data.
WhatsApp Notifications: Instant admin alerts for new bookings using Twilio's WhatsApp API.
Admin Panel: View all bookings with user details in a tabular format.


Prerequisites
Python 3.8+
Twilio Account (for WhatsApp integration)
SQLite (included with Python)
Git (for cloning the repository)

Installation

Clone the Repository:
git clone https://github.com/yourusername/flask-booking-system.git
cd flask-booking-system

Set Up a Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install Dependencies:
pip install -r requirements.txt

Configure Environment Variables:
Create a .env file in the project root:

TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=whatsapp:+your_twilio_number
ADMIN_PHONE_NUMBER=whatsapp:+admin_number
FLASK_SECRET_KEY=your_secret_key
Replace placeholders with your Twilio credentials and a random secret key.


Initialize the Database:
Run the app once to create the SQLite database (booking.db):
python app.py

Create an Admin User:
Run the provided script to add an admin:
python create_admin.py

Run the Application:
python app.py
Access the app at http://localhost:5000.

User Flow:
Register at /register.
Log in at /login.
Select a date/time at /dashboard.
Submit booking details at /booking_form.

Admin Flow:

Log in as admin at /admin_login (default: admin / admin).
View bookings at /admin_panel.
Receive WhatsApp notifications for new bookings.
