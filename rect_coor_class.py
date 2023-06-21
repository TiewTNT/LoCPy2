'''
Rectangular coordinates class, for LoC homework.
'''

from math import atan, pi


class RectCoor:
    '''
    Rectangular Coordinates Class
    '''

    def __init__(self, x, y):
        '''
        Initialization
        '''

        self.x = x
        self.y = y

    def pos(self):
        '''
        Returns the class's x and y.
        '''

        return self.x, self.y

    def is_on_any_axis(self):
        '''
        Returns True if the class's position is on any axis, else False.
        '''

        return 0 in [self.x, self.y]

    def quadrant(self):
        '''
        Returns the quadrant of the class's position.
        Returns None if the class's position is on the x-axis.
        '''

        if self.is_on_any_axis():
            return None
        elif self.x > 0 and self.y > 0:
            return 1
        elif self.x < 0 and self.y > 0:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        else:
            return 4

    def dist_x(self):
        '''
        Returns the distance between the class's position and the x-axis.
        '''

        return abs(self.y)

    def dist_y(self):
        '''
        Returns the distance between the class's position and the y-axis.
        '''

        return abs(self.x)

    def dist_origin(self):
        '''
        Return the distance between the origin and the class's position.
        '''

        return (self.x ** 2 + self.y ** 2) ** 0.5

    def middle_between(self, a, b):
        '''
        Returns the middle position between class's position and your specified position.
        '''

        return (a + self.x) / 2, (b + self.y) / 2

    def dist_to(self, a, b):
        '''
        Return the distance of the class's position to your sepecified position.
        '''

        return ((self.x - a) ** 2 + (self.y - b) ** 2) ** 0.5

    def angle_from_x_axis(self):
        '''
        Returns the angle from the x-axis.
        0 <= return value <= 90
        '''

        if self.x == 0:
            if self.y == 0:
                raise ValueError(
                    'Angle from x-axis could not be calculated, your point is the origin.')
            return 90
        return abs((atan(self.y / self.x) * (180 / pi))
                   - int((atan(self.y / self.x) * (180 / pi)) / 90))


if __name__ == '__main__':
    print(RectCoor(0, -5).angle_from_x_axis())
