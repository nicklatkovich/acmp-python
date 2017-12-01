n=list(map(int,input().split()))
print(sum([x*y for x,y in zip(sorted(n[:3]),sorted(n[3:]))]))