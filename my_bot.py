from secret import my_username
import random
"""
**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""
def should_i_respond(user_message, user_name):
  if "gamble" in user_message:
    return True
  else:
    return False
  
def respond(user_message, user_name):
  global
  file = open("SavedData.txt", "r")
  
  print (var)
  
  balance = var
  file.close()
  file = open("SavedData.txt", "w")
  file.write(str(var))
  file.close
  ammount = checkbalance(user_name)
  # need to change this to be able to respond to different functions and respond with input amound and then go into the betting
  # probably just start with betamount() and then whatever game e.g. coinflip() or blackjack()
  return f"""you said my name!!
  {user_message.replace("gamble", user_name)} you have {ammount} dollars"""



#Use dictionary and maybe .append
# balance [f"{user_name}"] = 2
balance = {}
print(balance["Ido"])

# balance[username]
#REMEMBER TO SAVE THE TXT FILE BEFORE USING
# fully flesh out balance system for multiple users ideally with a format like @username : balance
# then modify all the balance checks to check for the specific user balance probably not with a text file

def checkbalance(user_name):
  global balance
  account = list(balance.keys())
  if user_name in account:
    return(balance)
  else:
    balance[user_name] = 0
  
  

  # global balance
  # global var


bet = int(0)

def betamount():
  global bet
  global balance
  bet = int.input("How much would you like to bet?")
  if bet <= balance:
    balance = balance - bet
    print (f"You have bet {bet} dollars and have {balance} left in your account")
  else:
    print (f"Please input a valid response. You have {balance} in your account")
    betamount()

rcolor = ()
rnumber = int()
def roullete():
  global rcolor
  global rnumber
  rcolor = input("What color would you like to bet on, Red (R), Black (B), or Green (G)?")
  rnumber = int.input("What number would you like to bet on")
  #fix this https://www.wikihow.com/Play-Roulette

def blackjack():
  pass
  #add proper deck of cards then deal cards, 1 face up to dealer and 1 face down to dealer, and 2 to you. add splitting if its not too hard
  #get options of hit or stand, once you stand, dealer reveals hits on 16 or lower or soft 17(one with an ace)
  #and stands on hard 17 or higher
  #hands are compared and bets are given

def bingo():
  pass
  #figure out the amount of bingo numbers that would be optimal for the hosue to win and how the betting should work
  #mbe scrap bingo

def slots():
  pass
  #likely just going to be slots of 3 but maybe try and make the 5x5 or whatever and print out a graph something like ascii


  


def coinflip():
  #hopefully should work
  global balance
  global bet
  coin = random.choice(["heads", "tails"])
  if coin == "heads":
    balance += bet
  elif coin == "tails":
    balance -= bet



# 