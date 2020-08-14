# In this game first of all you have to define on number ex: n=10
# After that you have to take input from user
# you have to create loop in which it will check if user input is matched with defined number 
# If input is matched then it will print sucess message with how many time he/she guess
# else it will check till some limitation that we proide in loop
# if limitation is over you have to print message that limit is over



print("-------------Guess The Number--------------")
 
you_have_to_guess = 18
chance = 10

for num in range(chance):
    num += 1
    guess = int(input("Enter Your Guessing Number: "))
    if guess > 18:
        print("Guess lesser number...\n")
        print(f"you have  {(chance)-(num)} attemp left\n")
        continue
    elif guess < 18:
        print("Guess greater number then this...\n")
        print(f"you have  {(chance)-(num)} attempt left\n")
        continue
    elif you_have_to_guess == guess:
        print("Congratulation your guess is correct!\n")
        print(f"you take {num} attempt for the perfact guess\n")
        break
    
print("Game is over!!\n")


