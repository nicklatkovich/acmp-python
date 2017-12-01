l=[1,0,0]
def s(a,b):l[a],l[b]=l[b],l[a]
for i in list(map(lambda x:list('ABC').index(x),list(input()))):s(i,(i+1)%3)
print(l.index(1)+1)