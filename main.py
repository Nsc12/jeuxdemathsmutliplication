start = str(input("Un mini-jeux de mathématiques : multiplication (go pour commencer)"))
while start != "go":
    start = str(input("Un mini-jeux de mathématiques : multiplication (go pour commencer)"))
print("Bonne chance")

n = int(input("0*9 = "))
while n != 0:
    n = int(input("X 0*9 = "))
    if n == 0:
        print("V")

n = int(input("1*2 = "))
while n != 2:
    n = int(input("X 1*2 = "))
    if n == 0:
     print("V")

n = int(input("1*9 = "))
while n != 9:
  n = int(input("X 1*9 = "))
  if n == 9:
    print("V")

n = int(input("1*6 = "))
while n != 6:
  n = int(input("X 1*6 = "))
  if n == 6:
      print("V")
n = int(input("2*9 = "))
while n != 18:
  n = int(input("X 2*9 = "))
  if n == 18:
      print("V")

n = int(input("2*4 = "))
while n != 8:
  n = int(input("X 2*4 = "))
  if n == 8:
      print("V")

n = int(input("3*9 = "))
while n != 27:
  n = int(input("X 3*9 = "))
  if n == 27:
      print("V")

n = int(input("3*4 = "))
while n != 12:
  n = int(input("X 3*4 = "))
  if n == 12:
      print("V")

n = int(input("4*9 = "))
while n != 36:
  n = int(input("X 4*9 = "))
  if n == 36:
      print("V")

n = int(input("4*5 = "))
while n != 20:
  n = int(input("X 4*5 = "))
  if n == 20:
      print("V")

n = int(input("5*3 = "))
while n != 15:
  n = int(input("X 5*3 = "))
  if n == 15:
      print("V")

n = int(input("5*7 = "))
while n != 35:
  n = int(input("X 5*7 = "))
  if n == 35:
      print("V")


print("Fini")
