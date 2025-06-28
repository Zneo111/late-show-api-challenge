from app import create_app, db
from models.user import User
from models.guest import Guest
from models.episode import Episode
from models.appearance import Appearance

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    # Create a user
    user = User(username="admin")
    user.set_password("password")
    db.session.add(user)

    # Create guests
    guest1 = Guest(name="Alice Smith", occupation="Actor")
    guest2 = Guest(name="Bob Jones", occupation="Musician")
    db.session.add_all([guest1, guest2])

    # Create episodes
    episode1 = Episode(date="2024-06-01", number=1)
    episode2 = Episode(date="2024-06-02", number=2)
    db.session.add_all([episode1, episode2])

    db.session.commit()

    # Create appearances
    appearance1 = Appearance(rating=5, guest_id=guest1.id, episode_id=episode1.id)
    appearance2 = Appearance(rating=4, guest_id=guest2.id, episode_id=episode2.id)
    db.session.add_all([appearance1, appearance2])

    db.session.commit()

    print("Database seeded!")
