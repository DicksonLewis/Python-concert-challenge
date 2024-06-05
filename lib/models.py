import os
import sys

sys.path.append(os.getcwd())

from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine('sqlite:///lib/db/concerts.db', echo=True)

class Band(Base):
    __tablename__ = 'bands'

    id = Column(Integer, primary_key=True)
    name = Column(String())
    hometown = Column(String())

    concerts = relationship('Concert', back_populates='band')

    def __repr__(self):
        return f'Band: {self.name}'

class Venue(Base):
    __tablename__ = 'venues'

    id = Column(Integer, primary_key=True)
    title = Column(String())
    city = Column(String())

    concerts = relationship('Concert', back_populates='venue')

    def __repr__(self):
        return f'Venue: {self.title}'

class Concert(Base):
    __tablename__ = 'concerts'

    id = Column(Integer, primary_key=True)
    band_id = Column(Integer, ForeignKey('bands.id'))
    venue_id = Column(Integer, ForeignKey('venues.id'))
    date = Column(String())

    band = relationship('Band', back_populates='concerts')
    venue = relationship('Venue', back_populates='concerts')

    def __repr__(self):
        return f'Concert: {self.date} - {self.band.name} at {self.venue.title}'

# Create tables
Base.metadata.create_all(engine)
