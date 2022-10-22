
#--------------------------------Instructor & Importer-------------------------------------

from random import randint
import datetime
import time
import wikipedia

name=input('Hello! What is your name? ')
print("\n\nWelcome to chatbox, ", name, "!  I can perforom numerous functions that can help you a lot \nin your daily tasks!, What do you feel like doing today?\n\n I can:\n\n A. Tell you a joke\n B. Give you good restaurant options \n C. Tell you the day and time \n D. Play a number game \n E. Give you a timed workout catered toward your time schedule \n F. Search for the definition of a term on Wikipedia\n\n Type '?' to see these options again\n Input 'Exit' to log out \n\nNote: To choose a function, please type in the capitalized letter of the function without \nthe period (i.e. A for 'tell me a joke')")

#--------------------------------------Laugh box-------------------------------------------

def joke():
      joketype=randint(1,20)
      if joketype==1:
        print('How does a dog stop a video? By hitting the paws button!')
      if joketype==2:
        print('My teachers told me I would never amount to much because I procrastinate so much. I told them, "Just you wait!"')
      if joketype==3:
        print('Comic Sans walks into a bar. The bartender says, "We do not serve your type here."')
      if joketype==4:
        print("What's a balloon's least favorite type of music? Pop.")
      if joketype==5:
        print("What does the world's top dentist get? A little plaque.")
      if joketype==6:
        print("I used to be addicted to not showering. Luckily, I've been clean for five years.")
      if joketype==7:
        print('Why were they called the Dark Ages? Because there were lots of knights.')
      if joketype==8:
        print("What's the best thing about Switzerland? I don't know, but the flag is a big plus") 
      if joketype==9:
        print('What did the big flower say to the little flower? Hi bud!')
      if joketype==10:
        print("Why is no one friends with Dracula? Because he's a pain in the neck.")
      if joketype==11:
        print('What did one toilet say to the other? You look flushed.')
      if joketype==12:
        print("Want to hear a roof joke? The first one's on the house.")
      if joketype==13:
        print("What should you do if you're attacked by a group of clowns? Go straight for the juggler.")
      if joketype==14:
        print('How does NASA organize a party? They planet.')
      if joketype==15:
        print("Why don't koalas count as bears? They don't have the right koalafications.")
      if joketype==16:
        print("I couldn't figure out why the baseball kept getting bigger. Then it hit me.")
      if joketype==17:
        print('A man walks into a library and orders a hamburger. The librarian says, "This is a library." The man apologizes and whispers, "I would like a hamburger,please."')
      if joketype==18:
        print("Why did the taxi driver get fired? Passengers didn't like it when she went the extra mile.")
      if joketype==19:
        print('A group of crows was arrested for hanging out together. The charge? Attempted murder.') 
      if joketype==20:
        print('Why does Humpty Dumpty love autumn? Because he always has a great fall.')
  


#---------------------------------Resturant Selector---------------------------------------

roundrock_chineserestaurants = ["P.F. Chang's", 'China E Buffet', 'Punch Bowl Social Austin', 'Sichuan Garden', 'Happy Dragon Chinese Bistro' ]
roundrock_italianrestaurants = ["Carraba's Italian Grill", 'Mia Italian Tapas and Bar', 'Reales Italian Cafe', 'North Italia', 'Taverna']
roundrock_mexicanrestaurants = ['La Feria Mexican Restaurant', "Torchy's Tacos", "Chuy's", "El Huarache", "Jardin Corona"]
roundrock_americanrestaurants = ['Hopdoddy', 'Roaring Fork', 'Yardhouse', "Doc B's Restaurant & Grill", "Cheddar's Scratch Kitchen"]
roundrock_japaneserestaurants = ['Haru Sushi', 'Kobe Japanese Steakhouse', 'Osaka Mansun Restaurant', 'Miso Restaurant', "O'Daku Sushi"]



def restaurant_searcher():    
    print("Your options are Chinese, Italian, Mexican, American, and Japanese")
    inputvariable = input("\n\nWhat's your favorite type of cuisine to eat? ") 

    if inputvariable == "Chinese":
      print(" ")
      string = "  "
      ans = str(roundrock_chineserestaurants[0] + "," + " " + roundrock_chineserestaurants[1] + "," + " " + roundrock_chineserestaurants[2] + "," + " " + roundrock_chineserestaurants[3] + "," + " " + roundrock_chineserestaurants[4])
      print("\nThese are you options: ", ans, "\n")
      print(" ")
      second_ques = input("Not sure? type in a question mark for more details about each restaurant: ")
      if second_ques == "?":
        print("\n")
        print("P.F. Changs: casual dining restaurant chain with a plethora of asian food ranging from Mongolian Beef all the way to Hong Kongese street food! Mid-range, acceptable prices")
        print(" ")
        print("China E Buffet: Great for the food-lover, offers mainly authentic Chinese food, most notably duck and tasty dumplings. ")
        print(" ")
        print('Punch Bowl Social Austin: Situated in the Austin Domain, this restaurant offers more of an American-Chinese fusion, as well as some Mexican as well. Widely recommended by foodies. ')
        print(" ")
        print("Sichuan Garden: A unique restaurant with authenic Sizchuan cuisine, widely recommended. ")
        print(" ")

        print("Happy Dragon Chinese Bistro: A hefty menu of Cantonese- & Szechuan-style entrees served on tablecloths with beer & wine, very acceptable prices.")
    





    elif inputvariable == "Italian":
      print(" ")
      string1 = " "
      ans2 = str(roundrock_italianrestaurants[0] + "," + " " + roundrock_italianrestaurants[1] + "," + " " + roundrock_italianrestaurants[2] + "," + " " + roundrock_italianrestaurants[3] + "," + " " + roundrock_italianrestaurants[4])
      print("\nThese are you options: ", ans2, "\n")
      print(" ")
      second_ques = input("Not sure? type in a question mark for more details about each restaurant: ")
      if second_ques == "?":
        print("\n")
        print(" Carraba's Italian Grill: Chain eatery & bar serving a diverse menu of classic Italian fare in a family-friendly setting. Mostly an American-Italian fusion offering plates such as meatballs. ")
        print(" ")
        print("Mia Italian Tapas and Bar: A stylish hangout featuring pizzas, pastas & Italian small plates plus wine, beer & cocktails. Very nice atmosphere and a lively feel to it. ")
        print(" ")
        print("Reales Italian Cafe: Straightforward, family-run trattoria providing NYC-style pizzas & plenty of red-sauce standards. Great for those who like authentic NYC pizzas, amazingly good, according to food reviewers. ")
        print(" ")
        print("North Italia: Very amazing and vibey place offering neo-italian food, mixed with a couple of specials that are a must for any occasion. ")
        print(" ")
        print("Taverna: Upscale but unfussy Italian eatery serving pasta, pizzas, risotto, seafood, cocktails and wine, very rustic feel and tasty pizzas and pastas. ")




    elif inputvariable == "Mexican":
      print(" ")
      string2 = " "
      ans3 = str(roundrock_mexicanrestaurants[0] + "," + " " + roundrock_mexicanrestaurants[1] + "," + " " + roundrock_mexicanrestaurants[2] + "," + " " + roundrock_mexicanrestaurants[3] + "," + " " + roundrock_mexicanrestaurants[4])
      print("\nThese are you options: ", ans3, "\n")
      print(" ")
      second_ques = input("Not sure? type in a question mark for more details about each restaurant: ")
      if second_ques == "?":
        print("\n")
        print("La Feria Mexican Restaurant: Casual spot for Mexican classics & a full bar, with booth seating, beer signs, TVs & mariachis, small but lively. ")
        print(" ")
        print("Torchy's Tacos: Offers wonderfully tasty tacos and amazing queso, recommended for a quick yet filling meal. ")
        print(" ")
        print("Chuy's: Tex-Mex restaurant based in Austin, has a unique vibe and is a truly different experience! ")
        print(" ")
        print("El Huarache: Unfussy restaurant turning out hearty, traditional Mexican grub for breakfast, lunch & dinner. Very, very quaint and average-looking place, but the food makes up for that! ")
        print(" ")
        print("Jardin Corona: Pricey yet top-class food, some claim it is 'Best mexican food in Texas!' ")

  


    elif inputvariable == "American":
      print(" ")
      string3 = " "
      ans4 = str(roundrock_americanrestaurants[0] + "," + " " + roundrock_americanrestaurants[1] + "," + " " + roundrock_americanrestaurants[2] + "," + " " + roundrock_americanrestaurants[3] + "," + " " + roundrock_americanrestaurants[4])
      print("\nThese are you options: ", ans4, "\n")
      print(" ")
      second_ques = input("Not sure? type in a question mark for more details about each restaurant: ")
      if second_ques == "?":
        print("\n")
        print("Hopdoddy: Highly recommended for burger, fries and milkshake lovers, usually a lot of people in line and a very long wait but worth it in the end. ")
        print(" ")
        print("Roaring Fork: Sleek restaurant with a buzzy happy hour serving upmarket Southwestern fare, such as steak and cornbread as well as good fish. Very upscale, so dress nicely! ")
        print(" ")
        print("Yardhouse: High-end sports-bar chain with a huge menu of New American fare & an extensive list of draft beers, has one of the largest draft beer menus in Texas. Serves burgers, fish tacos, salsa n chips and much more delights! ")
        print(" ")
        print("Doc B's Restaurant and Grill: Great for brunches, amazing burgers and unique homemade, southwestern and northeastern dishes. ")
        print(" ")
        print(" Cheddar's Scratch Kitchen: Mainly standard American food, very family-friendly and has many great reviews such as 'The food was excellent!' and 'The burger was very well-made. '")

    elif inputvariable == "Japanese":
      print(" ")
      string4 = " "
      ans5 = str(roundrock_japaneserestaurants[0] + "," + " " + roundrock_japaneserestaurants[1] + "," + " " + roundrock_japaneserestaurants[2] + "," + " " + roundrock_japaneserestaurants[3] + "," + " " + roundrock_japaneserestaurants[4])
      print("\nThese are you options: ", ans5, "\n")
      print(" ")
      second_ques = input("Not sure? type in a question mark for more details about each restaurant: ")
      if second_ques == "?":
        print("\n")
        print("Haru Sushi: Inventive rolls & hot dishes served in an upscale Japanese cafe amid bamboo touches. Very generously filled plates with mainly sushi and teriyaki variations. ")
        print(" ")
        print("Kobe Japanese Steakhouse: As suggested by the name of the restaurant, this place mainly serves rare chops of Japanese steaks with a plethora of sauces ranging from super sweet to extremely spicy. ")
        print(" ")
        print("Osaka Manusn Restaurant: Straightforward spot serving a mix of Japanese & Korean dishes, including sushi rolls & bibimbop. Mainly Japanese yet Korean is also very good here too. ")
        print(" ")
        print("Miso Restaurant: Laid-back eatery in a shopping plaza with a sushi bar, plus traditional Korean & Japanese standards. Has a very nice colorful stone bar with well-known chefs in the Austin area. ")
        print(" ")
        print("O'Daku Sushi: Shopping-center outpost for Korean & Japanese favorites, including sushi, bulgogi & noodle dishes. A not-too-shabby place with an old feel to it and wonderful aromas throughout the restaurant. ")

    else:
      print("\nNot an option, please input the name of your preffered cuisine from the list with the first letter being uppercase")



#--------------------------------------Time Tracker----------------------------------------

def day_and_time():
    now = datetime.datetime.now()
    print ("Current date and time: ")
    print (now.strftime("%Y-%m-%d %H:%M:%S"))

#---------------------------------------Wiki Reader----------------------------------------

def wikipedia_search():
  question=input('What term would you like to know about? ')
  detail=input('\nHow many sentences would you like in the summary? ')

  print("\n\n",wikipedia.summary(question, sentences=int(detail)))

#--------------------------------------Guessing Game---------------------------------------

def guessnumbergame():
    guessesTaken = 0





    number = randint(1, 21)
    print('Well, ' + name + ', I am thinking of a number between 1 and 20.')



    while guessesTaken < 6:

      guess=input('\n\nTake a guess: ') # There are four spaces in front of print.
      guess = int(guess)


      guessesTaken = guessesTaken + 1

      if guess < number:

       print('Your guess is too low.') # There are eight spaces in front  of print.


      if guess > number:

        print('Your guess is too high.')



      if guess == number:
        guessesTaken = str(guessesTaken)
        print('\n\nGood job, ' + name + '! You guessed my number in ' + guessesTaken + ' guesses!')
        main_runner()



      if guessesTaken>5:
       print('\n\nThe number I was thinking of was', number)     

#---------------------------------Fitnessgram Pacer Test-----------------------------------

def workout():
    print("Welcome to your workout!\n\n For a 4 minute workout, type 'Short'\n For a 9 minute workout, type 'Long'\n")
    mainquestion = input()
    
    if mainquestion == 'Long':
      print("\n\nEach exercise's time will be printed after the previous excercize has ended, \ngood luck!\n")
      time.sleep(4)
      print('\nReady,')
      time.sleep(2)
      print('\nSet,')
      time.sleep(2)
      print('\nGo!\n\n')
      time.sleep(1)
      print("Mountain Climbers for 40 seconds")
      time.sleep(40)
      print("Left Side Plank for 25 seconds")
      time.sleep(25)
      print("12 Sit-ups for 20 seconds")
      time.sleep(20)
      print("50 Russian Twists for 90 seconds")
      time.sleep(90)
      print("Mountain Climbers for 40 seconds")
      time.sleep(40)
      print("Rest for 30 seconds, you got this!")
      time.sleep(25)
      print("Superman Planks for 30 seconds")
      time.sleep(20)
      print("Forearm Side PLank - Left for 90 seconds")
      time.sleep(90)
      print("15 Windsheild Wipers for 40 seconds")
      time.sleep(40)
      print("Plank for 25 seconds")
      time.sleep(25)
      print("Bicycle Kicks for 20 seconds")
      time.sleep(20)
      print("Mountain Climbers for 90 seconds")
      time.sleep(90)
      print("Congratulations, you have successfully completed the workout!")
    elif mainquestion == 'Short':
      print("\n\nEach exercise's time will be printed after the previous excercize has ended, \ngood luck!\n")
      time.sleep(4)
      print('\nReady,')
      time.sleep(2)
      print('\nSet,')
      time.sleep(2)
      print('\nGo!\n\n')
      time.sleep(1)
      print("Jumping Jacks for 60 seconds")
      time.sleep(60)
      print("Burpees for 30 seconds")
      time.sleep(30)
      print("Rest for 30 seconds")
      time.sleep(30)
      print("Side Lunges for 60 seconds")
      time.sleep(60)
      print("Pushups for 30 seconds")
      time.sleep(30)
      print("Lunge with a Twist for 60 seconds")
      time.sleep(60)
      print("Congratulations, you have successfully completed the workout!")
    else:
      print(" ")

#-----------------------------------Main Input Code----------------------------------------

def main_runner():

  UsingFunction = True
  while UsingFunction == True:
    chooser=input('\n\n\nWhat would you like to do? ')
    print('\n\n')
    if chooser == "A":
      joke()
    elif chooser == "B":
      restaurant_searcher()
    elif chooser == "C":
      day_and_time()
    elif chooser == "D":
      guessnumbergame()
    elif chooser == "E":
      workout()
    elif chooser == "F":
      wikipedia_search()
    elif chooser == "?":
      print("Welcome to chatbox, ", name, "!  I can perform numerous functions that can help you a lot \nin your daily tasks!, What do you feel like doing today?\n\n I can:\n\n A. Tell you a joke\n B. Give you good restaurant options \n C. Tell you the day and time \n D. Play a number game \n E. Give you a timed workout catered toward your time schedule\n F. Search for the definition of a term on Wikipedia\n\n Type '?' to see these options again\n Input 'Exit' to log out \n\nNote: To choose a function, please type in the capitalized letter of the function without \nthe period (i.e. A for 'tell me a joke')")
    elif chooser == "Exit":
      print('Thank you, I hope you enjoyed the program!')
      UsingFunction = False
    else:
      print("Sorry, that is not part of my functionality! Please refer to the list of my functions by typing a question mark! ")



main_runner()
