from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
password = os.environ.get("POSTGRESQL_PWD")
engine = create_engine(f"postgresql://magot:{password}@localhost:5432/item_db",echo=True)

Base = declarative_base()

SessionLocal=sessionmaker(bind=engine)

