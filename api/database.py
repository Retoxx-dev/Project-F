from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os

DBUSER = os.environ["DBUSER"]
DBPASSWORD = os.environ["DBPASSWORD"]
DBNAME = os.environ["DBNAME"]

SQLALCHEMY_DATABASE_URL = f"mysql://{DBUSER}:{DBPASSWORD}@db/{DBNAME}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, encoding='latin1', echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()