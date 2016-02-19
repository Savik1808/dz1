# coding UTF-8
import os
names=os.listdir('.') 
print(names)
summa=0
file=open('result.txt','w')
for name in names:
    f=open(name)
    s=f.read()
    if (s.count('Python'))>0:
        print(name)
        n=s.count('Python')
        summa=summa+n
        print(n)
        file.write(name+'\t'+str(n)+'\n')
    else:
        file.write(name+'\t'+str(0)+'\n')
    f.close()
print(summa) 
file.close()
