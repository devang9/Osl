import time
import datetime
today=datetime.datetime.today().strftime('%Y-%m-%d')
mins =5
lastline=''
with open('testfile.txt', "r") as f1:
    last_line = f1.readlines()[-1]
f1.close()
if last_line[0:10]==today:
    f2 = open('testfile.txt','r')
    lines = f2.readlines() 
    f2.close()
    del lines[-1] 
    f2 = open('testfile.txt','w')
    f2.writelines(lines) 
    f2.close()
    mins = mins+int(last_line[11:])
else:
    f = open('testfile.txt','a')
    toprint='\n'
    f.write(toprint)
    f.close()
f = open('testfile.txt','a')
toprint='%s %s'%(today,mins)
f.write(toprint)
f.close()