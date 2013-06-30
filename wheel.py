class Wheel:
    """Wheel Abstract Data Type"""
    def __init__(self, capacity):
        self.capacity = capacity
        self.datas = [None for x in range(0, capacity)]
        self.end = 0

    def addData(self, data):
        # add data to end of list
        if self.isFull():
            print "Wheel is full"
        else:
            self.datas[self.end] = data
            self.end += 1

    def getData(self):
        # get data in the middle of circle
        middle = (self.capacity - 1) / 2
        return self.datas[middle]

    def isFull(self):
        # are the circle is full?
        return self.end == self.capacity - 1

    def isEmpty(self):
        # are the circle is empty?
        return self.end == 0

    def rotateClockWise(self):
        # rotating clockwise
        self.capacity -= 2

    def rotateCounterClockWise(self):
        # rotating counter-clockwise
        self.capacity += 2
