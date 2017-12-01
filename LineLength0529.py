import math
[a,b,c,d]=map(int,input().split())
print(format(math.sqrt((a-c)**2+(b-d)**2),'0.5f').rstrip('0').rstrip('.'))