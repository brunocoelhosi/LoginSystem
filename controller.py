from operator import and_
from models import Usuario
import hashlib 

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Usuario


def RetornaSession():

    HOST = "localhost"
    USUARIO = "root"
    SENHA = ""
    PORT = "3306"
    BANCO = "aulapythonfull"

    CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

    engine = create_engine(CONN, echo = True)
    Session = sessionmaker(bind=engine)
    return Session()

class UsuarioController:

    def verifica_dados(cls, nome, email, senha):
        if len(nome) > 50:
            return 2
        if len(email) > 200:
            return 2
        if len(senha) > 100:
            return 4
        return 1

    def cadastrarUsuario(cls, nome, email, senha):

        session = RetornaSession()

        usuario = session.query(Usuario).filter(Usuario.email == email).all()
        if len(usuario) > 0:
            return 5
        
        dadosverificados = cls.verifica_dados(nome,email,senha)

        if dadosverificados != 1:
            return dadosverificados
        
        try:
            senha = hashlib.sha256(senha.encode()).hexdigest()
            x = Usuario(nome = nome,
                        email = email,
                        senha = senha)
            session.add(x)
            session.commit()
            return 1

        except:
            return 6
        
class LoginController:

    def realizarLogin(self, email, senha):

        session = RetornaSession()
        senha = hashlib.sha256(senha.encode()).hexdigest()
        x = session.query(Usuario).filter(and_(Usuario.email == email, Usuario.senha == senha)).all()
        if len(x)>0:
            return {'logado': True, 'id':x[0].id}
        else: 
            return False
    


