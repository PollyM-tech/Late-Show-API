from models import db, Episode, Guest, Appearance

def seed_database():
    db.drop_all()
    db.create_all()


    ep1 = Episode(date="1/11/99", number=1)
    ep2 = Episode(date="1/12/99", number=2)

    guest1 = Guest(name="Michael J. Fox", occupation="actor")
    guest2 = Guest(name="Sandra Bernhard", occupation="Comedian")
    guest3 = Guest(name="Tracey Ullman", occupation="television actress")

    appearances = [
        Appearance(rating=4, episode=ep1, guest=guest1),
        Appearance(rating=5, episode=ep2, guest=guest2),
        Appearance(rating=3, episode=ep2, guest=guest3)
    ]

    db.session.add_all([ep1, ep2, guest1, guest2, guest3])
    db.session.add_all(appearances)
    db.session.commit()
    print("Database seeded!")