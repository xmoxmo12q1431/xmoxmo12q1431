import math
from turtle import*

def hearta(k):
  return 15*math.sin(K)**3

def heartb(k):
  return 12*math.cos(k)-5*\
  math.cos(2*k)-2*\
  math.cos(3*k)-\
  math.cos(4*k)

speed(9000)
bgcolour("black")

for i in range(6000):
  goto(hearta(i)*20,heartb(i)*20)
  for i in range(5):
    colour("red")
  goto(0,0)
done()
