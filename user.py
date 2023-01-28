import json
import logging.config
from dataclasses import dataclass
from helper.exceptions import PasswordIsShort, NameISNotStringException

register: dict = dict()

logger = logging.getLogger(__name__)


@dataclass
class EnterUserName:
    """ class EnterUserName which is dataclass use to return first name
    and last name """
    first_name: str
    last_name: str

    def __str__(self):
        """ method to return firstname and lastname
        Parameters
        ----------
        self 
        """
        return f'{self.first_name}{self.last_name}'


class BaseUser():
    """ class BaseUser which give username and password
    """
    def __init__(self, username: str, password: int):
        """ constructor
        method to initialize username and password 
        Parameters
        ----------
        variable1 : 
            self
        variable2 :
            username
        variable3 :
            password
        """
        self.username = username
        self.password = password    
    @property
    def username(self):
        """ getter to get username
        Parameters
        ----------
        variable1 : 
            self
        """
        return self.__username

    @username.setter
    def username(self, value: str):
        """ setter to set username
        Parameters
        ----------
        variable1 : 
            self
        variable1 : 
            value
        """
        if isinstance(value, int):
            raise NameISNotStringException
        self.__username = value

    @property
    def password(self):
        """ getter to get password

        Parameters
        ----------
        variable1 : 
            self
        """
        return self.__password
    
    @password.setter
    def password(self, value:any):
        """ setter to set password

        Parameters
        ----------
        variable1 : 
            self
        variable1 : 
            value
        """
        if len(value) <= 3:
            raise PasswordIsShort
        self.__password = value

    def __str__(self):
        """ use magic method str to display user name and password.

        Parameters
        ----------
        variable1 : 
            self
        """
        return f" {self.username} , {self.password}"


class User(BaseUser):
    """ class User which register and login user
        Parameters
        ----------
        variable1 : 
            BaseUser is a parent class.
    """    
    def register_user(self ,username: str, password: any):
        """ method to initialize username and password .
        Parameters
        ----------
        variable1 : 
            self
        variable2 : 
            username
        variable3 : 
            password
        """
        super().__init__(username, password)
        return self

    def register_file(username: str, password: any):
        """ method to register user.
        Parameters
        ----------
        variable1 : 
            username
        variable2 : 
            password
        """
        with open('database/register.json', 'w') as user_register:
            register[username] = password
            json.dump(register, user_register)
            logger.info(f'user {username} registered successfully !!!')

def login_user(username: str):
        """ method to login user.
        Parameters
        ----------
        variable1 : 
            username
        """
        with open('database/register.json') as login_user:
            login = json.load(login_user)
            if username in login:
                print('you logged in successfully! ')
                logger.info(f'user {username} login successfully!!')
            else:
                print('user name is not into the database .')
        
