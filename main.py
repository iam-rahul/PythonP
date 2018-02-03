from spy_details import spy_name,spy_age,spy_rating

print "Hello!!!"
print "Welcome to the SpyWorld"
print "Let's Start"
spy_exist = raw_input("Are You an Existing Spy (Y or N)? ")
if spy_exist.upper() == "Y":
    print "We Already have Your Details"
    menu_choice = True
    while menu_choice:
        spy_choice = input("\nPlease Select from Menu\n 1. Update Status\n 0. Exit\n")
        if spy_choice == 1:
            spy_status = raw_input("Enter Status Here ")
            print "Your Status is \"%s\"" %(spy_status)
        elif spy_choice == 0:
            print "You are out from Menu"
            menu_choice = False
        else:
            print "Wrong Choice"
elif spy_exist.upper() == "N":
    spy_name = raw_input("What is Your Spy Name? ")
    if len(spy_name)>0:
        print "Welcome " + spy_name + " Nice to Meet You"
        spy_salutation = raw_input("What should I call You (Mr or Miss)? ")
        spy_name = spy_salutation + " " + spy_name
        print "Hi " + spy_name + ", Let's Know Something More About You..."
        spy_age = input("What is Your Age? ")
        if spy_age>15 and spy_age<45:
            print "Your are Eligible to be A Spy"
            spy_rating = input("What is Your Spy Rating? ")
            if spy_rating>=6.0:
                print "Great Spy"
            elif spy_rating>=4.5 and spy_rating<6.0:
                print "Good Spy"
            elif spy_rating>=3.5 and spy_rating<4.5:
                print "Average Spy"
            else:
                print "Bad Spy"
            spy_online = True
            print "Authentication Complete!"
            print "Welcome %s Your Age is %d and Spy Rating is %.1f" %(spy_name,spy_age,spy_rating)
        else:
            print "You are not Eligible to be A Spy"
    else:
        print "Please Enter Your Spy Name"
else:
    print "Invalid Input"