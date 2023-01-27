import os
import json
import logging.config
from getpass import getpass
from shoppingList import Product
from user import User, EnterUserName
from userHelp import Help
from helper.enums import ExitCommands, DiscountCodes
from helper.exceptions import PasswordIsShort, NameISNotStringException
from helper.messages import (ExitShoppingListMessage as msg,
DisplayCategoryMessage as category,
RaiseValidOptionMessage as message,
DisplayBalanceMessage as balance,
DisplayBuyCategoryMessage as buy,
AddCategoryMessage as add,
RemoveCategoryItemsMessage as remove,
EditCategoryMessage as edit,
SearchCategoryMessage as search,)
cosmetics_bill: list = list()
vegetable_bill: list = list()
grocery_bill: list = list()


logging.config.fileConfig(fname='Log/config.toml', disable_existing_loggers=False)  #noqa:E501
logger = logging.getLogger(__name__)


while True:
    first_name = input('please enter your firstname:')
    last_name = input('please enter your lastname:')
    try:
        if first_name.isnumeric():
            raise NameISNotStringException
    except NameISNotStringException as e:
        print(e)
    else:
        information = EnterUserName(first_name, last_name)
        print(f"Hi {information} . welcome to shopping list. ")
        logger.info(f'user {first_name} {last_name} arrived into shopping list . ')  #noqa:E501
        logger.info(f"os user name: {os.getlogin()}")
        break        
os.system ('pause')


is_authenticated = False
while is_authenticated == False:
    try:
        print('please enter one option in line below')
        print('1) register  2) login')
        option = input('enter number of option :')
        if option == '1':
            is_registered = False
            while is_registered == False:
                username = input('enter username :')
                if not len(username.strip()):
                    print('OOoops !! invalid option , please try again .')
                    break
                else:
                    password= getpass('enter password :')
                    user = User(username, password )
                    User.register_file(username, password)
                    print('register successfully done !!!')
                    print('to continue please login .')
                    username = input('enter username :')
                    User.login_user(username)
                    is_authenticated = True
                    is_registered = True
        elif option == '2':
            is_login = False
            while is_login == False:
                username = input('enter username :')
                if not len(username.strip()):
                    print('OOoops !! invalid option , please try again .')
                    break
                else:
                    User.login_user(username)
                    is_authenticated = True
                    is_login = True
    except PasswordIsShort as e :
            print(e)
Help().display_help()


while True:
    print("\N{pushpin}", "\N{pushpin}", "\N{pushpin}", "\N{pushpin}", "\N{pushpin}", "\N{pushpin}", "\N{pushpin}", "\N{pushpin}")
    option = input('please enter one option :')
    for command in ExitCommands:
        value = command.name
        if option == value:
            print(msg.FIRST_EXIT_MESSAGE)
            print(msg.SECOND_EXIT_MESSAGE)
            logger.info('user exited from shop !!!!')
            break
    if option == 'price':
        question = input(category.DISPLAY_MESSAGE)
        if question == '1':
            print("\N{peanuts}" ,"GROCERY PRICES", "\N{peanuts}")
            Product().grocery_price()
        elif question == '2':
            print("\N{nail polish}" , "COSMETICS PRICES", "\N{nail polish}")
            Product().cosmetics_price()
        elif question == '3':
            print("\N{leafy green}" , "VEGETABLE PRICES", "\N{leafy green}" )
            Product().vegetable_price()
        else:
            print(message.VALID_MESSAGE)
    elif option == 'buy':
        print("\N{money bag}")
        print(buy.DISPLAY_FESTIVAL_MESSAGE, "\N{face with monocle}")
        print(buy.DISPLAY_ACCOUNT_MESSAGE, "\N{face with monocle}")
        code = DiscountCodes.get_random_code()
        print(f"your discount code is {code}")
        account_balance:int = int(input(balance.ACCOUNT_BALANCE))
        Product().use_discount(account_balance, code)
        # clear_screen()
        question:str = input(buy.BUY_CATEGORY_QUESTION)
        if question == '1':
            grocery:str = 'grocery'
            with open('database/grocery-items.json') as groceries:
                Product().buy_categories(groceries, grocery_bill, grocery, account_balance)  #noqa:E501
        elif question == '2':
            cosmetic:str = 'cosmetic'
            with open('database/cosmetics-items.json') as cosmetics:
                Product().buy_categories(cosmetics, cosmetics_bill, cosmetic, account_balance)  #noqa:E501
        elif question == '3':
            vegetable:str = 'vegetable'
            with open('database/vegetable-items.json') as vegetables:
                Product().buy_categories(vegetables, vegetable_bill, vegetable, account_balance)  #noqa:E501
        else:
            print(message.VALID_MESSAGE)   
    elif option == 'add':
        print("\N{money bag}")
        question:str = input(add.ADD_CATEGORY_QUESTION).casefold()
        # call clearscreen fnc()
        # clear_screen()
        # condition if question equal to 1
        if question == '1':
            items_number:int = int(input(add.NUMBER_ITEM_QUESTION))
            Product().add_grocery(items_number)
        elif question == '2':
            items_number:int = int(input(add.NUMBER_ITEM_QUESTION))
            Product().add_cosmetics(items_number)
        elif question == '3':
            items_number:int = int(input(add.NUMBER_ITEM_QUESTION))
            Product().add_vegetable(items_number)
        else:
            print(message.VALID_MESSAGE)    
    elif option == 'show':
        question:str = input(category.DISPLAY_MESSAGE)
        # clear_screen()
        if question == '2':
            with open('database/cosmetics-items.json', 'r') as files:
                Product().show_category(files)
        elif question == '3':
            with open('database/vegetable-items.json', 'r') as files:
                Product().show_category(files)
        elif question == '1':
            with open('database/grocery-items.json', 'r') as files:
                Product().show_category(files)
        else:
            print(message.VALID_MESSAGE)
    elif option == 'remove':
        question:str = input(remove.REMOVE_CATEGORY_QUESTION)
        if question == '1':
            item = input(remove.REMOVE_ITEM_QUESTION)
            Product().remove_grocery(item)
        elif question == '2':
            item = input(remove.REMOVE_ITEM_QUESTION)
            Product().remove_cosmetics(item)
        elif question == '3':
            item = input(remove.REMOVE_ITEM_QUESTION)
            Product().remove_vegetable(item)
        else:
            print(message.VALID_MESSAGE)
    elif option == 'edit':
        edit_question = input(edit.EDIT_CATEGORY_QUESTION )
        # clear_screen()
        if edit_question == '1':
            edit_item = input(edit.CHOOSE_SPECIFIC_ITEM)
            item_edit_with = input(edit.EDIT_SPECIFIC_ITEM)
            Product().edit_grocery(edit_item, item_edit_with)
        elif edit_question == '2':
            edit_item = input(edit.CHOOSE_SPECIFIC_ITEM)
            item_edit_with = input(edit.EDIT_SPECIFIC_ITEM)
            Product().edit_cosmetics(edit_item, item_edit_with)
        elif edit_question == '3':
            edit_item = input(edit.CHOOSE_SPECIFIC_ITEM)
            item_edit_with = input(edit.EDIT_SPECIFIC_ITEM)
            Product().edit_vegetable(edit_item, item_edit_with)
        else:
            print(message.VALID_MESSAGE)
    elif option == 'search':
        question:str = input(search.SEARCH_CATEGORY_QUESTION)
        if question == '1':
            search_item = input(search.SEARCH_INTENDED_ITEM)
            Product().search_grocery(search_item)
        elif question == '2':
            search_item = input(search.SEARCH_INTENDED_ITEM)
            Product().search_cosmetics(search_item)
        elif question == '3':
            search_item = input(search.SEARCH_INTENDED_ITEM)
            Product().search_vegetable(search_item)
        else:
            print(message.VALID_MESSAGE)
    elif option == 'history':
        Product().user_history()
    elif option == 'help':
        Help().display_help()
    else:
        print(message.VALID_MESSAGE)



    