combinations= [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[0,4,8],[2,5,8],[2,4,6]]
l = [0] * 9 # index-> 0 to 8
playerX_turn = False;
playerO_turn = False;


def checkIfWin():
    for a, b, c in combinations:
        if l[a] != 0 and l[a] == l[b] == l[c]:
            return True
    return False


while True:
  pt = input("Which Player's turn (X/O): ")
  if pt.lower()=='x':
    playerX_turn=True;
    break
  elif pt.lower()=='o':
    playerO_turn=True;
    break
  else:
    print("Enter valid number!")
pX_won = False
pO_won = False

while pX_won==False and pO_won==False:
  if 0 not in l:
    print("Game's DRAW.")
    break
  if playerX_turn:
    box1 = int(input("X's turn, select box (1-9) : "))
    if box1<1 or box1>9:
      print("Enter valid box number!")
      continue
    elif l[box1-1]==0:
      flagX=True
      l[box1-1] = 'x'
      print(l)
      if checkIfWin():
        print("Congrats Player X WON!!")
        pX_won = True
        break
      else:
        playerX_turn = False
        continue
    else:
      print("Spot's already taken, chose the box again!")
      continue
  else:
    box2 = int(input("O's turn, select box (1-9) : "))
    if box2<1 or box2>9:
      print("Enter valid box number!")
      continue
    elif l[box2-1]==0:
      flagO=True
      l[box2-1] = 'o'
      print(l)
      if checkIfWin():
        print("Congrats Player O WON!!")
        pO_won = True
        break
      else:
        playerX_turn = True
        continue
    else:
      print("Spot's already taken, chose the box again!")
      continue



