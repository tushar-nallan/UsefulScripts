import re
import os
os.system("mkdir FlashTemp")
os.chdir("FlashTemp")
n=input("Check the total No. of pages and enter that: ")
for i in xrange(1,n+1):
    os.system("wget http://www.flashmo.com/page/"+str(i))
os.chdir("..")
os.system("mkdir flashMos")
os.chdir("flashMos")
for i in xrange(1,n+1) :
	fp=open("../FlashTemp/"+str(i),'r')
	allData=fp.read()
	cnt=1
	ans=re.findall('\"/preview/.*?\"',allData)
	for i in ans :
		if(cnt%2==1) :
			os.system("wget http://www.flashmo.com/fm_zip_files_1127/"+i[10:-1]+".zip")
			print("http://www.flashmo.com/fm_zip_files_1127/"+i[10:-1]+".zip")
		cnt+=1
	fp.close()
os.chdir("..")
os.system("rm -rf FlashTemp")
