"""

"""
class alphabator:
    def __init__(self, lst):
        self.lst = lst
        self.itemno = 0
        self.count = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.count > self.itemno:
            try:
                self.val = self.lst[self.itemno]
                if isinstance(self.val, int) and 0 < self.val < 27:
                    self.val = chr(self.val + 64)
            except IndexError:
                raise StopIteration
            self.itemno += 1
        self.count += 1
        return self.val