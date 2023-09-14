
import random

def startGame():
  pcScore = 0
  yourScore = 0

  def scores():
    print(f'your score: {yourScore} \n pc score: {pcScore}')

  while True:

    randomPc=random.choice(['rock', 'paper', 'scissors'])
    choose= input("Choose between 'rock', 'paper', 'scissors': ")

    if choose in["Exit", "exit", "Quit", "quit"]:
      print('Bye')
      break
    if choose not in ['rock', 'paper', 'scissors']:
      print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
      continue
        

    if choose == randomPc:
      print(f"Computer's choice was also {randomPc}, it's tie ")
      scores()
    elif (choose == 'rock' and randomPc == 'scissors') or \
      (choose == 'paper' and randomPc == 'rock') or \
      (choose == 'scissors' and randomPc == 'paper'):
      print(f"Computer's choice was {randomPc}, you won!")
      yourScore += 1
      scores()
    else:
      print(f"Computer's choice was {randomPc}, you lost.")
      pcScore += 1
      scores()


startGame()    
