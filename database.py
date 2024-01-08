from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import Base

# Database connection URL.
DATABASE_URL = "sqlite:///epic_events_crm.db"

# Creating an engine. This is the starting point for any SQLAlchemy application.
engine = create_engine(DATABASE_URL, echo=True)

# Creating a sessionm
Session = sessionmaker(bind=engine)

def init_db():
    """
    Initializes the database.
    """
    Base.metadata.create_all(engine)