from math import *
from turtle import *
from ion import *

pendown()

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
  if keydown(KEY_TWO):
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

