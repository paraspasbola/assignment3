#Assignment 3

#You all are pilots, you have to land a plane, the altitude required for 
#landing a plane is 1000ft,
#if it is less than that tell pilot to land the plane,or 
#it is more than but less than 5000ft ask the pilot to "come down to 1000ft"
#,else if it is more than 5000ft ask the pilot to "go around and try later".


print("hello...Welcome to Airway\n")

print("Hello pilot,please give the flight details.")     
ch=int(input("What is the current height of the flight in air:")) 
#ch current height
height=1000
print("the Present height of the flight is "+str(ch)+".Pilot,we request you to")
if(ch<=height):
    print("safe to land .")
elif (ch>height and ch<5000):
     print("Bring down to 1000ft.")          #Example:Input-1000
else:
    print("Turn around and try later.")

print("Thank you...")                         #        Output:Safe to land
                                             #        Input-4500
                                             #        Output-bring down to 1000
                                             #        Input -6500
                                             #        Ouput-turn around
