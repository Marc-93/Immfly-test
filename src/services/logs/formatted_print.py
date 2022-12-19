class FormattedPrint(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def pink(self):
        """Prints key in default color and value with pink formatted color"""
        print(f'[{self.key}] \033[38;5;211m{self.value}\033[0;0m')

    def green(self):
        """Prints key in default color and value with green formatted color"""
        print(f'[{self.key}] \033[38;5;40m{self.value}\033[0;0m')

    def red(self):
        """Prints key in default color and value with red formatted color"""
        print(f'[{self.key}] \033[38;5;196m{self.value}\033[0;0m')
