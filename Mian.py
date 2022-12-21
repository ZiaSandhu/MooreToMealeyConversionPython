from numpy import * 
def Input_States():
    state=input("Enter Total States separated by comma:")
    state=state.split(',')
    [state.pop(state.index(i)) for i in state if i == '']
    state=set(state)
    state=list(state)
    state.sort()
    # print(state)
    return state
def Input_Symbols():
    symbol=input("Enter Total Symbols separated by comma:")
    symbol=symbol.split(',')
    [symbol.pop(symbol.index(i)) for i in symbol if i == '']
    symbol=set(symbol)
    symbol=list(symbol)
    symbol.sort()
    # print(symbol)
    return symbol
def Set_Final_Initial():
    while True:
        init=input("Select initial state from :"+str(states))
        if init not in states:
            print("Not Valid Input!")
        else:
            break
    while True:
        flag=False
        final=input("Enter final states seperated by comma from :"+str(states))
        # print(type(final))
        if len(final) == 1:
            if final not in states:
                print("Invalid Input")
                continue
        else:
            final=final.split(',')
            [final.pop(final.index(i)) for i in final if i == '']
            for i in final:
                if i not in states:
                    print("Invalid Input")
                    flag=True
                    break
            if flag:
                continue
        final=set(final)
        final=list(final)
        break
    # print(final)
    Terminal=[init]
    Terminal.extend(final)
    return Terminal
def Initlize_Table():
    global rows
    rows=len(states)+1
    global col
    col=len(symbols)+2
    TransTable=[[' ']*col for i in range(rows)]
    TransTable[0][0]='States'
    TransTable[0][len(symbols)+1]="Output"
    for i in range(0,len(states)):
        TransTable[i+1][0]=states[i]
    for i in range(0,len(symbols)):
        TransTable[0][i+1]=symbols[i]
    for j in range(1,rows):
        i=TransTable[j][0]
        if i in Terminal[0]:
            TransTable[j][0]='->'+TransTable[j][0]
        elif i in Terminal[1:]:
            TransTable[j][0]='*'+TransTable[j][0]        
    return TransTable
def Input_Transitions():
    for i in range(1,rows):
        for j in range(1,col-1):
            q=input("\u03B4("+TransTable[i][0]+ ',' +TransTable[0][j]+')')
            while q not in states:
                q=input("\u03B4("+TransTable[i][0]+ ',' +TransTable[0][j]+')')
            TransTable[i][j]=q
            print(reshape(TransTable,(rows,col)))
def Input_OutPut():
    for j in range(1,rows):
        out=input("Enter Output for \u03BB("+ TransTable[j][0]+')')
        TransTable[j][col-1]=out
        print(reshape(TransTable,(rows,col)))

        
def MooreToMealey():
    pass

states=Input_States()
symbols=Input_Symbols()
Terminal=Set_Final_Initial()
TransTable=Initlize_Table()
print(reshape(TransTable,(rows,col)))
print("Lets Fill Transition Table")
Input_Transitions()
Input_OutPut()

MooreToMealey()