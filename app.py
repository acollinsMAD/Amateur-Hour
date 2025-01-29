#defines t1 from input
t1 = input("Enter a time as a whole number: ")

#converts t1 to integer
t1 = int(t1)


#checks if t1 is a proper time
def t1Check(t1):
    if (t1 > 12) or (t1 < 1):
        print("Invalid time, try again")
        exit()
    else:
        return True

t1Check(t1)

#defines t2 from input
t2 = input("Enter another time as a whole number: ")

#converts t2 to integer
t2 = int(t2)

#checks if t2 is a proper time
def t2Check(t2):
    if (t2 > 12) or (t2 < 1):
        print("Invalid time, try again")
        exit()
    else:
        return True

t2Check(t2)

#converts t1 and t2 to integers
if t1Check(t1) == True:
    time1 = int(t1)
    
if t2Check(t2) == True:
    time2 = int(t2)

        
#checks if t1 is less than t2
def time_passed(time1, time2):
    if time1 < time2:
        return time2 - time1
    #checks if t1 is greater than t2
    elif time1 > time2:
        return time2 - (24 - time1) + 12
    #checks if t1 is equal to t2
    else:
        print("No time passed")
        
print(time_passed(time1, time2))
