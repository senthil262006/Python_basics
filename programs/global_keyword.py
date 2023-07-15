x = 10
def fun1():
    x = 20
    
    def fun2():
        #global x
        nonlocal x
        x = 25
        #return x
    
    print("x value before calling fun2:", x)
    print("calling fun2 now")
    fun2()
    print("x value after calling fun2:", x)
   # return x
fun1()
print("x in main:", x)

