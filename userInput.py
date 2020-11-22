# def keyInput(key):
#     scrollBinds = {'w': 'scrollUp', 'a': 'scrollLeft', 's': 'scrollDown',
#                    'd': 'scrollRight'}
#     if key in scrollBinds:
#         return scrollBinds[key]


class KeyBinds:
    def __init__(self, bindName):
        self.bindName = bindName
        self.allKeys = ['w', 'a', 's', 'd']
        self.scrollBinds = {'w': 'scrollUp', 'a': 'scrollLeft', 's': 'scrollDown',
                            'd': 'scrollRight'}


    def followKey(self, key):
        if key in self.scrollBinds:
            return self.scrollBinds[key]






taskBinds = KeyBinds(bindName='tasks')
