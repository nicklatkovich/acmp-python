n='VCG'
k=int(input())%3
print((n[k:]+n[:k])[::-1])