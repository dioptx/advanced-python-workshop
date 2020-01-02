class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    # Works differently in IPython(Jupyter)
    def __repr__(self):
        return 'Polynomial(*{!r})'.format(self.coeffs)

    # Notion of addition
    def __add__(self, other):
        return Polynomial(*((x + y) for x, y in zip(self.coeffs, other.coeffs)))



p1 = Polynomial(1, 2, 3) # x^2 + 2x + 3
p2 = Polynomial(3, 4, 5) # 3x^2 + 4x + 3

print(p1 + p2 + p2)

class Angle:
    def __init__(self, degrees):
        # Wrap it around so that the value is always
        # in the interval of 0 and 359.999...
        self.degrees = degrees % 360
    # Less-than
    def __lt__(self, other):
        return self.degrees < other.degrees
    # Less-than-or-equals
    def __le__(self, other):
        return self.degrees <= other.degrees
    # Greater-than
    def __gt__(self, other):
        return self.degrees > other.degrees
    # Greater-than-or-equals
    def __ge__(self, other):
        return self.degrees >= other.degrees
    # Equals
    def __eq__(self, other):
        return self.degrees == other.degrees
    
    


class my_object(object):
    
    def __init__(self):
        pass
    
    def __repr__(self):
        return f"representation of the object: {self.__class__}"
    
    def __str__(self):
        return f"string format of the object"
    
obj = my_object()

print(f"With repr you get {repr(obj)}")
print(f"With str you get {str(obj)}")

