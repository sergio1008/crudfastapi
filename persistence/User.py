
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from config.db import engine

Base = declarative_base()



class User(Base):
    __tablename__ = "USUARIOS"    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    description = Column(String)        
        


Base.metadata.create_all(engine)