from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

HOST = "localhost"
USUARIO = "root"
SENHA = ""
PORT = "3306"
BANCO = "aulapythonfull"

CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

engine = create_engine(CONN, echo = True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Usuario(Base):
    __tablename__ = "Usuario"
    id = Column(Integer, primary_key = True)
    nome = Column(String(50))
    email = Column(String(10))
    senha = Column(String(100))

Base.metadata.create_all(engine) 