import math

def circles_intersects(x1, y1, r1, x2, y2, r2):
    min_radius = min(r1, r2)
    max_radius = max(r1, r2)
    sum_of_radius = r1 + r2
    radius_difference = max_radius - min_radius
    distance = math.sqrt((x1 - x2) **2 + (y1 - y2) **2)
    if distance == sum_of_radius or distance == radius_difference or (distance < sum_of_radius and distance > radius_difference):
        return True
    if distance > sum_of_radius or distance < radius_difference:
        return False


print(circles_intersects(2, 2, 3, 2, 1, 4))