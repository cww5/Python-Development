import math

class SimplePoint:
    '''This is a simple point implementation of a point in Euclidean space (2D).'''
    num_dimensions = 2

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def get_distance_to(self, x_val, y_val):
        return math.sqrt((x_val - self.x)**2 + (y_val - self.y)**2)

if __name__ == '__main__':
    my_point = SimplePoint(4, 2)
    print('Original Coordinates: ({}, {})'.format(my_point.x, my_point.y))
    my_point.move_to(3, 5)
    print('New Coordinate: ({}, {})'.format(my_point.x, my_point.y))
    print('distance to (0,0) is: {:.2f}'.format(my_point.get_distance_to(0, 0)))