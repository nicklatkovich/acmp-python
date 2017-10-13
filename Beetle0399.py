
def init2DArray(height, width, default_value):
    result = []
    for y in range(height):
        result.append([])
        for x in range(width):
            result[y].append(default_value)
    return result

def hasWay(map: list, _from, to):
    usedCells = init2DArray(len(map), len(map[0]) if len(map) > 0 else 0, False)


arr = []r
with open('INPUT.TXT', 'r') as f:
    h, w = map(int, f.read().split())
    for y in range(h):
        row = f.read()
        arr.append([])
        for x in range(w):
            arr[y].append(True if row[x] == '@' else False)
x = 1
y = 1
with open('OUTPUT.TXT', 'w') as f:
