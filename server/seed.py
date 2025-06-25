from .app import create_app, db
from .models.user import User
from .models.guest import Guest
from .models.episode import Episode
from .models.appearance import Appearance
from datetime import date

def seed():
    db.drop_all()
    db.create_all()

    # Users
    user = User(username="admin")
    user.set_password("password")
    db.session.add(user)

    # Guests
    guest1 = Guest(name="Alice Smith", occupation="Comedian")
    guest2 = Guest(name="Bob Jones", occupation="Actor")
    db.session.add_all([guest1, guest2])

    # Episodes
    episode1 = Episode(date=date(2024, 6, 1), number=1)
    episode2 = Episode(date=date(2024, 6, 2), number=2)
    db.session.add_all([episode1, episode2])

    db.session.commit()

    # Appearances
    appearance1 = Appearance(rating=5, guest_id=guest1.id, episode_id=episode1.id)
    appearance2 = Appearance(rating=4, guest_id=guest2.id, episode_id=episode1.id)
    appearance3 = Appearance(rating=3, guest_id=guest1.id, episode_id=episode2.id)
    db.session.add_all([appearance1, appearance2, appearance3])

    db.session.commit()

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        seed()
