print("Welcome to my computer quiz!")

playing = input("would you like to play the game? Y/N? ").lower()

if playing != "yes":
    quit()

print("Let's Play :) ")
score = 0

answer = input("What does cpu stands for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("what does GPU stands for? ").lower()
if answer == "graphical processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer = input("What does cli stands for? ").lower()
if answer == "command line interface":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

print("You got "+ str(score) + " Answers right! :)")
print("You got "+ str((score/3) * 100)+ "% :)")
