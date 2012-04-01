import re
fName=raw_input("Enter css path : ")
baseUrl=raw_input("Enter base url : ")
junk=open(fName,"r").read()
ans=re.findall("url\(.*\)",junk)
for i in ans:
	if i[4]=="\"":
		print baseUrl+i[5:-2]
		wget baseUrl+i[5:-2]
	else:
		print baseUrl+i[4:-1]
		wget baseUrl+i[4:-1]
