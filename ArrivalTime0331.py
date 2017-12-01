def f(s):return sum([x*y for x,y in zip(list(map(int,input().split(s))),[60,1])])
r=sum([f(':'),f(' ')])
print('{0:02d}:{1:02d}'.format(int(r/60)%24,r%60))