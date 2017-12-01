with open('INPUT.TXT', 'r') as f:
    r1, r2, r3 = map(int, f.read().split())
with open('OUTPUT.TXT', 'w') as f:
    f.write('NO' if r1 < r2 + r3 else 'YES')
