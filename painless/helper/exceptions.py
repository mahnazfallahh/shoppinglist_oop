

class PasswordIsShort(ValueError):
    """ class PasswordIsShort
    Parameters
    ----------
    ValueError:
        is a parent class
    """
    def __str__(self):
        """ use magic method str to display message
        Parameters
        ----------
        self
    """
        return "password is too short . "


class NameISNotStringException(TypeError):
    """ class NameISNotStringException
    Parameters
    ----------
    TypeError:
        is a parent class
    """
    def __str__(self):
        """ use magic method str to display message
        Parameters
        ----------
        self
    """
        return "first name can't be a number ."
