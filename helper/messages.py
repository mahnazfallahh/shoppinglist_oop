from enum import StrEnum


class ExitShoppingListMessage(StrEnum):
    """ class ExitShoppingListMessage which include exit commands messages
    Parameters
    ----------
    StrEnum:
        is a parent class
    """
    FIRST_EXIT_MESSAGE = "you exit from SHOPPING LIST !"
    SECOND_EXIT_MESSAGE = "HOPE TO SEE YOU SOON !"


class DisplayCategoryMessage(StrEnum):
    """ class DisplayCategoryMessage which include display category messages
    Parameters
    ----------
    StrEnum:
        is a parent class
    """
    DISPLAY_MESSAGE = "which category do you want to see ?"


class RaiseValidOptionMessage(StrEnum):
    """ class RaiseValidOptionMessage which include raise valid option messages
    Parameters
    ----------
    StrEnum:
        is a parent class
    """
    VALID_MESSAGE = "please enter valid option ."


class DisplayBalanceMessage(StrEnum):
    """ class DisplayBalanceMessage which include account balance messages
    Parameters
    ----------
    StrEnum:
        is a parent class
    """
    ACCOUNT_BALANCE = "please enter your account balance :"


class DisplayBuyCategoryMessage(StrEnum):
    """ class DisplayBuyCategoryMessage which include buy category messages
    Parameters
    ----------
    StrEnum:
        is a parent class
    """
    BUY_CATEGORY_QUESTION = "which category do you want to buy ?"
    DISPLAY_FESTIVAL_MESSAGE = "we have a seasonal festival Here."
    DISPLAY_ACCOUNT_MESSAGE = "if you choose discount code Your account balance will increase by 5%"


class AddCategoryMessage(StrEnum):
    """ class AddCategoryMessage which include add category messages
    Parameters
    ----------
    StrEnum:
        is a parent class
    """
    ADD_CATEGORY_QUESTION = "which category do you want to add ?"
    NUMBER_ITEM_QUESTION = "how many items do you want add ?"


class RemoveCategoryItemsMessage(StrEnum):
    """ class RemoveCategoryItemsMessage which include remove category messages
    Parameters
    ----------
    StrEnum:
        is a parent class
    """
    REMOVE_CATEGORY_QUESTION = "which category do you want to remove ?"
    REMOVE_ITEM_QUESTION = "which item do you want to remove ?"


class EditCategoryMessage(StrEnum):
    """ class EditCategoryMessage which include edit category messages
    Parameters
    ----------
    StrEnum:
        is a parent class
    """
    EDIT_CATEGORY_QUESTION = "which category do you want to edit ?"
    CHOOSE_SPECIFIC_ITEM = "enter which item do you want edit it ?"
    EDIT_SPECIFIC_ITEM = "enter which item do you want edit it with?"


class SearchCategoryMessage(StrEnum):
    """ class SearchCategoryMessage which include search category messages
    Parameters
    ----------
    StrEnum:
        is a parent class
    """
    SEARCH_CATEGORY_QUESTION = "which category do you want to search ?"
    SEARCH_INTENDED_ITEM = "please enter your intended item :"


class DisplayUserQuestion(StrEnum):
    FIRST_NAME = "please enter your firstname:"
    LAST_NAME = "please enter your lastname:"
    



