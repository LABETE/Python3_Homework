"""
Create an inventory of X thing
"""

class Inventory:
    
    total = 0 
    
    def add(self, number):
        "Add X number of things"
        if isinstance(number, str):
            raise AttributeError("Strings are not accepted, the input should be int")
        else:
            self.total += number
            
    def total_weight(self):
        return self.total * self.weight
    
        
        