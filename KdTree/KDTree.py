import math


class KdTree:
    def __init__(self, points, dim=0):
        points.sort(key=lambda x: x[dim])
        m = len(points) // 2
        self.median = points[m]
        dim = (dim + 1) % 2
        if m > 0:
            self.left = KdTree(points[:m], dim)
        else:
            self.left = None
        if len(points) > m + 1:
            self.right = KdTree(points[m + 1:], dim)
        else:
            self.right = None


def search_nearest(tree, point):
    stack = []
    current = tree
    current_best = current
    while tree is not None:
        if current is not None:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            curr_res = distance(current.median, point)
            if curr_res < distance(current_best.median, point):
                current_best = current
            current = current.right
        else:
            break
    return current_best.median


def distance(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


points = [(1, 2), (2, 3), (5, 7), (10, 20), (5, 3), (2,5)]
tree = KdTree(points)
pt = (4,5)
print(search_nearest(tree, pt))
