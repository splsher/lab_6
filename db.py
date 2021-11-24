from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
metadata = Base.metadata

class User(Base):

     __tablename__ = 'users'

     id = Column(Integer, primary_key=True,autoincrement=True)
     username = Column(String(45))
     firstname = Column(String(45))
     lastname = Column(String(45))
     email = Column(String(45))
     password = Column(String(45))
     phone = Column(String(45))
     family_id = Column(Integer, ForeignKey('family.id'), nullable=False)
     def __repr__(self):
        return "<User(id='%s',username='%s', firstname='%s', lastname='%s', email='%s', password='%s', phone='%s', family_id='%s')>" % (
                             self.id, self.username, self.firstname, self.lastname, self.email, self.password, self.phone, self.family_id)


class Family(Base):
     __tablename__ = 'family'

     id = Column(Integer, primary_key=True,autoincrement=True)
     name = Column(String(45))
     account_ownerId = Column(Integer, ForeignKey('account.ownerid'), nullable=False)
     def __repr__(self):
        return "<Family(id='%s', name='%s', account_owner='%s')>" % (
                             self.id, self.name, self.account_ownerId)


class Account(Base):
     __tablename__ = 'account'

     ownerid = Column(Integer, primary_key=True)
     balance = Column(Integer)

     def __repr__(self):
        return "<Account(id='%s', balance ='%s')>" % (
                             self.id, self.balance)


class Budget_note(Base):
     __tablename__ = 'budget_note'
     id = Column(Integer, primary_key=True,autoincrement=True)
     sum = Column(Integer)
     date = Column(Date)
     type = Column(String(40))
     users_id = Column(Integer, ForeignKey('users.id'))
     def __repr__(self):
        return "<Budget_note(id='%s',sum='%s', date='%s', type='%s', users_id='%s')>" % (
                             self.id, self.sum, self.date, self.type, self.users_id)