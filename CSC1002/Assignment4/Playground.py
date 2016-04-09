class Bstr(str):
    def __init__(self, *args, **kwargs):
        if 'function' in kwargs:
            self.__func = kwargs['function']
            kwargs.pop('function')
        else:
            self.__func = False
        str.__init__(self)

    def get_func(self):
        return self.__func
a=Bstr('a')
print('hello')