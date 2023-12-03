from math import *
from turtle import *
from ion import *

pendown()

# Initialisation de la variable taille

s=1

#introduction

print("Bienvenue dans NFPaint, un outil de dessin simple pour Numworks !")
print("(c) Lord Manchot, 2023")
print("")
print("APPUYEZ SUR UNE TOUCHE")
print("POUR COMMENCER")

#fun part

while True :
  s=pensize()

  #Couleurs

if keydown(KEY_ONE):
  color("red")
if keydown(KEY_ZERO):
  color("black")
if keydown(KEY_TWO)
  color ("'blue")
if keydown(KEY_THREE):
  color ("yellow")
if keydown (KEY_FOUR):
  color ( "green ")
if keydown(KEY_FIVE):
  color ("orange")
if keydown(KEY_SIX) :
  color("purple")

# Taille

if keydown (KEY_PLUS):
    pensize(s+1)
if keydown(KEY_MINUS):
    pensize(s-1)

# Contrôles

if keydown(KEY_RIGHT):
  setheading(0)
  forward(1)

if keydown(KEY_UP):
  setheading(90)
  forward(1)

if keydown(KEY_LEFT):
  setheading(180)
  forward(1)

if keydown(KEY_DOWN):
  setheading(270)
  forward(1)

# Réinitialisation

if keydown(KEY_BACKSPACE):
  reset()

# Introduitre du texte (expérimental)

if keydown(KEY_ALPHA):
  text=input("Écrivez votre texte :")
  write(text)
