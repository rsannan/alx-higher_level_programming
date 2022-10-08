#!/usr/bin/python3
"""
Changes the name of the State object with id = 2 to
New Mexico in the database hbtn_0e_6_usa.
Usage: ./12-model_state_update_id_2.py <mysql username> /
                                       <mysql password> /
                                       <database name>
"""
from sys import argv
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    sess = Session()
    for instance in sess.query(State).order_by(states.id):
        if instance.id == 2:
            instance.name = "New Mexico"
            break
    session.commit()
