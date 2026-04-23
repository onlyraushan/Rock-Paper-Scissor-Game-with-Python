import random 
item_list = ["Rock","Paper", "Scissor"]

user_choice = input("Enter your choice (Rock, Paper, Scissor): ")
comp_choice = random.choice(item_list)

print(f"User Choice = {user_choice}, Computer Choice = {comp_choice}")

if user_choice == comp_choice:
  print("You both choosed same, Match Tie")
  
elif user_choice == "Rock":
  if comp_choice == "Paper":
    print("Computer Wins")
  elif comp_choice == "Scissor":
    print("You Win")
  
elif user_choice == "Paper":
  if comp_choice == "Rock":
    print("You Win")
  elif comp_choice == "Scissor":
    print("Computer Wins")
    
elif user_choice == "Scissor":
  if comp_choice == "Paper":
    print("You Win")
  elif comp_choice == "Rock":
    print("Computer Wins")
    
print("Have a Good Day")