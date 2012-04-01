import re
import os
os.system("mkdir temp")
os.chdir("temp")
n=input("Check the total No. of pages and enter that: ")
for i in xrange(1,n+1):
    os.system("wget http://www.templatemo.com/page/"+str(i))
os.chdir("..")
os.system("mkdir templateMos")
os.chdir("templateMos")
for i in xrange(1,n+1) :
	fp=open("../temp/"+str(i),'r')
	allData=fp.read()
	cnt=1
	ans=re.findall('\"/preview/.*?\"',allData)
	for i in ans :
		if(cnt%2==1) :
			os.system("wget http://cdn.templatemo.com/tm_zip_1115/"+i[10:-1]+".zip")
			print("http://cdn.templatemo.com/tm_zip_1115/"+i[10:-1]+".zip")
		cnt+=1
	fp.close()
os.chdir("..")
os.system("rm -rf temp")
