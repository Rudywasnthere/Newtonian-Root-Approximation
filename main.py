## Rudy Garcia

import random as rd
import math as math


def main():
  print("Hello, I do Newtonian Approximation to get you decently close roots")
  function = new_function()
  aprox_1 = float(int_input("start"))
  times = int(int_input("times"))
  approximation = approximater(function, aprox_1, times)
  print(f"Your approximation: {approximation}")

def new_function():
  tries = 0
  play = False
  while play == False:
    user_function = input("Function: ")
    user_function = replacer(user_function)
    f = lambda x: eval(user_function)
    random_1 = rd.randint(0,100)
    random_2 = rd.randint(0,100)
    random_3 = rd.randint(0,100)
    try:
      useless_garbage = f(random_1)
      play = True
    except ZeroDivisionError:
      print(f"break at: {random_1}")
      try:
        useless_again = f(random_2)
        play = True
      except ZeroDivisionError:
        play = True
        print(f"break two at: {random_2}")
        try:
          useless_finally = f(random_3)
        except ZeroDivisionError:
          print(f"break three at: {random_3}")
    except SyntaxError:
      if tries//2 == 0:
        print("I need correct syntax")
      play = False
    except NameError:
      print("NameError")
  return user_function

def replacer(user_function):
  if ".cos(" not in user_function:
    user_function = user_function.replace("cos(", "math.cos(")
  if ".sin(" not in user_function:
    user_function = user_function.replace("sin(", "math.sin(")
  if ".tan(" not in user_function:
    user_function = user_function.replace("tan(", "math.tan(")
  if ".acos(" not in user_function:
    user_function = user_function.replace("arccos(", "math.acos(")
    user_function = user_function.replace("cos^-1(", "math.acos(")
  if ".asin(" not in user_function:
    user_function = user_function.replace("arcsin(", "math.asin(")
    user_function = user_function.replace("sin^-1(", "math.asin(")
  if ".atan(" not in user_function:
    user_function = user_function.replace("arctan(", "math.atan(")
    user_function = user_function.replace("tan^-1(", "math.atan(")
  if ".log(" not in user_function:
    user_function = user_function.replace("log(", "math.log10(")
  if ".ln(" not in user_function:
    user_function = user_function.replace("ln(", "math.log(")
  if ".sqrt(" not in user_function:
    user_function = user_function.replace("sqrt(", "math.sqrt(")
  if ".exp(" not in user_function:
    user_function = user_function.replace("e**x" , "math.exp(x)")
  return user_function

def int_input(case):
  if case == "start":
    usr = input("Number close to root: ")
  if case ==  "times":
    usr = input("Number of (n) times to approximate with: ")
  play = False
  while False:
    try:
      usr = float(usr)
      play = True
    except:
      usr = input("I need an number m8: ")
  return usr

def approximater(function, start, times):
  f = lambda x: eval(function)
  current = start
  for x in range(0, times):
    d = float((f(current + 0.001) - f(current))/ (0.001))
    current = float(current - f(current)/d)
  return current
  
main()