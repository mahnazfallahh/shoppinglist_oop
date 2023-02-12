import json
import logging.config
from dataclasses import dataclass
from painless.helper.exceptions import PasswordIsShort, NameISNotStringException # noqa E501


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


class PasswordDescriptors:
    """ class PasswordDescriptors which include password descriptors
    """
    def __set_name__(self, owner, title):
        self.title = title

    def __get__(self, instance, owner):
        return instance.__dict__[self.title]

    def __set__(self, instance, value):
        if len(value) <= 3:
            raise PasswordIsShort
        instance.__dict__[self.title] = value


class UserNameDescriptors:
    """ class UserNameDescriptors which include username descriptors
    """
    def __set_name__(self, owner, title):
        self.title = title

    def __get__(self, instance, owner):
        return instance.__dict__[self.title]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise NameISNotStringException
        instance.__dict__[self.title] = value


class BaseUser():
    """ class BaseUser which give username and password
    """
    username = UserNameDescriptors()
    password = PasswordDescriptors()

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


class User(BaseUser):
    """ class User which register and login user
        Parameters
        ----------
        variable1 :
            BaseUser is a parent class.
    """

    def register_user(self, username: str, password: any):
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
