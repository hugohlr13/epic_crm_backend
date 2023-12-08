import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import Base, Utilisateur, Role

@pytest.fixture
def db_session():
    """
    Creates an in-memory database session for testing.
    """
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

def test_user_creation(db_session):
    """
    Test for creating and retrieving a user in the database.
    """
    user = Utilisateur(numero_employe=123,nom="Test User", email="testuser@example.com", departement="Commercial")
    user.set_password("securepassword")
    db_session.add(user)
    db_session.commit()
    retrieved_user = db_session.query(Utilisateur).filter_by(email="testuser@example.com").first()
    assert retrieved_user is not None
    assert retrieved_user.check_password("securepassword") is True

def test_user_with_role_creation(db_session):
    """
    Integration test for creating a user with a role in the database.
    """
    role = Role(nom="Commercial", permissions="create_view_clients")
    db_session.add(role)
    user = Utilisateur(numero_employe=123, nom="Test User", email="testuser@example.com", departement="Commercial")
    user.set_password("securepassword")
    user.role = role
    db_session.add(user)
    db_session.commit()
    retrieved_user = db_session.query(Utilisateur).filter(Utilisateur.email == "testuser@example.com").first()
    assert retrieved_user is not None
    assert retrieved_user.role.nom == "Commercial"