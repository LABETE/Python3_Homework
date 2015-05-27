"""
Class cetipede: using 'magic methods'
"""

class Centipede:
    def __init__(self):
        super().__setattr__('stomach', [])
        super().__setattr__('legs', [])
        
    def __call__(self, food):
        
        self.stomach.append(food)
    
    def __str__(self):
        return ",".join(self.stomach)
    
    def __setattr__(self, key, value):
        if hasattr(self, key):
            raise AttributeError("{0} is for internal use only".format(key))
        else:
            self.__dict__[key] = value
            self.legs.append(key)
    
    def __repr__(self):
        return ",".join(self.legs)
    
    
    