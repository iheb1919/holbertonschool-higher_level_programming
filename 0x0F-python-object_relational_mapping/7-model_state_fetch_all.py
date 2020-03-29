#!/usr/bin/python3
# fetchall sqlalchemy
if __name__ == "__main__":
    import sys
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = session(bind=engine)
    session = sessionmaker()
    for queryy in session.query(State).order_by(State.id):
        print("{}: {}".format(queryy.id, queryy.name))
