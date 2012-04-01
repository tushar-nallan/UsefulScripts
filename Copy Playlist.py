import os
fileName=input("Enter File Name")
fp=open(fileName,'r')
line=fp.readline()
line=line[:-1]
while(line):
	if(line[0]!='#') :
		print "copy \""+line+"\" C:\Users\Tushar\Desktop\Custom"
		os.system("copy \""+line+"\" C:\Users\Tushar\Desktop\Custom");
	line=fp.readline()
	line=line[:-1]
