#fibonoccis series

n = input("print enter n: ")
a = 0
b = 1
print a,
for i in range(0,n):
    c = a + b
    b = a
    a = c
    print a,
    #i = i + 1
    
