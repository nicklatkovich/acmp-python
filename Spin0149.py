arr = []

with open('INPUT.TXT', 'r') as f:
    N = int(f.readline())
    for num in f.read().split():
        arr.append(num)
arr.reverse()
with open('OUTPUT.TXT', 'w') as f:
    f.write(' '.join(arr))
