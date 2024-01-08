import jwt
import os
from database import Session  
from models.models import Utilisateur
from dotenv import load_dotenv
import bcrypt

load_dotenv()
SECRET_KEY = os.environ.get('JWT_SECRET_KEY')

def authenticate_user(email, password):
    """
    Authenticate a user and return a JWT token.
    """
    session = Session() 
    user = session.query(Utilisateur).filter_by(email=email).first()

    if user and bcrypt.checkpw(password.encode('utf-8'), user.hashed_password.encode('utf-8')):
        # JWT creation
        token = jwt.encode({'user_id': user.id, 'email': user.email}, SECRET_KEY, algorithm='HS256')
        session.close()
        return token
    
    session.close()
    return None

def authorize_user(token):
    """
    Validates a JWT token and checks user permissions.
    """
    try:
        # Decoding the JWT token
        user_data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])

        # Retrieve user information and permissions
        session = Session()
        user = session.query(Utilisateur).filter_by(id=user_data['user_id']).first()
        if user:
            return {
                'user_id': user.id,
                'email': user.email,
                'permissions': user.role.permissions
            }
    except jwt.ExpiredSignatureError:
        print("Le jeton a expiré.")
    except jwt.InvalidTokenError:
        print("Jeton invalide.")

    return None