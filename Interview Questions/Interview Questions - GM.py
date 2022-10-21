import math
def first_solution():
    points = "(-12,3) (56,2)"
    points = points.split('(')
    points = ''.join(points)
    points = points.split(')')
    points = ''.join(points)
    points = points.split(',')
    points[1] = points[1].split(' ')
    points[0] = int(points[0])
    points[1][0] = int(points[1][0])
    points[1][1] = int(points[1][1])
    points[2] = int(points[2])

    distance = math.sqrt(((points[1][1] - points[0]) ** 2) + ((points[2] - points[1][0]) ** 2))

    # points = points.split(',')


    print(points)
    print(round(distance))


def cleaner_solution():
    points = "(-12,3) (56,2)"
    points = points.replace('(','')
    points = points.replace(')', '')
    points = points.replace(',', ' ')
    points = points.split()
    points = [int(i) for i in points]
    distance = round(math.sqrt((points[2]-points[0])**2) + (points[3]-points[1])**2)

    print(points)
    print(distance)


first_solution()
cleaner_solution()
