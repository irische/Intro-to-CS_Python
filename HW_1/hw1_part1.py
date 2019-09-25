minutes=int(raw_input("Minutes ==> "))
print minutes
seconds=int(raw_input("Seconds ==> "))
print seconds
miles=float(raw_input("Miles ==> "))
print miles
time=float(minutes*60+seconds)
pace=time/miles
pace_minute=int(pace)/60
pace_second=pace-pace_minute*60
print "\nPace is %d:%04.1f"%(pace_minute,pace_second)
speed=miles/(time/3600)
print "Speed is %.2f miles per hour"%speed
