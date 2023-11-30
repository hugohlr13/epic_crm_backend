from sqlalchemy import Column, Integer, String, Float, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Client(Base):
    """
    Represents a client in the CRM system.
    
    Attributes:
        id (int): Unique identifier for the client.
        nom_complet (str): Full name of the client.
        email (str): Email address of the client.
        telephone (str): Phone number of the client.
        nom_entreprise (str): Name of the client's company.
        date_creation (date): Date when the client was first contacted.
        derniere_mise_a_jour (date): Date of the last update or contact.
        contact_commercial (str): Name of the associated commercial contact.
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
    
    Attributes:
        id (int): Unique identifier for the contract.
        client_id (int): Reference to the associated client.
        contact_commercial (str): Name of the commercial contact for the contract.
        montant_total (float): Total amount of the contract.
        montant_restant (float): Remaining amount to be paid.
        date_creation (date): Creation date of the contract.
        statut (str): Status of the contract (e.g., signed or not).
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
    
    Attributes:
        id (int): Unique identifier for the event.
        contrat_id (int): Reference to the associated contract.
        date_debut (datetime): Start date and time of the event.
        date_fin (datetime): End date and time of the event.
        contact_support (str): Name of the support contact responsible for the event.
        lieu (str): Location of the event.
        nombre_participants (int): Number of participants.
        notes (str): Additional details about the event.
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
