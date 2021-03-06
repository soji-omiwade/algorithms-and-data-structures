'Demonstrate effective use of super()'

import collections
import logging

logging.basicConfig(level="INFO")

class LoggingDict(dict):
    # Simple example of extending a builtin class
    def __setitem__(self, key, value):
        logging.info("setting %r to %r" % (key, value))
        super().__setitem__(key, value)
    
class LoggingOD(LoggingDict, collections.OrderedDict):
    #Build new functionality by re-ordering the MRO
    pass
ld = LoggingDict([("red", 1), ("green", 2), ("blue", 3)])
print(ld)
ld["red"] = 10

ld = LoggingOD([("red", 40), ("green", 80), ("blue", 120)])
print(ld)
ld['red'] = 400
print('-' * 20)

# ------- Show the order that the methods are called --------

def show_call_order(cls, methname):
    'Utility to show the call chain'
    classes = [cls for cls in cls.__mro__ if methname in cls.__dict__]
    print(' ==> '.join('%s.%s' % (cls.__name__, methname) for cls in classes))

show_call_order(LoggingOD, "__setitem__")
#output: LoggingDict.__setitem__ ==> OrderedDict.__setitem__ ==> dict.__setitem__
show_call_order(LoggingOD, "__iter__") 
# output: OrderedDict.__iter__ ==> dict.__iter__
print("-" * 20)

# ------- Validate and document any call order requirements

position = LoggingOD.__mro__.index
assert (position(LoggingDict) < position(collections.OrderedDict) < 
    position(dict))
    
    
# -------- Getting the argument signatures to match --------------
class Shape:
    def __init__(self, *, shapename, **kwds):
        self.shapename = shapename
        super().__init__(**kwds)

class ColoredShape(Shape):
    def __init__(self, *, color, **kwds):
        self.color = color
        super().__init__(**kwds)
cs = ColoredShape(color='red', shapename='circle')

# -------- Making sure a root exists ----------
class Root:
    def draw(self):
        #the delegation chain stops here
        print("the delegation chain stops here")
        assert not hasattr(super(), "draw")
        
class Shape(Root):
    def __init__(self, *, shapename, **kwds):
        self.shapename = shapename
        super().__init__(**kwds)
    def draw(self):
        print("Drawing. setting shape to", self.shapename)
        super().draw()

class ColoredShape(Shape):
    def __init__(self, *, color, **kwds):
        self.color = color
        super().__init__(**kwds)
    def draw(self):
        print("Drawing. setting color to", self.color)
        super().draw()
cs = ColoredShape(color="b.lue", shapename='square').draw()
print('-' * 20)

# ------- Show how to incorporate a non-cooperative class --------

class Moveable:
    # non-cooperative class that doesn't use super()
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        print('Drawing at position:', self.x, self.y)
        
class MoveableAdapter(Root):
    def __init__(self, *, x, y, **kwds):
        self.moveable = Moveable(x, y)
        super().__init__(**kwds)
    def draw(self):
        self.moveable.draw()
        super().draw()
        
class MoveableColoredShape(ColoredShape, MoveableAdapter):
    pass
    
MoveableColoredShape(shapename='triangle', x=10, color='red', y=20).draw()

# ------- Complete Example ---------------

from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    'Counter that remembers the order elements are first encountered'
    
    def __repr__(self):
        # return '{0:s}{1:s}'.format(self.__class__.__name__, OrderedDict(self))
        return '%s(%r)' % (self.__class__.__name__, OrderedDict(self))
        
oc = OrderedCounter('abracadabra')
print(oc)