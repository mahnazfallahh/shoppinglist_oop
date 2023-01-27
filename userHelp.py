class Help:
    """ class Help which include help methods for user
    """

    @staticmethod
    def display_help():
        """ method to read from json file and display to user.
        """
        with open('database\help.txt') as files:
            data = files.read()
            print(data)
    @staticmethod
    def clear_screen():
        """ func to clear screen"""
        # Clear the terminal screen
        return os.system('cls')
