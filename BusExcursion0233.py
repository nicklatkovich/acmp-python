input()
l=list(map(int,input().split()))
for i,h in enumerate(l):
	if 437>=h:
		print('Crash '+str(i+1))
		raise SystemExit()
print('No crash')