from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker





url_banco = 'sqlite:///C:/Users/User/Desktop/⠀⠀/Programação/Git/Hosrtfruit/DataBase/hortfuit.db'
engine = create_engine(url_banco, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Hortfruit(Base):
    __tablename__ = 'hortfruit'

    id = Column(Integer, primary_key=True)
    nome = Column(String(120))
    codigo = Column(String(20))

def x():
    x = session.query(Hortfruit).all()
    print(x)
x()


