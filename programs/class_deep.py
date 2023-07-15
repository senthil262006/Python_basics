class employee:
    direct = 0
    ndirect = 1
    def __init__(self, Firstname, Secoundname, employeeid):
        self.first = Firstname #data member
        self.secound = Secoundname
        self.id = employeeid
        
    def email(self): #methood
        return self.first + '.' + self.secound + '@univ.com'
        #self.email =  self.first + '.' + self.secound + '@univ.com'
        #return self.email



class manager(employee): # inheritance
    def __init__(self, Firstname, Secoundname, employeeid, Managerid):
        super().__init__(Firstname, Secoundname, employeeid)
        #employee.__init__(self, Firstname, Secoundname, employeeid) ## inheriting base clase init constructor
        self.mid  = Managerid
        
##main###        
emp1 = employee('Senthil', 'S', 100) # object for base
emp2 = employee('Vengadesh', 'S', 200)        

mg1 = manager('shanmugavelu', 'v', 1000, 1) #object for child
mg2 = manager('prema', 'v', 1000, 2)

print (emp1.first, emp1.secound, emp1.__class__.ndirect)#accessing data member
print (emp1.email()) #accessing member function
print (mg1.first, mg1.secound, mg1.__class__.direct)
print (mg2.email())


class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance
d = Dog('Fido')
e = Dog('Buddy')
print (d.kind, e.name)

        
