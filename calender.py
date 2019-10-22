import calendar

cal = calendar.month(2008, 1)
print "Here is the calendar:"
print cal
print "2016 is aleap year:", calendar.isleap(2016)
print "no of leapdays between 1947 to 2016:", calendar.leapdays(1947,2016)
calendar.setfirstweekday(6)
print calendar.month(2008, 1)
print "weekday for 2016,12,3"
print calendar.weekday(2016,12,3)
