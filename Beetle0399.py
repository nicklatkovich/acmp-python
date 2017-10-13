import queue


class Point:
    def __init__(self, _y, _x):
        self.y = _y
        self.x = _x

    def __add__(self, other):
        return Point(self.y + other.y, self.x + other.x)

    def __getitem__(self, item):
        return item[self.y][self.x]

    def __setitem__(self, key, value):
        key[self.y][self.x] = value

    def __eq__(self, other):
        if type(other) != Point:
            return False
        else:
            return self.y == other.y and self.x == other.x

    def __iadd__(self, other):
        return self + other


dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
dPoints = []
for _dy, _dx in zip(dy, dx):
    dPoints.append(Point(_dy, _dx))


def hasWay(_walls, _from, to):
    usedCells = init2DArray(len(_walls), len(_walls[0]) if len(_walls) > 0 else 0, False)
    q = queue.Queue()
    q.put(_from)
    while not to[usedCells] and not q.empty():
        cell = q.get()
        for dPoint in dPoints:
            nearCell = cell + dPoint
            if not nearCell[_walls] and not nearCell[usedCells]:
                nearCell[usedCells] = True
                q.put(nearCell)
    return to[usedCells]


def init2DArray(height, width, default_value=None):
    result = []
    for _y in range(height):
        result.append([])
        for _x in range(width):
            result[_y].append(default_value)
    return result


def beetle():
    with open('INPUT.TXT', 'r') as f:
        h, w = map(int, f.readline().split())
        _walls = init2DArray(h, w, False)
        for y in range(h):
            row = f.readline()
            for x in range(w):
                if row[x] == '@':
                    _walls[y][x] = True
    with open('OUTPUT.TXT', 'w') as f:
        prevDirection = None
        position = Point(1, 1)
        finishPosition = Point(h - 2, w - 2)
        if hasWay(_walls, position, finishPosition):
            obstruction = init2DArray(h, w, 0)
            result = 0
            while position != finishPosition:
                position[obstruction] += 1
                minStepWeight = float('inf')
                minStepWeightCount = -1
                minStepDirection = None
                for dPoint in dPoints:
                    nextPosition = position + dPoint
                    if nextPosition[_walls]:
                        continue
                    weight = nextPosition[obstruction]
                    if weight < minStepWeight:
                        minStepWeight = weight
                        minStepWeightCount = 0
                        minStepDirection = dPoint
                    if weight == minStepWeight:
                        minStepWeightCount += 1
                        if dPoint == prevDirection:
                            minStepDirection = dPoint
                prevDirection = minStepDirection
                position += minStepDirection
                result += 1
                # if result > 2000000:
                #     f.write('-1')
                #     return
            f.write(str(result))
        else:
            f.write('-1')


beetle()
