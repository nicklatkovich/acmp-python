n=int(input())
print(('12'if n%400==0 or(n%4==0 and n%100!=0)else'13')+'/09/'+format(n,'04d'))