#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True
            )
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    query = (session.query(City, State)
             .outerjoin(State, City.state_id == State.id)
             .order_by(City.id))
    for city, state in query.all():
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
