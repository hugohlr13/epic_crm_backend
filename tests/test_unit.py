import pytest
from models.models import Utilisateur, Role

@pytest.fixture
def user_sample():
    """
    Provides a sample user for testing.
    """
    user = Utilisateur(nom="Test User", email="testuser@example.com", departement="Commercial")
    user.set_password("securepassword")
    return user

def test_password_hashing(user_sample):
    """
    Test for password hashing and verification.
    """
    user = user_sample
    assert user.check_password("securepassword") is True
    assert user.check_password("wrongpassword") is False

@pytest.fixture
def role_sample():
    """
    Provides a sample role for testing.
    """
    return Role(nom="Commercial", permissions="create_view_clients")

def test_user_role_association(user_sample, role_sample):
    """
    Test to ensure that a user is correctly associated with a role.
    """
    user = user_sample
    user.role = role_sample
    assert user.role.nom == "Commercial"
    assert user.role.permissions == "create_view_clients"

