from spy_details import spy_name,spy_age,spy_rating

print "Hello!!!"
print "Welcome to the SpyWorld"
print "Let's Start"

status_msg = ["i am back","i shouldn't be alive","i am on mission","tiger zinda hai"]

def add_status(current):
    if current != None:
        print "Your Current Status is %s" %(current)
    else:
        print "You don't have any Status, yet"

    old_status = raw_input("Do You Want to Select from Old Status (Y or N)? ")
    if old_status.upper() == "Y":
        serial_no = 1
        for status in status_msg:
            print str(serial_no) + "." + " " + status
            serial_no = serial_no + 1
        user_select = input("Which Status You Want to Select ")
        if len(status_msg)>=user_select:
            new_status = status_msg[user_select - 1]
        else:
            print "Invalid Input"
    elif old_status.upper() == "N":
        new_status = raw_input("Enter Your New Status ")
        if len(new_status)>=3:
            status_msg.append(new_status)
        else:
            print "Invalid Input"
    else:
        print "Invalid Input"
    return new_status

def spy_start(spy_name,spy_age,spy_rating):
    current_status = None
    menu_choice = True
    while menu_choice:
        spy_choice = input("""\nSelect a Choice from Menu:
1. Update Status
0. Exit\n""")
        if spy_choice == 1:
            update_status = add_status(current_status)
            print "Your Status has been Set to \"%s\"" %(update_status)
        elif spy_choice == 0:
            print "You are out from Menu"
            menu_choice = False
        else:
            print "Wrong Choice"

spy_exist = raw_input("Are You an Existing Spy (Y or N)? ")
if spy_exist.upper() == "Y":
    print "We Already have Your Details"
    spy_start(spy_name,spy_age,spy_rating)

elif spy_exist.upper() == "N":
    spy_name = raw_input("What is Your Spy Name? ")
    if len(spy_name)>0:
        print "Welcome " + spy_name + ", Nice to have You Onboard"
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
            print "Welcome %s, Your Age is %d and Spy Rating is %.1f" %(spy_name,spy_age,spy_rating)
        else:
            print "You are not Eligible to be A Spy"
    else:
        print "Please Enter Your Spy Name"
else:
    print "Invalid Input"