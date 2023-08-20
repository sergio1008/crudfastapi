from sqlalchemy import Connection
from dto.UserDTO import UserDTO
from config.db import engine, Session
from persistence.User import User
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""
class UserService:
    def __init__(self):
        self.session = Session()      
    
    """
        Permite crear un usuario
    """    
    def create(self, user: UserDTO):
        with engine.connect() as con:
            user = User(id =user.id, username = user.username, description= user.description)
            self.session.add(user)
            self.session.commit()
            con.close()
            
    """ Retorna todos los usuarios
    """
    
    def getAll(self):
        with engine.connect() as con:
            users_query = self.session.query(User)
            users = users_query.all()
            con.close()
            return users