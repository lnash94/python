import re

Nameage ='''
Janice is 22 and Theon is 23
Gabriel is 44 and Joey is 21
'''
ages = re.findall(r'\d{1,3}',Nameage)
names = re.findall(r'[A-Z][a-z]*', Nameage)

ageDicts ={}

x = 0 

for eachname in names:
	
	ageDicts[eachname]= ages[x]
	x+=x

print(ageDicts)

allinform = re.findall(" info ","asinfo info asdfasfsfsfinfoadfaf")

for i in allinform:
	print(i)

for i in re.finditer("abc","abc sdfgewqwesdf saqwe bcs abc "):
	locationup = i.span()
	print(locationup)




str = "sat, hat , mata, pat"

allstr = re.findall("[Shmp]at", str)

for i in allstr:
	print(i)

