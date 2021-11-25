class clear:
    def __init__(self):
        self.clear = "\033[H\033[J"
    def __call__(self):
        print(self.clear, end="")
        
"""
clear()()
print(clear().clear, end="")
"""
