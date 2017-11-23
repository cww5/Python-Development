"""
This file tests some of the functionalities of the Point class.
"""
import point
axes = point.Point(0,0,'black') #Used to draw the axes
axes.drawAxes(300,300)
center = point.Point(0,0,'blue') #The first point
print("Current coordinates of 'center'" + str(center.coordinates()) + "\n")
center.move(100,-50)
print("New coordinates of 'center'" + str(center.coordinates()) + "\n")
center.drawPolygon(40,7)
point1 = point.Point(1,1, 'red') #The second point
print("Distance from center to point1 is: " + str(center.distance_to(point1)) + "\n")
print("Total number of points: " + str(point.getCount()))
point1.move_to(-25,-100)
point1.drawPolygon(60,3)
print("New distance from center to point1 is: " + str(center.distance_to(point1)) + "\n")
