# :pushpin:ShoppingList Document
	i'm using this md file
    to display flow of program
    and explain classes and methods.
    my database is Json file.
    

1) **class Product**
   1) Include def history() which display history of user when user buy, is user buy any thing , and the date time which user buy any thing.
   2) Include def buy() which calculate which category user want to buy and calculate amount of items and multiple it .
   3) Include def search() which display any items user want.
   4) Include def remove() which remove any item user want .
   5) Include def edit() which edit list with specific item user want .
   6) Include def discount() code which increase account balance of user.
   7) Include def add() which add any item user want into the list.
   8) Include def price() which display price and items in each category.
   9) Include def show() which display items into the each list.
2) **class Base User**
   1) Which initialize username and password by constructor and getter setter.
3) **class User**
    This class inheritance from BaseUSer
   1) Include def register() which register user and write into the json file.
   2) Include def login() which login user and write into the json file.
4) **class EnterUserName**
   1) Is a data class which help to display first name  and last name.
5) **class DateTimeEncoder**
   1) I override it in order to serialize datetime into the jsonfile
6) **class Help**
   1) This class is for help commands read commands from json file .
7) **class DiscountCodes**
   1) This class is a Enum class to keep discount code and return random of discount codes.
8) **class ExitCommands**
   1) This class is a Enum class to keep exit commands. 
>:pushpin: There is two logging file in this project .   
> 1. main.log
>        include logging of flow of program.
> 2. admin.log
>        include logging for register or login of user .