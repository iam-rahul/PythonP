from spy_details import spy_friend
from steganography.steganography import Steganography
from datetime import datetime
import time

print "Hello!!!"
print "Welcome to the SpyWorld"
print "Let's Start"

status_msg = ["i am back","i shouldn't be alive","i am on mission","tiger zinda hai"]                             #list
friends_spy = [{'name':'bond','age':28,'rating':5.8,'is_online':True,'chats':[]},{'name':'ghost','age':30,'rating':6.2,'is_online':True,'chats':[]},{'name':'soap','age':42,'rating':7.6,'is_online':True,'chats':[]}]                                                                                            #empty list

def add_status(current_status):                                                    #function definition of add_status()
    if current_status != None:
        print "Your Current Status is %s" %(current_status)
    else:
        print "You don't have any Status, yet"

    old_status = raw_input("Do You Want to Select from Old Status (Y or N)? ")
    if len(old_status)>=1:
        if old_status.upper() == "Y":
            serial_no = 1
            for status in status_msg:                                                                         #for loop
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
                status_msg.append(new_status)                                                          #append() method
            else:
                print "Invalid Input"
        else:
            print "Invalid Choice"
    else:
        return_status = "No Status"
        return return_status                                                                                    #return

def add_friend():                                                                    #function definition of add_friend
    new_friend = {
        'name':'',
        'salutation':'',
        'age':0,
        'rating':0.0,
        'chats':[]
    }                                                                                                       #dictionary
    valid_name = True
    valid_salutation = True
    while valid_name:
        new_friend['name'] = raw_input("Enter the Name of Your Friend ")
        if len(new_friend['name'])>0:
            while valid_salutation:
                new_friend['salutation'] = raw_input("What should We call Your Friend (Mr or Miss)? ")
                if len(new_friend['salutation'])>0:
                    new_friend['name'] = new_friend['salutation'] + " " + new_friend['name']
                    valid_salutation = False
                    valid_name = False
                else:
                    print "Invalid Salutation"
        else:
            print "Invalid Name"
    valid_age = True
    while valid_age:
        new_friend['age'] = raw_input("Enter the Age of Your Friend ")
        if len(new_friend['age'])>0:
            valid_age = False
        else:
            print "Invalid Age"
    valid_rating = True
    while valid_rating:
        new_friend['rating'] = raw_input("Enter the Rating of Your Friend ")
        if len(new_friend['rating'])>0:
            valid_rating = False
        else:
            print "Invalid Rating"
    if len(new_friend['name'])>0 and 45<=int(new_friend['age'])>=15 and float(new_friend['rating'])>=spy['rating']:
        friends_spy.append(new_friend)
    else:
        print "Your Friend can't be Added"
    return len(friends_spy)

def select_friend():                                                              #function definition of select_friend
    serial_no = 1
    for frnd in friends_spy:
        print str(serial_no) + " " + frnd['name']
        serial_no = serial_no + 1
    user_select = input("Select Your Friend ")
    user_index = user_select - 1
    return  user_index

def send_message():
    user_frnd_index = select_friend()
    original_image = raw_input("What is the name of Your Image? ")
    text = raw_input("What is Your Secret Message? ")
    output_path = 'output.png'
    Steganography.encode(original_image,output_path,text)
    new_chat = {
        "message" : text,
        "time" : datetime.now(),
        "sent_by_me" : True
    }
    friends_spy[user_frnd_index]['chats'].append(new_chat)
    print "Your Secret Message is Ready!!!"

def read_message():
    sender = select_friend()
    output_path = raw_input("What is the Name of File? ")
    secret_text = Steganography.decode(output_path)
    new_chat = {
        "message": secret_text,
        "time": time.strftime("%b %d %Y %H : %M : %S"),
        "sent_by_me": False
    }
    friends_spy[sender]['chats'].append(new_chat)
    print "Your Secret Message is " + secret_text

def spy_start(spy_name,spy_age,spy_rating):                                           #function definition of spy_start
    current_status = None
    menu_choice = True
    while menu_choice:                                                                                      #while loop
        spy_choice = input("""\nSelect a Choice from Menu:
1. Update Status
2. Add New Friend
3. Send Message
4. Read Message
0. Exit\n""")
        if spy_choice == 1:
            current_status = add_status(current_status)                                     #function call add_status()
            if len(current_status)>=1:
                if current_status == "No Status":
                    print "Invalid Status"
                else:
                    print "Your Status has been Set to \"%s\"" %(current_status)
            else:
                print "Invalid Status"
        elif spy_choice == 2:
            no_of_frnds = add_friend()                                                      #function call add_friend()
            print "You have \"%d\" Number of Friends" %(no_of_frnds)
        elif spy_choice == 3:
            send_message()                                                                #function call send_message()
        elif spy_choice == 4:
            read_message()
        elif spy_choice == 0:
            print "You are out from Menu"
            menu_choice = False
        else:
            print "Wrong Choice"

valid_exist = True
while valid_exist:
    spy_exist = raw_input("Are You an Existing Spy (Y or N)? ")
    if spy_exist.upper() == "Y":
        print "We Already have Your Details"
        spy_start(spy_friend['name'],spy_friend['age'],spy_friend['rating'])                 #function call spy_start()
        valid_exist = False
    elif spy_exist.upper() == "N":
        spy = {
            'name': '',
            'salutation': '',
            'age': 0,
            'rating': 0.0,
        }                                                                                                   #dictionary
        spy['name'] = raw_input("What is Your Spy Name? ")
        if len(spy['name'])>0:
            print "Welcome " + spy['name'] + ", Nice to have You Onboard"
            spy['salutation'] = raw_input("What should I call You (Mr or Miss)? ")
            spy['name'] = spy['salutation'] + " " + spy['name']
            print "Hi " + spy['name'] + ", Let's Know Something More About You..."
            spy['age'] = input("What is Your Age? ")
            if spy['age']>=15 and spy['age']<=45:
                print "Your are Eligible to be A Spy"
                spy['rating'] = input("What is Your Spy Rating? ")
                if spy['rating']>=6.0:
                    print "Great Spy"
                elif spy['rating']>=4.5 and spy['rating']<6.0:
                    print "Good Spy"
                elif spy['rating']>=3.5 and spy['rating']<4.5:
                    print "Average Spy"
                else:
                    print "Bad Spy"
                spy_online = True
                print "Authentication Complete!"
                print "Welcome %s, Your Age is %d and Spy Rating is %.1f" %(spy['name'],spy['age'],spy['rating'])
                spy_start(spy['name'],spy['age'],spy['rating'])                              #function call spy_start()
            else:
                print "You are not Eligible to be A Spy"
        else:
            print "Please Enter Your Spy Name"
        valid_exist = False
    else:
        print "Invalid Input"