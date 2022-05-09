import random
import sys

MapSize= int(input("맵의 크기는 얼마인가요?:"))
BompCount=int(input("폭탄개수는?:"))

map = []

def MakeMap(MapSize, BompCount):
    
    for i in range(MapSize):
        subList=[]
        for j in range(MapSize):
            subList.append("🔳")
        map.append(subList)
        
    map[0][0]="⬜"
    while True:
        px=random.randint(0,MapSize-1)
        py=random.randint(0,MapSize-1)
        if (px!=0 or py!=0):
            map[px][py]="💠"
            break
    count=0
    while True:
        bx=random.randint(0,MapSize-1)
        by=random.randint(0,MapSize-1)
        if ((bx!=0 and by!=0)and (bx!=px and by!=py)):
            count+=1
            map[bx][by]="🔺"
            if(count==BompCount):
                break

    for i in range(MapSize):
        for j in range(MapSize):
            print(map[i][j], end=' ')
        print()
    

UserX=0
UserY=0

def MoveUser():
    global UserX, UserY
    print("1. 아래로 이동")
    print("2. 위로 이동")
    print("3. 오른쪽으로 이동")
    print("4. 왼쪽으로 이동")
    temp =int(input("입력:"))
    

    if temp ==1:
        nx= UserX+1
        ny= UserY
        if (map[nx][ny]=="🔺"):
            return False
        if (map[nx][ny]=="💠"):
            print ("성공하셨습니다!")
            sys.exit()
        map[nx][ny]="⬜"
        map[UserX][UserY]="🔳"
        UserX=nx
        UserY=ny
        for i in range(MapSize):
             for j in range(MapSize):
                print(map[i][j], end=' ')
             print()
 
        
    
    
    elif temp ==2:
        nx= UserX-1
        ny= UserY
        if (map[nx][ny]=="🔺"):
            return False
        if (map[nx][ny]=="💠"):
            print ("성공하셨습니다!")
            sys.exit()     
        map[nx][ny]="⬜"
        map[UserX][UserY]="🔳"
        UserX=nx
        UserY=ny
        for i in range(MapSize):
             for j in range(MapSize):
                print(map[i][j], end=' ')
             print()
 

    elif temp ==3:
        nx= UserX
        ny= UserY+1
        if (map[nx][ny]=="🔺"):
            return False
        if (map[nx][ny]=="💠"):
            print ("성공하셨습니다!")
            sys.exit()
        map[nx][ny]="⬜"
        map[UserX][UserY]="🔳"
        UserX=nx
        UserY=ny
        for i in range(MapSize):
             for j in range(MapSize):
                print(map[i][j], end=' ')
             print()
 

    elif temp ==4:
        nx= UserX
        ny= UserY-1
        if (map[nx][ny]=="🔺"):
            return False
        if (map[nx][ny]=="💠"):
            print ("성공하셨습니다!")
            sys.exit()
        map[nx][ny]="⬜"
        map[UserX][UserY]="🔳"
        UserX=nx
        UserY=ny
        for i in range(MapSize):
             for j in range(MapSize):
                print(map[i][j], end=' ')
             print()
 
    
    
MakeMap(MapSize, BompCount)    
while True:
    MoveUser()
