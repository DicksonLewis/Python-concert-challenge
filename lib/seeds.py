from models import Band, Venue, Concert, Base, engine
from sqlalchemy.orm import sessionmaker

# Creating a session
Session = sessionmaker(bind=engine)
session = Session()

# Dropping all tables and recreating them
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Create a few bands
band1 = Band(name="The Beatles", hometown="Liverpool")
band2 = Band(name="The Rolling Stones", hometown="London")
band3 = Band(name="Led Zeppelin", hometown="London")

# Create a few venues
venue1 = Venue(title="The Cavern Club", city="Liverpool")
venue2 = Venue(title="Royal Albert Hall", city="London")
venue3 = Venue(title="Madison Square Garden", city="New York")

# Add concerts
concert1 = Concert(band=band1, venue=venue1, date="1962-08-01")
concert2 = Concert(band=band2, venue=venue2, date="1969-01-01")
concert3 = Concert(band=band3, venue=venue3, date="1971-07-01")
concert4 = Concert(band=band1, venue=venue3, date="1965-08-15")
concert5 = Concert(band=band2, venue=venue1, date="1966-07-02")
concert6 = Concert(band=band3, venue=venue2, date="1970-09-15")

# Add all to the session
session.add_all([band1, band2, band3, venue1, venue2, venue3, concert1, concert2, concert3, concert4, concert5, concert6])

# Commit the session
session.commit()

# Closing the session
session.close()

print("Database seeded successfully!")
