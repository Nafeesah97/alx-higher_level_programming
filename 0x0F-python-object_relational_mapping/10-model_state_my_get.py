#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


from sqlalchemy import (create_engine)

if __name__ == "__main__":
    state_to_be = sys.argv[4]
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True
            )
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    query = session.query(State).filter(State.name == state_to_be)
    row = query.first()
    if (row is None):
        print('Not found')
    else:
        print('{}'.format(row.id))