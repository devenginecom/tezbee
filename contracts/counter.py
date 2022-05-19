import smartpy as sp

class Counter(sp.Contract):
    def __init__(self):
        self.init(
            counter = sp.int(0)
        )
    
    @sp.entry_point
    def increment(self):
        self.data.counter += 1
    
    @sp.entry_point
    def decrement(self):
        self.data.counter -= 1

    