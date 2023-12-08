from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import Base

# Database connection URL. In this case, we are using SQLite.
DATABASE_URL = "sqlite:///epic_events_crm.db"

# Creating an engine. This is the starting point for any SQLAlchemy application.
# 'echo=True' will log all generated SQL statements, which is helpful for debugging.
engine = create_engine(DATABASE_URL, echo=True)

# Creating a sessionmaker, bound to our engine. This factory will provide us
# with new Session objects connected to the database.
Session = sessionmaker(bind=engine)

def init_db():
    """
    Initializes the database.

    This function creates all tables defined in the models module
    using the metadata that SQLAlchemy collects from the Base class.
    It's safe to run this function multiple times as it doesn't
    recreate existing tables.
    """
    Base.metadata.create_all(engine)