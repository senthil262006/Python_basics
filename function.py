
def total(bill = 50):
    overall = bill + 0.1 * bill
    #print overall
    return(overall)

print "Value of total :", total(bill = 100)

a=total(150)
print a
a=total()
print a

sum = lambda arg1, arg2: arg1 + arg2;

# Now you can call sum as a function
print "Value of total : ", sum( 10, 20 )
print "Value of total : ", sum( 20, 20 )
