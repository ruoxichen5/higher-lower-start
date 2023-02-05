import art
import random
from replit import clear
from game_data import data

##randomly choose two people
chosen_two = random.sample(data, 2)
## a function to print out content in dic with two indexes
def header(dic_list):
  desc = []
  for dic in dic_list:
    dic['from'] = "from" 
    for i in ('name', 'description', 'from','country'):
      desc.append(dic[i])
  return desc
def print_header(chosen_two):
  print(art.logo)
  desc = header(chosen_two)
  bio1 = desc[0:4]
  bio2 = desc[4:8]
  print("Compare A "+(", ".join(bio1).replace("from,","from")))
  print(art.vs)
  print("Against B "+(", ".join(bio2).replace("from,","from"))) 
## a function to choose next round
def choose_new(chosen_two):
  dic1 = chosen_two[0]
  dic2 = chosen_two[1]
  data.remove(dic1)
  dic_new1 = random.choice(data)
  chosen_two = [dic2,dic_new1]
  data.append(dic1)
  return chosen_two
# ask for name guess input
##define a function to choose winner and calculate score
game_stop = False
def game(current_score):
  if (guess == "A" and chosen_two[0]["follower_count"] > chosen_two[1]["follower_count"]) or (guess == "B" and chosen_two[0]["follower_count"] < chosen_two[1]["follower_count"]):  
    current_score += 1
    print("You are right!")
    return current_score
  else:
    global game_stop
    game_stop = True
    return current_score
current_score = 0
while not game_stop :
  print_header(chosen_two)
  guess = input("Who has more followers? Type 'A' or 'B'\n")
  clear()
  game(current_score)
  current_score = game(current_score)
  clear()
  print(f"Current score:{current_score}!")
  chosen_two = choose_new(chosen_two)
print(f"you loose! you scored {current_score} points!") 


