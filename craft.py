
def clrs(): # Since there's no clear screen function in Python, or on Pycharm, this will make my program more readable
    for i in range(20):
        print(" ") # By creating empty space, lots of them
def spaceup(): # For the look, this to seperate the lines, so the text would be in the middle
    for i in range(5):
        print(" ")
def send_to_admin(from_user_email,the_email,validity, tail_found): # I use external file to store the list of email source
    admin = open('output.txt','a+') # To write the result in output.txt
    admin.writelines(f"User with email: '{from_user_email}' report '{the_email}' as '{validity} email'\n") # Write into the output file With user name, reported email.
    admin.writelines(f"Email source found: {tail_found}\n")
    admin.close()

def adding_database(sus_email,section): # A function to add the corresponding type of email to the right .txt file.
    if section == "sus": # Mark it if it is suspicious
        send_to = open('Phising email.txt', 'a+')
    elif section == "add": # Mark it if it is valid
        send_to = open('Common right email.txt', 'a+')
    send_to.writelines(f'{sus_email}\n') # If it's suspicious, send to Phising email.txt
                                        # Else, send to common, valid email
    send_to.close()

def report(this_email,tails): # A function to process upon receive new email
    print(f'{this_email} does not match any result in Database') # Just to makesure if the sender
                                                                    # isn't suspicious as well
    print('Before sending report, please provide your email address: ')
    user_email = input('Type nothing if you prefer not to share ') # Take the email input
    if user_email == " ":
        user_email = 'Anonymous'
    print('What should this email be?')
    print("Type 'v' if you sure this is a valid email, 's' if this is suspicious")
    command = input("Please enter ")
    command = command.lower() # To make sure even when caplocks on
    spaceup()
    while (command != 'v') and (command != 's'): # Loop if user didn't give the correct command
        clrs() # Repeat codes above
        print(f'{this_email} does not match any result in Database')
        print('What should this email be?')
        print("Type 'v' if you sure this is a valid email, 's' if this is suspicious ")
        command = input("Please enter ")
        command = command.lower()
        spaceup()
    if command == 'v': # If valid email
        adding_database(this_email,'add') # Add email to valid email list
        adding_database(tails,'add') # Add email source to valid email list
        send_to_admin(user_email,this_email,'Valid',tails) # Report to data base
    else:
        adding_database(this_email,'sus') # Add email to suspicious email list
        adding_database(tails,'sus') # Add email source to suspicious email list
        send_to_admin(user_email, this_email, 'Suspicious',tails) # Report to data base

def thank_you_text():
    print('Thank you for using my system')
    command = input('Got another email? y/n ') # A loop ready to re run the process
    command = command.lower() # Making sure no capslock problems
    spaceup()
    while (command != 'y') and (command != 'n'): # Loop if user doesn't give proper command
        print("Type 'y' for Yes and 'n' for No ")
        command = input('Got another email? y/n ')
        command = command.lower()
        spaceup()
    if command == 'y':
        return True
    else: # Regardless if it isn't yes, then re run the program
        print("Good bye ( 'w')/ ")
        exit(0)

def check_per_line(email,mark):
    if '@' in email:  # if it is legitmate an email
        email_tails = email.index('@')  # if it contains '@' in email, take the index of '@' to process later
    else:
        print('Is this an email even? ')  # If not, terminate and force quit
        exit(0)
    with open(mark) as f:
        data = f.readlines()
    for line in data:
        if email in line:
            return True
    return False

def checkmap(email):
    if '@' in email: # if it is legitmate an email
        email_tails = email.index('@') # if it contains '@' in email, take the index of '@' to process later
    else:
        print('Is this an email even? ') # If not, terminate and force quit
        exit(0)
    if check_per_line(email[email_tails::],'Common right email.txt'):
        print('Yes, Valid email')
    elif check_per_line(email[email_tails::],'Phising email.txt'):
        print('Suspicious email detected. Do not give your credential or click anything from this email')  # print response
    else:
        report(email,email[email_tails::])
    return

def main_program(): # So it's callable if user want to add more email
    start = input("What's the email? ") # Get the email from input
    checkmap(start) # Check if valid email
    if thank_you_text(): # Check if user wants to try again
        main_program() # Try again

print('Yo, welcome to my email checking database')
print("I know this just an assignment for CPS109 and I'm a first year student")
print("But who knows if I'll make this viral or start my own server after studying about web design")
main_program()
