[n,t,k]=[int(input()),[],[]]
for i in range(3):k.insert(0,60**i)
for i in range(n):
	a=input()
	t.append([a,sum([x*y for x,y in zip(list(map(int,a.split())),k)])])
for i in sorted(t,key=lambda x:x[1]):
	print(i[0])