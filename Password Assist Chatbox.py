#----------------------------------Resources----------------------------------------------
#Donald Winkelman 
import random

list_for_numbers= ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
list_for_symbols= ['"', "!", "'", '@', '#', '$', '%', '^', '&']
list_for_letters= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
list_for_passwordguessing = ['rat', 'tiger1', 'garbage444', 'education567#', 'abomination123456$$', 'concentration**%^&', 'mischievousness12345678901234567890', 'biomathematicians$$##@@%%^^&&**']

#------------------------------------List Code--------------------------------------------
#Donald Winkleman 
'''

Account_Database = {

  "Google Login" : "\n\n Username- replator9000 \n Password- Trains_r_neat1066\nExtra/Backup Authentication- sauce@gmail.com\nDescription- Used for personal coding of stuff and things",

  "Repl.it Login" : "\n\nUsername- replator9000\nPassword- Trains_r_neat1066\nExtra/Backup Authentication- sauce@gmail.com\nDescription- Used for personal coding of stuff and things",

  "Github Login" : "Google Login\n\nUsername- VictorCharlie72\nPassword- 3trees*speak \nExtra/Backup Authentication- 512-607-7777\nDescription- For all my google stuffs",

  "Netflix Login" : "Netflix Login\n\nUsername- seriousgamer_uwu_\nPassword- waxwaffles9*1 \nExtra/Backup Authentication- 512-607-7777\nDescription- $15 dollars a month? Wy?",

  "Microsoft Login" : "Microsoft Login\n\nUsername- supersized_chungusv1.01\nPassword- 2number9's\nExtra/Backup Authentication- None\nDescription- Windows, Office and that's about it really"





}


def list_start():
  print(Account_Database)
  listing = input('\n\n\nWelcome to the database! Above are a few starter enteries.\nFeel free to search for a specific entry via the dictionary.\nWhen ready to go back, type "back": ')
  if listing in Account_Database:
    print("Login: " + listing)

  else:
    print(main_runner())
  
 # Account_Database.search(listing)

  

#--------------------------------New Database Entry---------------------------------------


def entry_start():
  entry_number = 5

  entry_number = entry_number + 1
  newaccount = input('What are you making this account for?\n(ex. For a microsoft account, put "Microsoft)\n')
  newusername = input("What's the Username for this account?: ")
  newpassword = input("What's the password for this account?: ")
  newtwofactor = input('Do you have two factor or alternate verification?\n If so, enter your email or phone number. If not, type anything else: ')
  newdescription = input("Is there any other information about your account you want to add")

'''

#-----------------------------Password Strength Detector-----------------------------------
#Michel Azar, Donald Winkleman 

def passwordlength(strength):
  password = input("\nWelcome to the password generator! Please enter your password: ")
  if len(password) < (5*strength):
    passtwo = ("\nConsider lengthening your password:")
    something = input(passtwo)
    if len(something) > (10*strength) and len(something) < (40*strength):
      print("Your password is sufficiently long.")
      
    else:
      print("\nYour password is still too short!")
      
  elif len(password) > (40*strength):
    passthree = ("\nYour password is too long! Consider shortening it. ")
    somethingtwo = input(passthree)
    if len(somethingtwo) > (10*strength) and len(somethingtwo) < (40*strength):
      print("\nYour password is sufficiently long.\n")

  else: 
    print("\nYour password is sufficiently long.\n")



def password_tester():
  password_tester = input('\n\nHow strong do you want your password to be?\n\n1. Moderately Strong\n2. Strong\n3. Very Strong\n\nPlease enter the number corresponding to your preference: ')

  if password_tester == '1':
    passwordlength(1)

  if password_tester == '2':
    passwordlength(1.25)

  if password_tester == '3':
    passwordlength(1.5)


#-------------------------------Password Improvment---------------------------------------
#Michel Azar
def passwordvariation():
 password = input("\n\nWelcome to the password strengthener! Please enter your password: ")
 for letter in list_for_letters:
   if letter in password:
     print(input("\nConsider adding numbers and symbols to your password: "))
 for number in list_for_numbers:
    if number in password:
      print(input("\nConsider adding letters and symbols to your password: "))
 for symbol in list_for_symbols:
    if symbol in password:
      print(input("\nConsider adding letters and numbers to your password: "))
      

#----------------------------------Password Game------------------------------------------
#Praneit Goyal, Donald Winkleman 

def guesswordgame():
  guessesTaken = 0
  guess_intro = ("\n\nWelcome to the Guess My Password game!\nThis game shows you the power of having strong and hard-to-crack passwords.\nThere are 8 levels, 1 being the easiest to crack and 8 being the hardest.")
  print((guess_intro))
  passwordone = ("\nPlease choose the level of the game you want to play ")
  passwordlevel = input(passwordone)
  if passwordlevel == "1":
    word = list_for_passwordguessing[0]

  elif passwordlevel == "2":
    word = list_for_passwordguessing[1]
  elif passwordlevel == "3":
    word = list_for_passwordguessing[2]
  elif passwordlevel == "4":
    word = list_for_passwordguessing[3]
  elif passwordlevel == "5":
    word = list_for_passwordguessing[4]
  elif passwordlevel == "6":
    word = list_for_passwordguessing[5]
  elif passwordlevel == "7":
    word = list_for_passwordguessing[6]





    # we can use a choice function here and randomize the words from a list. 
  print('\nWell, I am thinking of a word')



  while guessesTaken < 6:

      guess=input('\nTake a guess: ') # There are four spaces in front of print.
      guess = str(guess)


      guessesTaken = guessesTaken + 1
      

      if len(guess) < len(word):

       print('\nTry Again! Your guess has fewer characters than the word.') # There are eight spaces in front  of print.


      if len(guess) > len(word):

        print('\nTry Again! Your guess has more characters than the word.')
      

      if len(guess) == len(word):
      
        print("\nYou've got the right word count, the first letter is ", str(list_for_passwordguessing[0][0]) )

      if guess == word:
        print("\n\nCongratulations! You got it!")

      if guessesTaken>5:
       print('\n\nThe word I was thinking of was', word)     




#---------------------------------Main Code Relay-----------------------------------------
#Michel Azar, Donald Winkleman
welcome = 'Welcome to our password assist program! If you want to improve your passwords, you can test their strength and recieve suggestions to strengthen them. There is also an interactive game that teaches you about the importance of choosing a strong, secure password for you to play! What do you want to do first?\n\n 1. Check password strength\n 2. Generate a new password\n 3. Play the interactive game\n\nWhat would you like to do? '

def main():
  main_runner = input(welcome)

  if (main_runner == "1"): 
    password_tester()

  if (main_runner == "2"):
    passwordvariation()

  if (main_runner == "3"):
    guesswordgame()

  if (main_runner == 'main'):
    main()

  else:
    print('\nInvalid entry, please enter either "1", "2", or "3" in the main menu\n')


main()

main()