import random
from enum import Enum


class DiscountCodes(Enum):
    """ class discount which inheritance from Enum
    use to keep discount codes .
    Parameters
    ----------
    Enum
    """
    spring_discount_code = 'first_code',
    summer_discount_code = 'second_code',
    autumn_discount_code = 'third_code'

    @classmethod
    def get_random_code(cls):
        """ method to choose random of discount code
        Parameters
        ----------
        cls
        """
        code = random.choice(cls._member_names_)
        return code


class ExitCommands(Enum):
    """ class to keep exit commands in Enum class
    Parameters
    ----------
    Enum
    """
    q = 'q',
    e = 'e',
    Q = 'Q'
