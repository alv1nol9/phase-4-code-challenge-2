import sys
from pathlib import Path
from datetime import date

# Add project root to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

from server.app import create_app, db
from models import  User, Guest, Episode, Appearance

def seed_data():
    app = create_app()
    
    with app.app_context():
        try:
            print("Resetting database...")
            db.reflect()
            db.drop_all()
            db.create_all()
            
            print("Seeding data...")
            # Create users
            admin = User(username='admin')
            admin.set_password('admin123')
            db.session.add(admin)
            
            # Create guests
            guest1 = Guest(name='John Murphy', occupation='Actor')
            guest2 = Guest(name='Jane Smith', occupation='Musician')
            db.session.add_all([guest1, guest2])
            
            # Create episodes
            ep1 = Episode(date=date(2023, 1, 1), number=101)
            ep2 = Episode(date=date(2023, 1, 2), number=102)
            db.session.add_all([ep1, ep2])
            
            # Create appearances
            app1 = Appearance(rating=5, guest_id=1, episode_id=1)
            app2 = Appearance(rating=4, guest_id=2, episode_id=1)
            db.session.add_all([app1, app2])
            
            db.session.commit()
            print("✅ Database seeded successfully!")
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            db.session.rollback()
        finally:
            db.session.close()

if __name__ == '__main__':
    seed_data()
