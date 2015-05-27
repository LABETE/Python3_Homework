'''
Furnishing class for save furnishings in each room
'''

class Furnishing:
    def __init__(self, room):
        self.room = room
        
class Sofa(Furnishing):
    def __init__(self, room):
        super().__init__(room)
    
class Bookshelf(Furnishing):
    def __init__(self, room):
        super().__init__(room)

class Bed(Furnishing): 
    def __init__(self, room):
        super().__init__(room)
    
class Table(Furnishing):
    def __init__(self, room):
        super().__init__(room)
        
def map_the_home(home):
    """
    Take a list of the furnishings classes and return a dict with a room mapped with the object class
    """
    furnishing_dict = {}
    for num, furnishing in enumerate(home):
        if furnishing_dict.get(home[num].room):
            furnishing_dict[home[num].room] = furnishing_dict.get(home[num].room) + [furnishing]    
        else:
            furnishing_dict[home[num].room] = [furnishing]
    return furnishing_dict

def counter(home):
    """
    Take a list of the furnishings classes and print the values added in each class
    """
    bed_count = 0
    sofa_count = 0
    table_count = 0
    bookshelf_count = 0
    for furnishing in home:
        if isinstance(furnishing, Bed):
            bed_count += 1
        elif isinstance(furnishing, Sofa):
            sofa_count += 1
        elif isinstance(furnishing, Table):
            table_count += 1
        elif isinstance(furnishing, Bookshelf):
            bookshelf_count += 1
    print('Beds: {0}\nBookshelves: {1}\nSofas: {2}\nTables: {3}'.format(
                                bed_count, bookshelf_count, sofa_count, table_count))
    
if __name__ == "__main__":
    home = []
    home.append(Bed('Bedroom'))
    home.append(Sofa('Living Room'))
    result = map_the_home(home)
    print(result)