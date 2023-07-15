class student:
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
#std1.apply_raise()
#print(std1.marks)
print(std1.apply_raise())
