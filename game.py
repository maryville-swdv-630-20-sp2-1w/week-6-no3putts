# Jeremiah Pineda
# SWDV 630
# Instructor:  J. Gradecki
# Week 6 Assignment - Storing Objects in the Database

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

# Class that can Mapped object to database
Base = declarative_base()

class CharacterClass(Base):
    def __init__(self, name, gender, race):
        self.name = name
        self.gender = gender
        self.race = race

    __tablename__ = 'character'

    # FILEDS
    id = Column(Integer, primary_key=True)
    name = Column(String)
    gender = Column(String)
    race = Column(String)


    def attack(self):
        raise NotImplementedError()

    def dance(self):
        raise NotImplementedError()


# SUBCLASSES
class Warrior(CharacterClass):
    def __init__(self, name, gender, race):
        CharacterClass.__init__(self,name, gender, race)
        self.main_hand = 'sword'
        self.off_hand = 'shield'
        self.range = 'gun'

    def attack(self):
        print(self.name + " raise + to strike monster")

    def dance(self):
        print(self.name + " doing the irish jig")

    def raise_shield(self):
        print(self.name + " raised shiedl, blocking enemy attack")

    def activate_whirlwind(self):
        print(self.name + " casting whirlwind, hits 10 enemy combatants")

    def activate_challenging_shout(self):
        print(self.name + " challenging shout activated, agro all enemies")


class Mage(CharacterClass):
    def __init__(self, name, gender, race):
        CharacterClass.__init__(self, name, gender, race)
        self.main_hand = 'Wand'
        self.off_hand = 'Orb'

    def attack(self):
        print(self.name + " casting with wand")

    def dance(self):
        print(self.name + " Started to Break Dance")

    def summon_portal(self,location):
        print(self.name + " activated portal to " + location)

    def cast_ice_barrier(self):
        print(self.name + " casting ice barrier, 100% damage absorbed")


class Hunter(CharacterClass):
    def __init__(self,  name, gender, race):
        CharacterClass.__init__(self, name, gender, race)
        self.main_hand = 'Bow'
        self.quiver = 0

    def attack(self):
        print(self.name + " start shooting with Bow and Arrow")

    def dance(self):
        print(self.name + " doing the Macarena")

    def summon_pet(self, pet):
        print(self.name + " summoning pet " + pet)

    def lay_trap(self, type):
        print(self.name + " yaying " + type + " trap")

    def play_dead(self):
        print(self.name + " cast play dead")

    def refil_quiver(self, count):
        self.quiver = count
        print("Loaded quiver with " + count + " arrows")


def main():
    print('\nSQLAlchemy version {}\n'.format(sqlalchemy.__version__))
    engine = create_engine('sqlite:///:memory:', echo=False)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    print ('''
     Creating these objects:
     
     w = Warrior('Dragon', 'male', 'human')
     m = Mage('Ewalanikoa', 'female', 'goblin')
     h = Hunter('kukanaloa', 'male', 'elf')
    ''')

    w = Warrior('Dragon', 'male', 'human')
    m = Mage('Ewalanikoa', 'female', 'goblin')
    h = Hunter('kukanaloa', 'male', 'elf')

    print('Adding {}, a {} to the database'.format( w.name, w.__class__.name))
    session.add(w);
    print('Adding {}, a {} to the database'.format(m.name, m.__class__.name))
    session.add(m);
    print('Adding {}, a {} to the database'.format(h.name, h.__class__.name))
    session.add(h);

    session.commit()
    print()

    print("Retrieving Characters Created Above")
    for row in session.query(CharacterClass).all():
        print('{:3} {}, {}, {},'.format(row.id, row.name, row.gender, row.race))


main()
