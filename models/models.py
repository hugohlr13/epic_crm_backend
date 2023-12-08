from sqlalchemy import Column, Integer, String, Float, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
import bcrypt

Base = declarative_base()

class Client(Base):
    """
    Represents a client in the CRM system.
    """
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    nom_complet = Column(String, nullable=False)
    email = Column(String, nullable=False)
    telephone = Column(String)
    nom_entreprise = Column(String)
    date_creation = Column(Date)
    derniere_mise_a_jour = Column(Date)
    contact_commercial = Column(String)
    # Relations
    contrats = relationship("Contrat", back_populates="client")

class Contrat(Base):
    """
    Represents a contract in the CRM system.
    """
    __tablename__ = 'contrats'
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('clients.id'))
    contact_commercial = Column(String)
    montant_total = Column(Float)
    montant_restant = Column(Float)
    date_creation = Column(Date)
    statut = Column(String)
    # Relations
    client = relationship("Client", back_populates="contrats")
    evenements = relationship("Evenement", back_populates="contrat")

class Evenement(Base):
    """
    Represents an event in the CRM system.
    """
    __tablename__ = 'evenements'
    id = Column(Integer, primary_key=True)
    contrat_id = Column(Integer, ForeignKey('contrats.id'))
    date_debut = Column(DateTime)
    date_fin = Column(DateTime)
    contact_support = Column(String)
    lieu = Column(String)
    nombre_participants = Column(Integer)
    notes = Column(String)
    # Relations
    contrat = relationship("Contrat", back_populates="evenements")

class Role(Base):
    """
    Represents a role in the CRM system.
    """
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    nom = Column(String, nullable=False)
    permissions = Column(String)
    # Relations
    utilisateurs = relationship("Utilisateur", back_populates="role") #easier for SQL Requet : User with Role A


class Utilisateur(Base):
    """
    Represents a user in the CRM system.
    """
    __tablename__ = 'utilisateurs'
    id = Column(Integer, primary_key=True)
    numero_employe = Column(Integer, unique=True, nullable=False)
    nom = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    departement = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    role_id = Column(Integer, ForeignKey('roles.id'))
    # Relations
    role = relationship("Role")

    def set_password(self, password):
        self.hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.hashed_password.encode('utf-8'))

