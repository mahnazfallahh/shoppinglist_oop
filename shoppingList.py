import json
import random
import datetime
import pandas as pd
import logging.config
from json import JSONEncoder

grocery_items: dict = dict()
cosmetics_items: dict = dict()
vegetable_items: dict = dict()
cosmetics_bill: list = list()
vegetable_bill: list = list()
grocery_bill: list = list()
user_history: dict = dict()
logger = logging.getLogger('admin')

class DateTimeEncoder(JSONEncoder):
    """ class datetime encoder 
        Parameters
        ----------
        variable1 : 
            jsonencoder is parent class"""
    def default(self, obj:int):
        """ override default method in datetime encoder in order to convert datetime 
        value into Isoformat in order to serialize it which can write it in json file.
        Parameters
        ----------
        self
        obj
        """
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()


class Product():
    """ class Product which include product method like buy categories .
    """

    @staticmethod
    def user_history():
        """ method for display user history. read json file and iterate
        into file to display value key """
        with open('database\history.json') as history:
            data = json.load(history)
            for key, value in data.items():
                print(key, "---->", value)

    
    @staticmethod
    def use_discount(account_balance:int, code:str) -> int:
        """ method to calculate account balance which multiple it into 0.5 increase it and
        display to user 
        Parameters
        ----------
        variable1 : 
            account_balance is account balance of user.
        variable2 :
            code which it's discount code ."""
        result = account_balance * 0.5
        print(f"your account balance is {result} dollars now", "\N{money bag}") 
    
    
    @staticmethod
    def grocery_price():
        """ method for display grocery prices and items in one simple table """
        data = {
            '': [90000, 1000, 80000]
        }
        grocery = pd.DataFrame(data, index=['walnut', 'rice', 'sugar'])
        print(grocery)
        logger.info(f'user see grocery prices !!')

    @staticmethod
    def vegetable_price():
        """ method for display vegetable prices and items in one simple table """
        data = {
            '': [4000, 40000, 1000]
        }
        vegetable = pd.DataFrame(data, index=['cucumber', 'carrot', 'lettuce'])
        print(vegetable)
        logger.info(f'user see vegetable prices !!')
    
    @staticmethod
    def cosmetics_price():
        """ method for display cosmetics prices and items in one simple table """
        data = {
            '': [3400000, 1200, 340000]
        }
        cosmetics = pd.DataFrame(data, index=['lipstick', 'cream', 'spray'])
        print(cosmetics)
        logger.info(f'user see cosmetics prices !!')

    @staticmethod
    def buy_categories(categories, category_bill:list[int],
    bill_name:str, 
    account_balance:int) -> int:
        """ iterate in specific items in to the list and iterate in users items
    to access into number of products and prices.    
    Parameters
    ----------
    var1 : categories
            categories is a variable which we open json file with it.
    var2 : category_bill
            is category bill parameter like grocery bill.
    var3 : bill_name
            as show as it is a variable for bill name.
    var4 : account_balance
            it's  account balance of user .
    """
        category:dict = json.load(categories)
        lines:list = [line for line in category]
        with open('database/shopping-list.json') as files:
            data:dict = json.load(files)
            for line in lines:
                for key, value in data.items():
                    if line == key:
                        price:list = data[line]['price']
                        product_number:int = int(category.get(line))
                        total_sum:int = price * product_number
                        category_bill.append(total_sum)
                        bill:int = sum(category_bill)
                        if bill > account_balance:
                            print("OOoops, sorry ! you don't have enough money to buy your list.","\N{slightly frowning face}")
                            with open('database/history.json') as files:
                                user_history["account_balance"] = account_balance
                                user_history["is_buy"] = "you couldn't buy anything."
                                user_history["date_buy"] = datetime.datetime.now()
                                user_history["bill_name"] = bill_name
                                with open('database/history.json', 'w') as history:
                                    json.dump(user_history, history, indent=2, cls=DateTimeEncoder)
                        else:
                            balance:int = account_balance - bill
                            print("The purchase was made successfully!!","\N{smiling face with smiling eyes}")
                            print(f"your account balance is : {balance}")
                            logger.info(f'user buy {bill_name} lists !!')
                            with open('database/history.json') as files:
                                user_history["account_balance"] = balance
                                user_history["is_buy"] = "you bought your list ."
                                user_history["date_buy"] = datetime.datetime.now()
                                user_history["bill_name"] = bill_name
                                with open('database/history.json', 'w') as history:
                                    json.dump(user_history, history, indent=2, cls=DateTimeEncoder)
                                
            print(f" your {bill_name} bill is : {bill} dollars.")
            
    @staticmethod
    def add_grocery(items_number:int) -> dict:
        """ method to add into grocery list. 
        Parameters
        ----------
        variable1 : 
            items_number is number of items which user want to add into list"""
        with open('database/grocery-items.json', 'r+') as user_list:
                with open('database/shopping-list.json') as groceries:
                    grocery:dict = json.load(groceries)
                    # loop to iterate in items
                    for item in range(items_number):
                    # question from user
                        items:str = input('please enter your grocery items: ')
                        number_items:str = input('how many do you want from this item ?')
                        if items not in grocery:
                            print('OOops ! no such item is in shopping list.',"\N{slightly frowning face}")
                            print("Sorry ! we can't add it into the list .","\N{slightly frowning face}")
                        else:
                            grocery_items[items] = number_items
                            products_number:int = len(grocery_items)
                            print(f'{products_number} item added successfully in grocery list!!!')
                            logger.info('user add item into grocery list')
                            json.dump(grocery_items, user_list)
                        

    @staticmethod
    def add_cosmetics(items_number:int) -> dict:
        """ method to add into cosmetics list. 
        Parameters
        ----------
        variable1 : 
            items_number is number of items which user want to add into list"""
        with open('database/cosmetics-items.json', 'r+') as user_list:
                with open('database/shopping-list.json') as cosmetics:
                    cosmetic:dict = json.load(cosmetics)
                    # loop to iterate in items
                    for item in range(items_number):
                        # question from user
                        items:str = input('please enter your cosmetics items: ')
                        number_items:str = input('how many do you want from this item ?')  #noqa:E501
                        if items not in cosmetic:
                            print('OOops ! no such item is in shopping list.',"\N{slightly frowning face}")
                            print("Sorry ! we can't add it into the list .","\N{slightly frowning face}")
                        else:
                            cosmetics_items[items] = number_items
                            products_number:int = len(cosmetics_items)
                            print(f'{products_number} item added successfully in cosmetics list!!!')  #noqa:E501
                            logger.info('user add item into grocery list')
                    json.dump(cosmetics_items, user_list)
                    

    @staticmethod
    def add_vegetable(items_number:int) -> dict:
        """ method to add into vegetable list. 
        Parameters
        ----------
        variable1 : 
            items_number is number of items which user want to add into list"""
        with open('database/vegetable-items.json', 'r+') as user_list:
                with open('database/shopping-list.json') as vegetables:
                    vegetable:dict = json.load(vegetables)
                    # loop to iterate in items
                    for item in range(items_number):
                        # question from user
                        items = input('please enter your vegetable items: ')
                        number_items:str = input('how many do you want from this item ?')  #noqa:E501
                        if items not in vegetable:
                            print('OOops ! no such item is in shopping list.',"\N{slightly frowning face}")
                            print("Sorry ! we can't add it into the list .","\N{slightly frowning face}")
                        else:
                            vegetable_items[items] = number_items
                            products_number:int = len(vegetable_items)
                            print(f'{products_number}item added successfully in vegetables list!!!')  #noqa:E501
                            logger.info('user add item into grocery list')
                    json.dump(vegetable_items, user_list)
                    

    @staticmethod
    def show_category(files):
        """ function for iterate into the json file to display items of categories.
        Parameters
        ----------
        var1 : files
        """
        data:dict = json.load(files)
        print('your items are in the list below:',"\N{shopping bags}")
        for key in data.keys():
            print(key)

    @staticmethod
    def remove_grocery(item:str) -> str:
        """ method to remove item in grocery list. 
        Parameters
        ----------
        variable1 : 
            is specific item which user want to remove into the list"""
        with open('database/grocery-items.json') as grocery:
                data = json.load(grocery)
                if item in data:
                    data.pop(item)
                    with open('database/grocery-items.json', 'w') as files:
                        json.dump(data, files)
                        print(f'{item} removed from grocery list.')
                        logger.info(f'user removed {item} into grocery list')
                else:
                    print('OOoops ! no such item is in shopping list.')

    @staticmethod
    def remove_cosmetics(item:str) -> str:
        """ method to remove item in cosmetics list. 
        Parameters
        ----------
        variable1 : 
            is specific item which user want to remove into the list"""
        with open('database/cosmetics-items.json') as cosmetics:
                data = json.load(cosmetics)
                if item in data:
                    data.pop(item)
                    with open('database/cosmetics-items.json', 'w') as files:
                        json.dump(data, files)
                        print(f'{item} removed from cosmetics list.')
                        logger.info(f'user removed {item} into grocery list')
                else:
                    print('OOoops ! no such item is in shopping list.')

    @staticmethod
    def remove_vegetable(item:str) -> str:
        """ method to remove item in vegetable list. 
        Parameters
        ----------
        variable1 : 
            is specific item which user want to remove into the list"""
        with open('database/vegetable-items.json') as vegetable:
                data = json.load(vegetable)
                if item in data:
                    data.pop(item)
                    with open('database/vegetable-items.json', 'w') as files:
                        json.dump(data, files)
                        print(f'{item} removed from vegetable list.')
                        logger.info(f'user removed {item} into grocery list')
                else:
                    print('OOoops ! no such item is in shopping list.')

    @staticmethod
    def edit_grocery(edit_item:str, item_edit_with:str) -> str:
        """ method to edit item in grocery list. 
        Parameters
        ----------
        variable1 : 
            edit_item is specific item which user want to edit it
        variable2 : 
            item_edit_with is specific item which user want to edit it with edit_item"""
        with open('database/shopping-list.json') as files:
            data = json.load(files)
            with open('database/grocery-items.json') as groceries:
                grocery = json.load(groceries)
                if edit_item in grocery:
                    if item_edit_with in data:
                        grocery[item_edit_with] = grocery.pop(edit_item)
                        with open('database/grocery-items.json', 'w') as files:
                            json.dump(grocery, files)
                            print(f'{edit_item} modified into {item_edit_with} in your grocery list.')
                            logger.info(f'{edit_item} modified into {item_edit_with} in  grocery list.')
                    else:
                        print('OOoops ! no such item is in shopping list.')
                else:
                    print('OOoops ! no such item is in shopping list.')
    
    @staticmethod
    def edit_cosmetics(edit_item:str, item_edit_with:str) -> str:
        """ method to edit item in cosmetics list. 
        Parameters
        ----------
        variable1 : 
            edit_item is specific item which user want to edit it
        variable2 : 
            item_edit_with is specific item which user want to edit it with edit_item"""
        with open('database/shopping-list.json') as files:
                data = json.load(files)
                with open('database/cosmetics-items.json') as cosmetics:
                    cosmetic = json.load(cosmetics)
                    if edit_item in cosmetic:
                        if item_edit_with in data:
                            cosmetic[item_edit_with] = cosmetic.pop(edit_item)
                            with open('database/cosmetics-items.json', 'w') as files:
                                json.dump(cosmetic, files)
                                print(f'{edit_item} modified into {item_edit_with} in your cosmetics list.')  #noqa:E501
                                logger.info(f'{edit_item} modified into {item_edit_with} in  grocery list.')  #noqa:E501
                        else:
                            print('OOoops ! no such item is in shopping list.')
                    else:
                        print('OOoops ! no such item is in shopping list.')

    @staticmethod
    def edit_vegetable(edit_item:str, item_edit_with:str) -> str:
        """ method to edit item in vegetable list. 
        Parameters
        ----------
        variable1 : 
            edit_item is specific item which user want to edit it
        variable2 : 
            item_edit_with is specific item which user want to edit it with edit_item"""
        with open('database/shopping-list.json') as files:
                data = json.load(files)
                with open('database/vegetable-items.json') as vegetables:
                    vegetable = json.load(vegetables)
                    if edit_item in vegetable:
                        if item_edit_with in data:
                            vegetable[item_edit_with] = vegetable.pop(edit_item)  #noqa:E501
                            with open('database/vegetable-items.json', 'w') as files:  #noqa:E501
                                json.dump(vegetable, files)
                                print(f'{edit_item} modified into {item_edit_with} in your vegetable list.')  #noqa:E501
                                logger.info(f'{edit_item} modified into {item_edit_with} in  grocery list.')  #noqa:E501
                        else:
                            print('OOoops ! no such item is in shopping list.')
                    else:
                        print('OOoops ! no such item is in shopping list.')

    @staticmethod
    def search_grocery(search_item:str) -> str:
        """ method to search item in grocery list. 
        Parameters
        ----------
        variable1 : 
            search_item is specific item which user want search it"""
        with open('database/grocery-items.json')as files:
            data = json.load(files)
            if search_item in data:
                print(f'item you searched is : {search_item}')
                logger.info(f" user searched {search_item} in grocery list.")  #noqa:E501
            else:
                print('item is not into the list')

    @staticmethod
    def search_cosmetics(search_item:str) -> str:
        """ method to search item in cosmetics list. 
        Parameters
        ----------
        variable1 : 
            search_item is specific item which user want search it"""
        with open('database/cosmetics-items.json')as files:
            data = json.load(files)
            if search_item in data:
                print(f'item you searched is : {search_item}')
                logger.info(f" user searched {search_item} in grocery list.")  #noqa:E501
            else:
                print('item is not into the list')

    @staticmethod
    def search_vegetable(search_item:str) -> str:
        """ method to search item in vegetable list. 
        Parameters
        ----------
        variable1 : 
            search_item is specific item which user want search it"""
        with open('database/vegetable-items.json')as files:
                data = json.load(files)
                if search_item in data:
                    print(f'item you searched is : {search_item}')
                    logger.info(f" user searched {search_item} in grocery list.")  #noqa:E501
                else:
                    print('item is not into the list')




