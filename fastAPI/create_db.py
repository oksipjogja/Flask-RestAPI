from database import Base,engine
from models import Item

print('Creating Databse ....')\

Base.metadata.create_all(engine)