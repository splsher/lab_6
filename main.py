from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import datetime
from db import Base, Budget_note, User, Family, Account

engine = create_engine('mysql://root:Bonia9977@localhost/family_budget', echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

session = Session()

# session.query(Budget_note).delete()
# session.query(User).delete()
# session.query(Family).delete()
# session.query(Account).delete()
# session.commit()

session.add_all([
    Account(balance=10000, ownerid=1),
    Account(balance=20000, ownerid=2),
    Family(id=1, name='Zhuk', account_ownerId=1),
    Family(id=2, name='Stepanovy', account_ownerId=1),
    User(username='Katya2002', firstname='Katya', lastname='Stepanova', email='us1@ukr.net', family_id=2),
    User(username='Alex2002', firstname='Alexy', lastname='Stepanov', email='us2@ukr.net', family_id=2),
    User(username='Ivan2000', firstname='Ivan', lastname='Zhuk', email='us1@ukr.net', family_id=1),

])
session.commit()

print("пошук користувача з ніком Ivan2000")
our_user = session.query(User).filter_by(username='Ivan2000').first()
print("Користувач", our_user.username, our_user.firstname, our_user.lastname, our_user.email)

print("пошук користувачів з ніком, який містить фразу 2002")
our_users = session.query(User).filter(User.username.like('%2002%')).all()
for user in our_users:
    print("Користувач", user.username, user.firstname, user.lastname, user.email)

k = 100
for user in session.query(User, User.id).all():
    print(user.id)
    session.add_all([
        Budget_note(sum=k, date=datetime.datetime(2020, 10, 10), type='Купівля', users_id=user.id),
        Budget_note(sum=k + 100, date=datetime.datetime(2020, 10, 20), type='Купівля', users_id=user.id),
        Budget_note(sum=k + 400, date=datetime.datetime(2020, 10, 30), type='Купівля', users_id=user.id)
    ])
    k += 100
session.commit()
