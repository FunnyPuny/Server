import psycopg2
import sqlalchemy as db
from sqlalchemy.orm import declarative_base
from db_config import user, password, host, port, db_name
from sqlalchemy import create_engine, Column, Integer, String

import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='sqlalchemy')


url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}"
engine = create_engine(url)

Base = declarative_base()

class Users(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String)

Base.metadata.create_all(bind=engine)
print('Done')