#!/usr/bin/python
n = int(input("Enter the number of table   n: "))
o = int(input("Enter itretion of the table o: "))


for i in range(1,n+1):
    for j in range(1,o+1):
        k=i*j
        #print(1,2,3,4,sep='*')
        print (k, end='  ') # "end" key will work from python 3.5
        #print  k, "\t",
    print('\n')
   
