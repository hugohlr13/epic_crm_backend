from models.models import Utilisateur, Base, Role
from database import Session
import bcrypt

session = Session()

# User creation
user = Utilisateur(
    numero_employe=1,
    nom="Nom Utilisateur",
    email="email@example.com",
    departement="Commercial",
)
user.set_password("password123")  

# Add and save user to db
session.add(user)
session.commit()
