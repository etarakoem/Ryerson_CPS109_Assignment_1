# Problem: Phising and suspicious email checking
# So apparently it's International Cyber security Awareness Month.
# To help minimize your risk of falling for common cyber attacks like phishing and fake email,
# I made a program to check whether an email is suspicious,
# or if not, adding to the list of valid (trusted) email or Suspicious email, and all send to my own admin page to check
# whether the report is legitimate.
# Since phishing email is getting more complex over time, it needs more work to determine one
# But so far, everything would be sent to the output.txt
# ----------------------------------------------------------------------------------------------------------------------
# Note: this program require 2 blanks .txt file:
# - Common right email.txt
# - Phising email.txt
# in the same directory to store Phising and Valid email list.
# As updating and writing new data into these list is part of the program, it would work regardless the list is empty.

# Program

# Since there's no clear screen function in Python, or on Pycharm, this will make my program more readable
def clrs():
    # By creating empty space, lots of them
    for i in range(20):
        print(" ")

# For the look, this to seperate the lines, so the text would be in the middle
def spaceup():
    for i in range(5):
        print(" ")

# I use external file to store the list of email source to write the result in output.txt
def send_to_admin(from_user_email,the_email,validity,tail_found):
    # Open the .txt file, 'a+' as append and read, to add more to my Database
    admin = open('output.txt','a+')

    # Make some space for latter input
    admin.writelines(" \n")

    # Write into the output file With user name, reported email.
    admin.writelines(f"User with email: '{from_user_email}' report '{the_email}' as '{validity} email'\n")

    # Report the source as well
    admin.writelines(f"Email source found: {tail_found}\n")


    admin.close()

# A function to add the corresponding type of email to the right .txt file.
def adding_database(sus_email,section):
    # Mark it if it is suspicious
    if section == "sus":
        # If it's suspicious, send to Phising email list
        send_to = open('Phising email.txt', 'a+')

    # Mark it if it is valid
    elif section == "add":
        # Else, send to Valid email list
        send_to = open('Common right email.txt', 'a+')

    # Ensure to send the email source regardless sus or not
    send_to.writelines(f'{sus_email}\n')
    send_to.close()

# A function to process upon receive new email that does not in Database
def report(this_email,tails):
    # Report the email
    print(f'{this_email} does not match any result in Database')

    # Just to makesure if the sender isn't suspicious as well, I'll take the sender's email
    print('Before sending report, please provide your email address: ')

    # But I'm kinda lazy for this one, also if people prefer privacy as keeping their email, they can skip
    user_email = input('Type nothing if you prefer not to share ')
    # And the empty email will be sent to output as "Anonymous"
    if user_email == " ":
        user_email = 'Anonymous'

    # Ask for this reported email's type, Suspicious or Valid
    print('What should this email be?')

    # Taking command to proceed
    print("Type 'v' if you sure this is a valid email, 's' if this is suspicious")
    command = input("Please enter ")
    # To ensure the input even when caplocks on
    command = command.lower()
    spaceup() # Make some space to galre at the look

    # Loop if user didn't give the correct command
    while (command != 'v') and (command != 's'):
        # Repeat codes above
        clrs()
        print(f'{this_email} does not match any result in Database')
        print('What should this email be?')
        print("Type 'v' if you sure this is a valid email, 's' if this is suspicious ")
        command = input("Please enter ")
        command = command.lower()
        spaceup()

    # If valid email
    if command == 'v':
        # Add email to valid email list
        adding_database(this_email,'add')

        # Add email source to valid email list, since mostly fraud email are from fraud sources
        adding_database(tails,'add')

        # Report to data base
        send_to_admin(user_email,this_email,'Valid',tails)

    # If sus email:
    else:
        # Add email to suspicious email list
        adding_database(this_email,'sus')

        # Add email source to suspicious email list
        adding_database(tails,'sus')

        # Report to data base
        send_to_admin(user_email, this_email, 'Suspicious',tails)

# This function will make a loop process if User wants to report another email in one run
# It's for TA to check multiple time without re run my program. You're welcome
def thank_you_text():
    # Loop procedure. I'm basically adding lines of comments here.
    print('Thank you for using my system')
    command = input('Got another email? y/n ')

    # Making sure no caplocks problems
    command = command.lower()
    spaceup()

    # Loop in case user doesn't give proper command.
    while (command != 'y') and (command != 'n'):
        # Repeat the code above
        print("Type 'y' for Yes and 'n' for No ")
        command = input('Got another email? y/n ')
        command = command.lower()
        spaceup()

    # Return True, if statement, and re run the whole program
    if command == 'y':
        return True

    # Regardless if it isn't yes, then end the program
    else:
        print("Good bye ( 'w')/ ")
        exit(0)

# This function will check each line of the email
def check_per_line(email,mark):
    # Check if it is legitmate an email, with '@'. If not, terminate and force quit
    if '@' not in email:
        print('Is this an email even? ')
        exit(0)

    # Quick open the file and read each of the line
    with open(mark) as f:
        data = f.readlines()

    # Check if email is in data base
    for line in data:
        if email in line:
            return True

    # Return False and end the program if not.
    return False

# This part would response whether the input is a legitimate email,
# or a Valid email, or a suspicious email that matches my database
def checkmap(email):
    # If this is a legitmate email
    if '@' in email:
        # If it contains '@' in email, take the index of '@' to process with the email source
        email_tails = email.index('@')

    # If not, terminate and force quit
    else:
        print('Is this an email even? ')
        exit(0)
    # Check the email status whether it is Valid or Suspicious. Report if not in database
    if check_per_line(email[email_tails::],'Common right email.txt'):
        print('Yes, Valid email')
    elif check_per_line(email[email_tails::],'Phising email.txt'):
        print('Suspicious email detected. Do not give your credential or click anything from this email')

    # If not in Database
    else:
        report(email,email[email_tails::])
    return

# Parts of main program, re-callable if user desire.
def main_program():
    # Get the email from input
    start = input("What's the email? ")

    # Check if valid email
    checkmap(start)

    # Check if user wants to try again
    if thank_you_text():
        # Re-call the program
        main_program()

# My greetings
print('Yo, welcome to my email checking database')
print("I know this just an assignment for CPS109 and I'm a first year student")
print("But who knows if I'll make this viral or start my own server after studying about web design")
main_program()
