from app import app, db, User
from werkzeug.security import generate_password_hash

with app.app_context():
    # Check if admin already exists
    admin = User.query.filter_by(username='admin').first()
    if not admin:
        # Create admin user
        admin_user = User(
            username='admin',
            password=generate_password_hash('admin'),  # Change this password
            email='admin@example.com',
            is_admin=True
        )
        db.session.add(admin_user)
        db.session.commit()
        print("Admin user created successfully!")
    else:
        print("Admin user already exists!")