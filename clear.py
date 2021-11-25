class clear:
    def __init__(self):
        self.clear = "\033[H\033[J"
    def __call__(self):
        print(self.clear, end="")


clear = clear()

"""
clear() # calls the `__call__()` function of the `clear` class -> clears the screen
clear.clear # returns the `clear` variable of the `clear` class
"""
