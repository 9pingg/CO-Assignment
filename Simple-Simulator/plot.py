from sys import stdin, stdout, exit
import regval
import matplotlib.pyplot as plt

# memoryDump(memoryDumparr)

# x_axis = []
# for i in range(0, len(y_axis)):
#     x_axis.append(i)


# plt.scatter(x_axis, y_axis)
# plt.show()    

## TYPE A ##

def add(line):
    line = line[2:]
    temp = []
    for i in range(3):
        temp.append(line[0:3])
        line = line[3:]
    line = temp        
    temp = int(regval.regvals[line[1]], 2) + int(regval.regvals[line[2]],2)
    if (temp>(2**16-1)):
        flg["V"] = 1
        temp = temp // 2**16
    temp = bin(temp)
    regval.regvals[line[0]] = temp[2:].zfill(16)

def sub(line):
    line = line[2:]
    temp = []
    for i in range(3):
        temp.append(line[0:3])
        line = line[3:]
    line = temp    
    temp = int(regval.regvals[line[1]], 2) - int(regval.regvals[line[2]],2)
    if (temp<0):
    #overflow
        flg["V"] = 1
        temp = 0
    temp = bin(temp)
    regval.regvals[line[0]] = temp[2:].zfill(16)

def mul(line):
    line = line[2:]
    temp = []
    for i in range(3):
        temp.append(line[0:3])
        line = line[3:]
    line = temp
    temp = int(regval.regvals[line[1]], 2) * int(regval.regvals[line[2]],2)
    if (temp > 2**16-1):
        flg["V"] = 1
        flg["L"] = 0
        flg["G"] = 0
        flg["E"] = 0
        temp = temp // 2**16
    temp = bin(temp)
    regval.regvals[line[0]] = temp[2:].zfill(16)
    
def xor(line):
    line = line[2:]
    temp = []
    for i in range(3):
        temp.append(line[0:3])
        line = line[3:]

    line = temp
    temp = int(regval.regvals[line[1]], 2) ^ int(regval.regvals[line[2]],2)
    temp = bin(temp)
    regval.regvals[line[0]] = temp[2:].zfill(16)

def funcOR(line):
    line = line[2:]
    temp = []
    for i in range(3):
        temp.append(line[0:3])
        line = line[3:]

    line = temp
    temp = int(regval.regvals[line[1]], 2) | int(regval.regvals[line[2]],2)
    temp = bin(temp)
    regval.regvals[line[0]] = temp[2:].zfill(16)
    

def funcAND(line):
    line = line[2:]
    temp = []
    for i in range(3):
        temp.append(line[0:3])
        line = line[3:]
    line = temp
    temp = int(regval.regvals[line[1]], 2) & int(regval.regvals[line[2]],2)
    temp = bin(temp)
    regval.regvals[line[0]] = temp[2:].zfill(16)


## TYPE B ##

def mov(line):
    temp = [] 
    temp.append(line[0:3])
    line = line[3:]
    temp.append(line)
    line = temp
    imm = line[1]

    regval.regvals[line[0]] = imm.zfill(16)

def ls(line):

    temp = [] 
    temp.append(line[0:3])
    line = line[3:]
    temp.append(line)
    line = temp
    imm = line[1]

    regvalue = regval.regvals[line[0]]
    regvalue = int(regvalue, 2)
    imm = int(imm, 2)
    regvalue = regvalue<<imm 
    regvalue = bin(regvalue)
    regval.regvals[line[0]] = regvalue[2:].zfill(16)    


def rs(line):

    temp = [] 
    temp.append(line[0:3])
    line = line[3:]
    temp.append(line)
    line = temp
    imm = line[1]

    regvalue = regval.regvals[line[0]]
    imm = int(imm, 2)
    regvalue = int(regvalue, 2)
    regvalue = regvalue>>imm 
    regvalue = bin(regvalue)[2:]
    regval.regvals[line[0]] = regvalue.zfill(16)  


def cmp(line):
    temp = []
    line = line[5:]
    for i in range(2):
        temp.append(line[0:3])
        line = line[3:]
    line = temp    

    if int(regval.regvals[line[0]], 2) > int(regval.regvals[line[1]],2) :
        #g
        flg["G"] = 1
        flg["L"] = 0
        flg["V"] = 0
        flg["E"] = 0

    elif int(regval.regvals[line[0]], 2) < int(regval.regvals[line[1]],2) :
        #l
        flg["L"] = 1
        flg["G"] = 0
        flg["V"] = 0
        flg["E"] = 0

        
    elif int(regval.regvals[line[0]], 2) == int(regval.regvals[line[1]],2):
        #equal     
        flg["E"] = 1
        flg["L"] = 0
        flg["G"] = 0
        flg["V"] = 0

    temp = "0"*12
    temp += str(flg["V"])
    temp += str(flg["L"])
    temp += str(flg["G"])
    temp += str(flg["E"])
    regval.regvals["111"] = temp

def funcNOT(line):

    temp = []
    line = line[5:]
    for i in range(2):
        temp.append(line[0:3])
        line = line[3:]
    line = temp

    temp = ""
    for i in line[1]:
        if i=='0':
            temp+='1'
        else:
            temp+='0'
    regval.regvals[line[0]] = temp

def move(line):
    
    temp = []
    line = line[5:]
    for i in range(2):
        temp.append(line[0:3])
        line = line[3:]
    line = temp

    regval.regvals[line[0]] = regval.regvals[line[1]]   

def div(line):

    temp = []
    line = line[5:]
    for i in range(2):
        temp.append(line[0:3])
        line = line[3:]
    line = temp 

    quo = int(regval.regvals[line[1]], 2) / int(regval.regvals[line[2]],2)
    modr1 = int(regval.regvals[line[1]], 2) % int(regval.regvals[line[2]],2)
    # modr1 = int(regval.regvals[line[1]], 2) % int(regval.regvals[line[2]],2)
    quo = bin(quo)
    modr1 = bin(modr1)

    regval.regvals["000"] = quo[2:].zfill(16)
    regval.regvals["001"] = modr1[2:].zfill(16)

def ld(line):
    
    temp = []
    temp.append(line[0:3])
    line = line[3:]
    temp.append(line)
    line = temp
    
    varname = line[1]
    if(varname in vardic):

        valueval = vardic[varname]
        binvalue = bin(valueval)
        binvalue = binvalue[2:]
        binvalue = binvalue.zfill(16)
        regval.regvals[line[0]] = binvalue
    
    # else:
    #     # Error
    #     if(varname in labeldic):
    #         print(f"Misuse of labels as variables error at line {lineno}")
    #         exit()
    #     print(f"Use of undefined variables error at line {lineno}")
    #     exit()
        
def st(line):
    
    temp = []
    temp.append(line[0:3])
    line = line[3:]
    temp.append(line)
    line = temp
    varname = line[1]
    if(varname not in vardic):
        vardic[varname] = regval.regvals[line[0]]
    else:
        vardic[varname] = regval.regvals[line[0]]

    # 0000000001 --> value = 00430974981648911

def jmp(line):
    global pc
    pc = int(line[3:] , 2)


def jlt(line):
    global pc
    if flg["L"] == 1 :
        pc = int(line[3:] , 2)
    else:
        pc = pc + 1   
def jgt(line):
    global pc
    if flg["G"] == 1 :
        pc = int(line[3:] , 2)
    else:
        pc = pc + 1    

def je(line):
    global pc
    if flg["E"] == 1 :
        pc = int(line[3:] , 2)
    else:
        pc = pc + 1      
def flagReset():
    flg["V"] = 0   
    flg["L"] = 0
    flg["G"] = 0
    flg["E"] = 0
    regval.regvals["111"] = "0"*16
    
def memoryDump(alllines):
    length = len(alllines)
    for i in range(length):
        print(alllines[i])
    varvals = vardic.values()
    for vals in varvals:
        print(vals)
    for i in range(256 - length - len(varvals)):
        print("0000000000000000")
        
flg = {"V":0,
        "L": 0,
        "G" :0,
        "E": 0
        }  


vardic = {}
alllines = []

for line in stdin:

    line = line.split()
    if line == []:
        break
    
    line = line[0]
    line = str(line)
    alllines.append(line)
pc = 0
y_axis = []

# for line in alllines:
memoryDumparr = []
while pc < len(alllines):
    y_axis.append(pc)
    opcode = alllines[pc][0:5:1]
    line = alllines[pc][5:]
    memoryDumparr.append(alllines[pc])
    if (opcode == "00000"):
        flagReset()
        add(line)
        pc = pc + 1
     
    elif (opcode == "00001"):
        flagReset()
        sub(line)
        pc = pc + 1

    elif (opcode == "00010"):
        flagReset()
        mov(line)
        pc = pc + 1
    elif (opcode == "00011"):
        move(line)
        flagReset()
        pc = pc + 1
    elif (opcode == "00100"):
        flagReset()
        ld(line) 
        pc = pc + 1
    elif (opcode == "00101"):
        flagReset()
        st(line)
        pc = pc + 1
    elif (opcode == "00110"):
        flagReset()
        mul(line)
        pc = pc + 1
    elif (opcode == "00111"):
        flagReset()
        div(line)
        pc = pc + 1
    elif (opcode == "01000"):
        flagReset()
        rs(line)
        pc = pc + 1
    elif (opcode == "01001"):
        flagReset()
        ls(line)
        pc = pc + 1
    elif (opcode == "01010"):
        flagReset()
        xor(line)
        pc = pc + 1
    elif (opcode == "01011"):
        flagReset()
        funcOR(line)
        pc = pc + 1
    elif (opcode == "01100"):
        flagReset()
        funcAND(line)
        pc = pc + 1
    elif (opcode == "01101"):
        flagReset()
        funcNOT(line)
        pc = pc + 1
        
    elif (opcode == "01110"):
        cmp(line)    
        pc = pc + 1

    elif (opcode == "01111"):
        temppc = pc
        jmp(line)
        flagReset()

        print(bin(temppc)[2:].zfill(8), end = " ")
        regValues = regval.regvals.values()
        for values in regValues:
            print(values, end = " ")
        print()
        continue
    elif (opcode == "10000"):
        temppc = pc
        jlt(line)
        flagReset()

        print(bin(temppc)[2:].zfill(8), end = " ")
        regValues = regval.regvals.values()
        for values in regValues:
            print(values, end = " ")
        print()
        continue
    elif (opcode == "10001"):
        temppc = pc

        jgt(line)
        flagReset()

        print(bin(temppc)[2:].zfill(8), end = " ")
        regValues = regval.regvals.values()
        for values in regValues:
            print(values, end = " ")
        print()
        continue

    elif (opcode == "10010"):

        temppc = pc
        je(line)
        flagReset()
        print(bin(temppc)[2:].zfill(8), end = " ")
        regValues = regval.regvals.values()
        for values in regValues:
            print(values, end = " ")
        print()
        continue

    elif (opcode == "10011"):
        pc = pc +1
        print(bin(pc-1)[2:].zfill(8), end = " ")
        regValues = regval.regvals.values()
        for values in regValues:
            print(values, end = " ")
        print()
        break

    print(bin(pc-1)[2:].zfill(8), end = " ")
    regValues = regval.regvals.values()
    for values in regValues:
        print(values, end = " ")
    print()

memoryDump(memoryDumparr)
x_axis = []
for i in range(0, len(y_axis)):
    x_axis.append(i)

plt.scatter(x_axis, y_axis)
plt.xlabel("Cycle Number")
plt.ylabel("Memory Address")
plt.show()    

