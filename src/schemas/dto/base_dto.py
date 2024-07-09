class BaseDTO:
    
    def to_dict(self, by_alias: bool = False):
        dict = self.__dict__
        if by_alias:
            if hasattr(self, '__aliases__'):
                for field, alias in self.__aliases__.items():
                    dict[alias] = dict.pop(field)
        return dict