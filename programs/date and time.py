import time
localtime =  time.asctime(time.localtime()) 
print "Local current time :", localtime

localtime =  time.localtime()
print "Local current time :", localtime
print "time.altzone", time.altzone


import calendar

cal = calendar.month(2008, 1)
print "Here is the calendar:"
print cal

def procedure():
   time.sleep(2.5)

# measure process time
t0 = time.clock()
procedure()
print time.clock(), "seconds process time"

# measure wall time
t0 = time.time()
procedure()
print time.time() - t0, "seconds wall time"

print time.time()

print "time.ctime() : %s" % time.ctime()
print "time.gmtime() : %s" % time.gmtime()

#t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
t = time.gmtime()
t = time.mktime(t)
print time.strftime("%b %d %Y %H:%M:%S")


struct_time = time.strptime("30 Nov 00", "%d %b %y")
print "returned tuple: %s " % struct_time
