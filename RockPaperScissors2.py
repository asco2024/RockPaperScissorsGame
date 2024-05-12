import random
import streamlit as st
import pygame

#inisialize pygame mixer
pygame.mixer.init()
#load sound effects

win_sound = pygame.mixer.Sound("real win sound.wav")
tie_sound = pygame.mixer.Sound("draw sound.wav")
lose_sound = pygame.mixer.Sound("real lose sound.mp3")

def rockPaperScissors(userChoice):
    choices = ["rock","paper","scissors"]
    computerChoice = random.choice(choices)
    result = ""
 
    if userChoice == computerChoice:
        tie_sound.play() 
        result = "a draw"
    elif (userChoice == "rock" and computerChoice == "scissors") or (userChoice == "scissors" and computerChoice == "paper") or (userChoice == "paper" and computerChoice == "rock"):
        result = "you won. Well done."
        win_sound.play()
    elif (computerChoice == "rock" and userChoice == "scissors") or (computerChoice == "scissors" and userChoice == "paper") or (computerChoice == "paper" and userChoice == "rock"):
        result = "you lost🤣. Better luck next time."
        lose_sound.play()  
    return result,computerChoice 


st.title("Rock Paper Scissors Game")
st.header("This game is written by Osman and Cisse")
st.header("choose your option") 
userChoice = st.radio("",("rock","paper","scissors"))
print(userChoice)

osman,cisse = rockPaperScissors(userChoice)
print(osman)


st.write( f"The computer chose {cisse} and you chose {userChoice} and so the result is {osman}" )

st.write("")






