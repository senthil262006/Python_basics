class student:

    pers_rise = 1.5  
    
#std1 = student()
#std2 = student()
#std1.first = "Senthil"
#std1.last = "S"
#std1.email = "senthil.s@gmail.com"
#std1.marks = 90

#std2.first = "Venkadesh"
#std2.last = "S"
#std2.email = "vengadesh.s@gmail.com"
#std2.marks = 30


    def __init__(self, first, last, marks):
        self.first = first 
        self.last = last
        self.marks = marks
        self.email = first + '.' + last + "@gmail.com"
    
        
    def fulname(self):
        
       return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        
        self.marks = int(self.marks * 1.5)
        return self.marks
   
std1 = student('Senthil', 'S', 60)
std2 = student('Vengadesh', 'S', 100)



print(std1.email)
print(std2.email)
print ('{} {}'.format(std1.first, std1.last))
print(std2.fulname())
print(std1.marks)
std1.apply_raise()
print(std1.marks)
print(std1.apply_raise())
