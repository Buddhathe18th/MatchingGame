import random



def gameboardinit():
    gameboard=[]
    for x in range(82):
        gameboard.append(random.randint(1, 9))
    
    
    return gameboard
    


def printgameboard(gameboard):
    line = ""
    for x in range(len(gameboard)):
        
        
        line = line + "    " + str(gameboard[x])
        if (x+1)%9 == 0:
            
            print (line)
            line=""
 

def findnumber(gameboard, row, column):
    return(gameboard[(row-1)*9 + column - 1])
    
    


def check(mygameboard, number1row, number1column, number2row, number2column):
    flag=False
    
    number1=findnumber(mygameboard, number1row, number1column)
    number2=findnumber(mygameboard, number2row, number2column)
    print("Position of the two pressed values are ("+str(number1row)+", "+str(number1column)+") and "+str(number2row)+", "+str(number2column)+"). Values are "+str(number1)+" and "+str(number2))
    if number1==0 or number2==0:
        return flag;
    if number1==number2 or number1+number2==10:
        flag=False
        if number1column==number2column:
            #same column
            flag=checksamecolumn(mygameboard, number1row, number1column, number2row, number2column)
            print("Matched by column")
        elif checksamediagonalleft(mygameboard,number1row,number1column,number2row,number2column):
                #diagonal left
                flag=checksamediagonalleft(mygameboard, number1row, number1column, number2row, number2column)
                print("Matched by left diagonal")
        elif checksamediagonalright(mygameboard,number1row,number1column,number2row,number2column):
                #diagonal right
                flag=checksamediagonalright(mygameboard, number1row, number1column, number2row, number2column)
                print("Matched by right diagonal")
        elif checksamerow(mygameboard, number1row, number1column, number2row, number2column):
            flag=checksamerow(mygameboard, number1row, number1column, number2row, number2column)
            print("Matched by row")
            
        else:
            flag=False
            print("Did not match")
    else:    
        flag=False
        print("Did not match")
        
    return(flag)

def checkdiagonalleft(number1row,number1column,number2row,number2column):
    position1=(number1row-1)*9 + number1column - 1
    position2=(number2row-1)*9 + number2column - 1
    
    if (position1-position2)%8==0 and number1row!=number2row:
        return(True)
    return(False)

"""def checksameline(number1row,number1column,number2row,number2column):
    number1position=(number1row-1)*9 + number1column - 1
    number2position=(number2row-1)*9 + number2column - 1
            
    if number1position>number2position:
        firstposition=number2position
        secondposition=number1position
    else:
        firstposition=number1position
        secondposition=number2position
    value=firstposition+1
    while value<secondposition:
        if gameboard[value]==0:
            value=value+1
            flag=True
        else:
            flag=False
            break
    return (flag) """  
    

def checkdiagonalright(number1row,number1column,number2row,number2column):
    position1=(number1row-1)*9 + number1column - 1
    position2=(number2row-1)*9 + number2column - 1
    
    if (position1-position2)%10==0:
        return(True)
    return(False)

def checkdiagonal(number1row,number1column,number2row,number2column):
    if abs(number1row-number2row)==abs(number1column-number2column):
        return True
    
    return False
    


def checksamerow(gameboard, number1row, number1column, number2row, number2column):
    flag=True
    number1position=(number1row-1)*9 + number1column - 1
    number2position=(number2row-1)*9 + number2column - 1
            
    if number1position>number2position:
        firstposition=number2position
        secondposition=number1position
    else:
        firstposition=number1position
        secondposition=number2position
    value=firstposition+1
    while value<secondposition:
        if gameboard[value]==0:
            value=value+1
            flag=True
        else:
            flag=False
            break
    return (flag)


def checksamecolumn(gameboard, number1row, number1column, number2row, number2column):
    flag=True
    number1position=(number1row-1)*9 + number1column - 1
    number2position=(number2row-1)*9 + number2column - 1
            
    if number1position>number2position:
        firstposition=number2position
        secondposition=number1position
    else:
        firstposition=number1position
        secondposition=number2position
    value=firstposition+9
    while value<secondposition:
        if gameboard[value]==0:
            value=value+9
            flag=True
        else:
            flag=False
            break
    return (flag)

def checksamediagonalleft(gameboard, number1row, number1column, number2row, number2column):
    flag=False
    number1position=(number1row-1)*9 + number1column - 1
    number2position=(number2row-1)*9 + number2column - 1
            
    if number1position>number2position:
        firstposition=number2position
        secondposition=number1position
    else:
        firstposition=number1position
        secondposition=number2position
    if firstposition%9==0:
                value=firstposition+17
    else:
                value=firstposition+8
    while value<secondposition:
        if gameboard[value]==0:
            if value%9==0:
                value=value+17
            else:
                value=value+8
        else:
            return False
    if value==secondposition:
        return True
    return False

def checksamediagonalright(gameboard, number1row, number1column, number2row, number2column):
    flag=False
    number1position=(number1row-1)*9 + number1column - 1
    number2position=(number2row-1)*9 + number2column - 1
            
    if number1position>number2position:
        firstposition=number2position
        secondposition=number1position
    else:
        firstposition=number1position
        secondposition=number2position
    if firstposition%9==8:
        value=firstposition+1
    else:
        value=firstposition+10
    while value<secondposition:
        if gameboard[value]==0:
            if(value%9==8):
                value=value+1
            else:
                value=value+10
        else:
            return False
            
    if value==secondposition:
        return True
    return False


def cleangameboard(mygameboard):
    emptylinenumber=-1
    for x in range(int((len(mygameboard))/9)):
        sumtotal=0
        for y in range(0,9):
            sumtotal=sumtotal+mygameboard[x*9+y]
        if sumtotal==0:
            emptylinenumber= x
    return emptylinenumber



def findrow(position):
    row=(position//9)+1
    return row

def findcolumn(position):
    column=(position%9)+1
    return column

def hintcheck(mygameboard):
    hintnumbers=[]
    for number1 in range(len(mygameboard)):
        for number2 in range(number1+1,len(mygameboard)):
            if check(mygameboard,findrow(number1),findcolumn(number1),findrow(number2),findcolumn(number2)):
                hintnumbers=[number1, number2]
                return(hintnumbers)
    return(hintnumbers)


'''
mygameboard = gameboardinit()

print(cleangameboard(mygameboard))

printgameboard(mygameboard)
stop=False
while stop == False:
    number1row=int(input("Input first number row"))
    number1column=int(input("Input first number column"))

    number1=findnumber(mygameboard, number1row, number1column)
    
    
    number2row=int(input("Input second number row"))
    number2column=int(input("Input second number column"))
    
    number2=findnumber(mygameboard, number2row, number2column)

    if check(mygameboard, number1row, number1column, number2row, number2column)==True:
        mygameboard[(number1row-1)*9 + number1column - 1]=0
        mygameboard[(number2row-1)*9 + number2column - 1]=0
    
    
    
    
    mygameboard=deletelines(mygameboard,cleangameboard(mygameboard));
    mygameboard=deletelines(mygameboard,cleangameboard(mygameboard));
    
    printgameboard(mygameboard);
    k=input("Do you want to continue? Click x to stop, click anything else to continue.")
    if k=="x":
        stop=True

'''
