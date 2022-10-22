#----------------------------------Intro Section----------------------------------------

def intro():
  print("\n\nWelcome to the Wordle solver! If you're stuck on a Wordle, you're in the right place. To get started, choose one of the options below by typing in its corresponding letter or symbol:\n\nA. Get word suggestions for a partially solved Wordle\n\n Type '?' to see these options again\n Input 'Exit' to log out")

intro()


#----------------------------------Lists & Imports----------------------------------------

import json
import requests
import urllib
import enchant

templist = []
unknowns = []
listNotPresent = []
ordering = []
filteredWords = []
notLocations = []
sortedWords = []
commonality = []
allWords = []

letterPop = [8.2, 1.5, 2.7,	4.7, 13, 2.2,	2, 6.2,	6.9, 0.16, 0.81, 4.0,	2.7, 6.7, 7.8, 1.9,	0.11,	5.9, 6.2, 9.6, 2.7, 0.97,	2.4, 0.15, 2,	0.078]

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

impossibleDoubles = ['bk', 'fq', 'jc', 'jt', 'mj', 'qh', 'qx', 'vj', 'wz', 'zh', 'bq', 'fv', 'jd', 'jv', 'mq', 'qj', 'qy', 'vk', 'xb', 'zj', 'bx', 'fx', 'jf', 'jw', 'mx', 'qk', 'qz', 'vm', 'xg', 'zn', 'cb',  'fz', 'jg', 'jx', 'mz', 'ql', 'sx', 'vn', 'xj', 'zq', 'cf', 'gq', 'jh', 'jy', 'pq', 'qm', 'sz', 'vp', 'xk', 'zr', 'cg', 'gv', 'jk', 'jz', 'pv', 'qn', 'tq', 'vq', 'xv', 'zs', 'cj', 'gx', 'jl', 'kq', 'px', 'qo', 'tx', 'vt', 'xz', 'zx', 'cp', 'hk', 'jm', 'kv', 'qb', 'qp', 'vb', 'vw', 'yq', 'cv', 'hv', 'jn', 'kx', 'qc', 'qr', 'vc', 'vx', 'yv', 'cw', 'hx', 'jp', 'kz', 'qd', 'qs', 'vd', 'vz', 'yz', 'cx', 'hz', 'jq', 'lq', 'qe', 'qt', 'vf', 'wq', 'zb', 'dx', 'iy', 'jr', 'lx', 'qf', 'qv', 'vg', 'wv', 'zc', 'fk', 'jb', 'js', 'mg', 'qg', 'qw', 'vh', 'wx', 'zg']

ynAccept = ['y', 'n']


#-------------------------------------Google Ngram (Word Popularity) Parser------------------------------------------

def seeker(query, start_year = 2020, end_year = 2020, corpus = 26, smoothing = 100000):
  
  query = urllib.parse.quote(query)
  url = 'https://books.google.com/ngrams/json?content=' + query + '&year_start=' + str(start_year) + '&year_end=' + str(end_year) + '&corpus=' + str(corpus) + '&smoothing=' + str(smoothing) + ''
  
  response = requests.get(url)
  output = response.json()
  return_data = []
    
  if len(output) == 0:
    return "No data available for this Ngram."
  
  else:
    for num in range(len(output)):
      return_data.append((output[num]['ngram'], output[num]['timeseries']))
      string = str(return_data)
      big = string.split(',')
      last = big[len(big) - 1]
      
      return last


#-------------------------------------Data Entry Error Correction------------------------------------------

def checker(known, directive):
  
  if len(known) > 5 and directive == 1:
    print("You included more than 5 characters in your entry, please list out the letters you know with spaces representing the positions where you don't know the letter")
    known = input().lower()
    checker(known, 1)

  if len(known) < 5 and directive == 1:
    print("You included less than 5 characters in your entry, please list out the letters you know with spaces representing the positions where you don't know the letter")
    known = input().lower()
    checker(known, 1)

  if len(known) > 5 and directive == 3:
    print("You included more than 5 characters in your entry, please list out a combination of only y's and n's that is a total of 5 characters long")
    known = input().lower()
    checker(known, 3)

  if len(known) < 5 and directive == 3:
    print("You included less than 5 characters in your entry, please list out a combination of only y's and n's that is a total of 5 characters long")
    known = input().lower()
    checker(known, 3)

  for i in known:
    if (i not in letters) and ((i == ' ') == False) and directive == 1:
      print("There's a character other than a letter or space present. Please retype the letters you know with spaces representing characters you don't know")
      first = input().lower()
      checker(first, 1)

  for i in known:
    if i in listNotPresent and directive == 2:
      print("You've typed a letter listed as not being present previously. Please re-enter the orange characters in your wordle guesses without including letters you listed as not present or restart this application")
      known = input().lower()
      checker(known, 2)
      
    elif i not in letters and directive == 2:
      print("You've typed something besides a letter in your list of orange letters. Please re-enter the orange characters in your wordle guesses with no repeats")
      known = input().lower()
      checker(known, 2)

    if i not in ynAccept and directive == 3:
      print("You included less than 5 characters in your entry, please list out a combination of only y's and n's that is a total of 5 characters long")
      known = input().lower()
      checker(known, 3)
  
  return known


#-------------------------------------Filtering Impossible Words------------------------------------------

def discarder(templist, unknowns, notLocations):
  word = ''
  
  for i in range(len(templist)):
    word = word + templist[i]
    
  for i in range(len(unknowns)):
    if unknowns[i] not in word:
      return 'false'
    
    unknown = str(unknowns[i])
    notLocation = str(notLocations[i])
    notLocation = notLocation.replace('y', '$')
    notLocation = notLocation.replace('n', unknown)
    for x in range(len(notLocation)):
      if notLocation[x] == word[x]:
        return 'false'
      
  for i in range(len(impossibleDoubles)):
    if word.find(impossibleDoubles[i]) != -1:
      return 'false'

  return word


#-------------------------------------Information Requests------------------------------------------

def guesser(): 
  templist = []
  unknowns = []
  listNotPresent = []
  ordering = []
  filteredWords = []
  notLocations = []
  sortedWords = []
  commonality = []
  allWords = []
  
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  
  print("\nPlease spell out the word with the letters you know the locations of so far. If you don't know what letter is in a space, use a space in that place." + ' For example: stove = "s o e", lists = "lis  "')
  first = input()
  first = first.lower()
  first = checker(first, 1)
  for i in first:
    templist.append(i)

  print("\nList all the letters that you've already tried and that aren't present in the word")
  notPresent = input().lower()
  for i in notPresent:
    if i in letters:
      letters.remove(i)
      listNotPresent.append(i)
      
  print("If there are other letters present that you don't know the positions of, please list them without spaces. If not, please press enter")
  somewheres = input().lower()
  somewheres = checker(somewheres, 2)
  for i in somewheres:
    unknowns.append(i)

  if len(unknowns) > 0:
    for i in (unknowns):
      print("List the positions where the letter " + '"' + i + '"' + " could be by listing a combination of 5 y's (representing possible areas for the letter) and n's (representing the areas where the letter has already been tested.)" + ' For example: "yynny"')
      notLocation = input().lower()
      notLocation = checker(notLocation, 3)
      notLocations.append(notLocation)
    

#-------------------------------------Random Word Generation------------------------------------------

  print('Please wait, this might take a while...')
  loops = 5 - len(first.replace(' ', ''))
  r = len(letters)
       
  if loops == 1:
    for a in letters:
      
      loopThreading = [a]
      threaded = []
      sum = 0
      for i in range(len(templist)):
        if templist[i] == ' ':
          threaded.append(loopThreading[sum])
          sum = sum + 1
        else:
          threaded.append(templist[i])
      test = discarder(threaded, unknowns, notLocations)
      if test != 'false':
        allWords.append(test)

  if loops == 2:
    for a in letters:
      for b in letters:
        
        loopThreading = [a, b]
        threaded = []
        sum = 0
        for i in range(len(templist)):
          if templist[i] == ' ':
            threaded.append(loopThreading[sum])
            sum = sum + 1
          else:
            threaded.append(templist[i])
        test = discarder(threaded, unknowns, notLocations)
        if test != 'false':
          allWords.append(test)
    
  if loops == 3:
    for a in letters:
      for b in letters:
        for c in letters:
          
          loopThreading = [a, b, c]
          threaded = []
          sum = 0
          for i in range(len(templist)):
            if templist[i] == ' ':
              threaded.append(loopThreading[sum])
              sum = sum + 1
            else:
              threaded.append(templist[i])
          test = discarder(threaded, unknowns, notLocations)
          if test != 'false':
            allWords.append(test)
      
  if loops == 4:
    for a in letters:
      for b in letters:
        for c in letters:
          for d in letters:
            
            loopThreading = [a, b, c, d]
            threaded = []   
            sum = 0
            for i in range(len(templist)):
              if templist[i] == ' ':
                threaded.append(loopThreading[sum])
                sum = sum + 1
              else:
                threaded.append(templist[i])
            test = discarder(threaded, unknowns, notLocations)
            if test != 'false':
              allWords.append(test)
            
  if loops == 5:
    for a in letters:
      for b in letters:
        for c in letters:
          for d in letters:
            for e in letters:
              
              loopThreading = [a, b, c, d, e]
              threaded = []
              sum = 0
              for i in range(len(templist)):
                if templist[i] == ' ':
                  threaded.append(loopThreading[sum])
                  sum = sum + 1
                else:
                  threaded.append(templist[i])
              test = discarder(threaded, unknowns, notLocations)
              if test != 'false':
                allWords.append(test)
                

#-------------------------------------Real/Fake Word Filter and Popularity Sorter------------------------------------------

  d = enchant.Dict("en_US")
  for i in allWords:
    if d.check(i) == True:
      filteredWords.append(i)
  if len(filteredWords) < 30:
    for i in filteredWords:
      try:
        searched = seeker(i)
        if searched != "No data available for this Ngram.":
          commonality.append(seeker(i))
        else:
          filteredWords.remove(i)
      except:
        filteredWords.remove(i)

    for i in commonality:
      chainZero = ''
      magnitude = i[len(i)-4 : len(i)-3]
      if magnitude[0] == '0':
        magnitude = magnitude[1:]
      for x in range(int(magnitude) - 1):
        chainZero = chainZero + '0'
      chainZero = '.' + chainZero + '1'
      ordering.append(float(chainZero) * float(i[0:len(i)-7]))
  
  else:
    for i in filteredWords:
      popularity = 0
      for x in i:
        pos = ord(x) - 97
        popularity = popularity + letterPop[pos]
      ordering.append(popularity)
      
  for i in range(len(filteredWords)):
    posMax = ordering.index(max(ordering))
    sortedWords.append(filteredWords[posMax])
    filteredWords.remove(filteredWords[posMax])
    ordering.remove(ordering[posMax])
    
  print('Here are your best possible guess options arranged from top to bottom:\n')
  for i in sortedWords:
    print(i)
    

#-------------------------------------Main Runner------------------------------------------

def main():
  choice = input("\n\nWhat would you like to do? ")

  if choice == 'A' or choice == 'a':
    guesser()
    main()

  elif choice == '?':
    intro()
    main()
  elif choice == "Exit" or choice == "exit":
    print("\nThanks for stopping by! Shutting down...")
  else:
    print("\nSorry, that is not part of my functionality! Please refer to the list of my functions by typing a question mark! ")
    main()

main()