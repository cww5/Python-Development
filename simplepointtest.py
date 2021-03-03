import simplepoint


def main():
    my_point_1 = simplepoint.SimplePoint(-100, 100)

    print("Point 1 coords: ({}, {})".format(my_point_1.x, my_point_1.y))
    my_point_1.move_to(1, 0)
    print("Point 1 new coords: ({}, {})".format(my_point_1.x, my_point_1.y))
    print("Point 1 distance to (0, 0) is: {}".format(my_point_1.get_distance_to(0, 0)))

    my_point_2 = simplepoint.SimplePoint(2.5, -5.6)
    print("Point 2 distance to Point 1 is: {}".format(my_point_2.get_distance_to(my_point_1.x, my_point_1.y)))


if __name__ == '__main__':
    main()
