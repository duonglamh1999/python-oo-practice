"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self,startNum=0):
        self.startNum = self.next = startNum
    def __repr__(self):
        return f'startNum:{self.startNum},next:{self.next}'
    def generate(self):
        self.next+=1
        return self.next-1
    def reset(self):
        self.next = self.startNum
    