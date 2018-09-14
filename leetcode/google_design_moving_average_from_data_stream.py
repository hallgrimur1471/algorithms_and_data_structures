from collections import deque

class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.window = deque()
        self.moving_average = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.window.append(val)
        if len(self.window) > self.size:
            removed = self.window.popleft()
            self.moving_average -= removed / self.size
            self.moving_average += val / self.size
        else:
            self.moving_average *= len(self.window) - 1
            self.moving_average += val
            self.moving_average /= len(self.window)
        return self.moving_average

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

