#Title: Coordinates
#Author: Dominic Corneliusen
#Date last modified: 3/6/2026

#Start
import math
def distance(cord1, cord2):
    x1 = cord1[0]
    y1 = cord1[1]
    z1 = cord1[2]
    x2 = cord2[0]
    y2 = cord2[1]
    z2 = cord2[2]
    distance_between = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    return distance_between
def create_3d_point():
    x = input("Enter the x-coordinate: ")
    while not check_point_data(x):
        x = input("Enter the x-coordinate: ")
    x = float(x)
    y = input("Enter the y-coordinate: ")
    while not check_point_data(y):
        y = input("Enter the y-coordinate: ")
    y = float(y)
    z = input("Enter the z-coordinate: ")
    while not check_point_data(z):
        z = input("Enter the z-coordinate: ")
    z = float(z)
    point = (x, y, z)
    return point
def check_point_data(dist):
    try:
        float(dist)
        return True
    except ValueError:
        print("Value is not a number. Please enter a number.")
        return False
print('The first x, y, and z coordinate.')
coordinate1 = create_3d_point()
print('The second x, y, and z coordinate.')
coordinate2 = create_3d_point()
distance_between_users_points = distance(coordinate1, coordinate2)
print('The distance between these two points is ' + str(distance_between_users_points))