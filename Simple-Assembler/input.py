import  OpcodeTable
import Registers
from sys import stdin,stdout, exit
import regval

lineno = 0 
def findOpcode(list_line):
    global ans
    global flg
    global lineno
    
    if(list_line[0][-1] == ':'):
        if (list_line[1] not in OpcodeTable.opcodes):
            print(f"Syntax Error: Invalid instruction detected, found at line {lineno}")
            exit()
    else:
        if (list_line[0] not in OpcodeTable.opcodes):
            print(f"Syntax Error: Invalid instruction detected, found at line {lineno}")
            exit()            
    if(list_line[0][-1] == ':'):
        # label
        if(list_line[1] in OpcodeTable.opcodes):
            if(list_line[1] == 'mov'):
                if('$' in list_line[2]):
                    list_line[1] = "mov"    
                else:
                    list_line[1] = "move" 
            ans = ans + OpcodeTable.opcodes[list_line[1]][0]
            typ = OpcodeTable.opcodes[list_line[1]][1]
            list_line = list_line[2:]

        if(typ) == "A":

            typeA(list_line)
            if(list_line[1] == "add"):
                add(list_line)
            elif(list_line[1] == "sub"):
                sub(list_line)
            elif(list_line[1] == "mul"):
                mul(list_line)
            elif(list_line[1] == "xor"):
                xor(list_line)
            elif(list_line[1] == "or"):
                funcor(list_line)
            elif(list_line[1] == "and"):
                funcand(list_line)

        elif(typ) == "B":
            typeB(list_line)
            if(list_line[1] == "mov"):
                mov(list_line)
            elif(list_line[1] == "rs"):
                rs(list_line)
            elif(list_line[1] == "ls"):
                ls(list_line)
        elif(typ) == "C":

            if(list_line[1] == "not"):
                funcnot(list_line)
            elif(list_line[1] == "cmp"):
                cmp(list_line)
            elif(list_line[1] == "div"):
                div(list_line)
            elif(list_line[1] == "move"):
                move(list_line)
            typeC(list_line)
        elif(typ) == "D":
            typeD(list_line)
        elif(typ) == "E":
            typeE(list_line)
        elif(typ) == "F":
            typeF(list_line)  

          

    elif(list_line[0] in OpcodeTable.opcodes):
        if(list_line[0] == 'mov'):
            if('$' in list_line[2]):
                list_line[0] = "mov"    
            else:
                list_line[0] = "move"        
        ans = ans + OpcodeTable.opcodes[list_line[0]][0]
        typ = OpcodeTable.opcodes[list_line[0]][1]
        list_line = list_line[1:]
        if(typ) == "A":
            
            if(list_line[1] == "add"):
                add(list_line)
            elif(list_line[1] == "sub"):
                sub(list_line)
            elif(list_line[1] == "mul"):
                mul(list_line)
            elif(list_line[1] == "xor"):
                xor(list_line)
            elif(list_line[1] == "or"):
                funcor(list_line)
            elif(list_line[1] == "and"):
                funcand(list_line)
            typeA(list_line)

        elif(typ) == "B":

            if(list_line[1] == "mov"):
                mov(list_line)
            elif(list_line[1] == "rs"):
                rs(list_line)
            elif(list_line[1] == "ls"):
                ls(list_line)
            typeB(list_line)

        elif(typ) == "C":

            if(list_line[1] == "not"):
                funcnot(list_line)
            elif(list_line[1] == "cmp"):
                cmp(list_line)
            elif(list_line[1] == "div"):
                div(list_line)
            elif(list_line[1] == "move"):
                move(list_line)    
            typeC(list_line)
        elif(typ) == "D":
            typeD(list_line)
        elif(typ) == "E":
            typeE(list_line)
        elif(typ) == "F":
            typeF(list_line)          
    else:
      print()
    flg = { 
        "V": 0,
        "L": 0,
        "G": 0,
        "E": 0
        }
    lineno += 1     

def add(line):
    temp = int(regval.regvals[line[1]], 2) + int(regval.regvals[line[2]],2)
    if (temp>(2**16-1)):
        flg["V"] = 1
        temp = temp // 2**16
    temp = bin(temp)
    regval.regvals[line[0]] = temp[2:].zfill(16)
    

def sub(line):
    temp = int(regval.regvals[line[1]], 2) - int(regval.regvals[line[2]],2)
    if (temp<0):
    #overflow
        flg["V"] = 1
        temp = 0
    temp = bin(temp)
    regval.regvals[line[0]] = temp[2:].zfill(16)


def mul(line):
    temp = int(regval.regvals[line[1]], 2) * int(regval.regvals[line[2]],2)
    if (temp > 2**16-1):
        flg["V"] = 1
        temp = temp // 2**16
    temp = bin(temp)
    regval.regvals[line[0]] = temp[2:].zfill(16)
    
def xor(line):
    temp = int(regval.regvals[line[1]], 2) ^ int(regval.regvals[line[2]],2)
    temp = bin(temp)
    regval.regvals[line[0]] = temp[2:].zfill(16)

def funcor(line):
    temp = int(regval.regvals[line[1]], 2) | int(regval.regvals[line[2]],2)
    temp = bin(temp)
    regval.regvals[line[0]] = temp[2:].zfill(16)
    

def funcand(line):
    temp = int(regval.regvals[line[1]], 2) & int(regval.regvals[line[2]],2)
    temp = bin(temp)
    regval.regvals[line[0]] = temp[2:].zfill(16)

## TYPE B##

def mov(line):

    imm = line[2][1:]
    regval.regvals[line[0]] = bin(int(imm)).zfill(16)
 
def ls(line):

    imm = line[2][1:]
    regvalue = regval.regvals[line[0]]
    regvalue = int(regvalue, 2)
    regvalue = regvalue<<imm 
    regvalue = bin(regvalue)
    regval.regvals[line[0]] = regvalue[2:].zfill(16)    

def rs(line):

    imm = line[2][1:]
    regvalue = regval.regvals[line[0]]
    regvalue = int(regvalue, 2)
    regvalue = regvalue>>imm 
    regvalue = bin(regvalue)[2:]
    regval.regvals[line[0]] = regvalue.zfill(16)  

#typeC

def cmp(line):
    for i in range (2):
        if (line[i]=='FLAGS'):
                print(f"Illegal use of FLAGS register at line {lineno}")
                exit()

    if int(regval.regvals[line[0]], 2) > int(regval.regvals[line[1]],2) :
        #g
        flg["G"] = 1
    elif int(regval.regvals[line[0]], 2) < int(regval.regvals[line[1]],2) :
        #l
        flg["L"] = 1
        
    elif int(regval.regvals[line[0]], 2) == int(regval.regvals[line[1]],2):
        #equal     
        flg["E"] = 1

    temp = "0"*12
    temp += flg["V"]
    temp += flg["L"]
    temp += flg["G"]
    temp += flg["E"]
    regval.regvals["FLAGS"] = temp

def funcnot(line):
    for i in range (2):
        if (line[i]=='FLAGS'):
                print(f"Illegal use of FLAGS register at line {lineno}")
                exit()
    temp = ""
    for i in line[1]:
        if i=='0':
            temp+='1'
        else:
            temp+='0'
    regval.regvals[line[0]] = temp

def move(line):
    if (line[0] == 'FLAGS'):
        exit()
    regval.regvals[line[0]] = regval.regvals[line[1]]   

def div(line):
    for i in range (2):
        if (line[i]=='FLAGS'):
                print(f"Illegal use of FLAGS register at line {lineno}")
                exit()
    quo = int(regval.regvals[line[1]], 2) / int(regval.regvals[line[2]],2)
    modr1 = int(regval.regvals[line[1]], 2) % int(regval.regvals[line[2]],2)
    modr1 = int(regval.regvals[line[1]], 2) % int(regval.regvals[line[2]],2)
    quo = bin(quo)
    modr1 = bin(modr1)
    regval.regvals["R0"] = quo[2:].zfill(16)
    regval.regvals["R1"] = modr1[2:].zfill(16)



def ld(line):
    varname = line[1]
    if(varname in vardic):
        ar = vardic[varname]
        binvalue = bin(ar)
        binvalue = binvalue[2:]
        binvalue = binvalue.zfill(16)
        regval.regvals[line[0]] = binvalue
    else:
        # Error
        if(varname in labeldic):
            print(f"Misuse of labels as variables error at line {lineno}")
            exit()
        print(f"Use of undefined variables error at line {lineno}")
        exit()
def st(line):
    varname = line[1]
    if(varname not in vardic):
         # Error
        if(varname in labeldic):
            print(f"Misuse of labels as variables error at line {lineno}")
            exit() 
        print(f"Use of undefined variables error at line {lineno}")
        exit()

def typeA(line):
    if (len(line)<3):
        print(f"Registers are not enough error at line {lineno}")
        exit()
    if (len(line)>3):
        print(f"Registers are more than enough error at line {lineno}")
        exit()
        
    global ans
    unused = "00"
    ans = ans + unused
    for i in range (3):
        if (line[i]=='FLAGS'):
            print(f"Illegal use of FLAGS register at line {lineno}")
            exit()
      
        if (line[i] not in Registers.Registers):
            print(f"Registers are not valid at line {lineno}")
            exit()

        ans += Registers.Registers[line[i]]

def typeB(line):
    if (len(line)<2 or len(line) > 2):
        print(f"tokens are not enough, error at line {lineno}")
        exit()
     
    global ans
    if (line[0]=='FLAGS'):
        print(f"Illegal use of FLAGS register at line {lineno}")
        exit()
    if(line[0] not in Registers.Registers):
        print(f"Registers not valid at line {lineno}")
        exit()
    if (line[0] in Registers.Registers):
        ans += Registers.Registers[line[0]]
    if(line[1][1:].isdigit() == False):
        print(f"Imm value not in appropriate range [0, 255], error at line {lineno}")  
        exit()
    if(int(line[1][1:]) > 255 or int(line[1][1:]) < 0):
        print(f"Imm value not in appropriate range [0, 255], error at line {lineno}")   
        exit() 
    binvalue = bin(int(line[1][1:]))
    binvalue = binvalue[2:]
    binvalue = binvalue.zfill(8)
    ans += str(binvalue)

def typeC(line):
  global ans
  unused = "00000"
  ans = ans + unused
  
  for i in range (2):
        if (line[i] not in Registers.Registers):
            print(f"Typos in register name error at line {lineno}")
            exit()
        ans += Registers.Registers[line[i]]



def typeD(line):
    global ans
    if (len(line)<2 or len(line)>2):
        print(f"Not valid operators at line {lineno}")
        exit()
    if (line[0]=='FLAGS'):
        print(f"Illegal use of FLAGS register at line {lineno}")
        exit()
    if (line[0] not in Registers.Registers):
            print(f"Typos in register name error at line {lineno}")
            exit()
    if (line[0] in Registers.Registers):
        ans += Registers.Registers[line[0]]

    varname = line[1]
    if (varname not in vardic):
        if(varname in labeldic):
            print(f"Misuse of labels as variables error at line {lineno}")
            exit()
        print(f"Use of undefined variables error at line {lineno}")
        exit()
        
    ar = vardic[varname]
    binvalue = bin(ar)
    binvalue = binvalue[2:]
    binvalue = binvalue.zfill(8)
    ans += str(binvalue) 

      
 
def typeE(line):
    #global vardic
    global ans
    unused = "0"*3
    ans = ans + unused
    #print(line)
    varname = line[0]
    if (varname not in labeldic):
        if(varname in vardic):
            print(f"Misuse of variables as labels error at line {lineno}")
            exit() 
        print(f" label is not defined {lineno}")
        exit()
    if(varname in labeldic):
        ar = labeldic[varname]
        binvalue = bin(ar)
        binvalue = binvalue[2:]
        binvalue = binvalue.zfill(8)
        ans += str(binvalue) 
        
        

def typeF(line):
    global ans
    unused = "0"*11
    ans = ans + unused
   
# for line in stdin:
#     pc = pc + 1
#     if line == '': # If empty string is read then stop the loop
#         break
#     findOpcode(line) # perform some operation(s) on given string

alllines = []
alllinesvar = []
flg = {"V":0,
        "L": 0,
        "G" :0,
        "E": 0
        }  

labelname = []
noofvars = 0
nooflabel = 0
pc = 0
typ = ""
ans = ""
varname = []
vardic = {}
labeldic = {}
noofinst = 0
allinst = []

for line in stdin:
    if line == "":
        continue
    line = line.split()
    if(line == []): 
        ###############################################
        continue
    if(line[0] == "var"):
        try:
            allinst.append(line)
            noofvars = noofvars + 1
            varname.append(line[1])
            noofinst += 1
            continue
        except:
            print(f"No variable name given error at line {pc}")
            exit()
    if(line[0][-1] == ':'):
        labelname.append(line[0][0:len(line[0])-1:1])
        labeldic[labelname[nooflabel]] = pc
        nooflabel += 1
    alllines.append(line)
    allinst.append(line)
    pc = pc + 1
    noofinst += 1

for i in range(noofvars):
    vardic[varname[i]] = pc + i 

# Checking Halt
hltpos = 0
for line in allinst[0:-1:1]:
    if (line[0] == "hlt"):
        print(f"Halt should not be anywhere except the last line, error at line {hltpos}")
        exit()
    try:    
        if(line[1] == "hlt"):
            print(f"Halt should not be anywhere except the last line, error at line {hltpos}")
            exit()
    except:
        print()
    hltpos += 1  

# halt at 
if (alllines[-1][-1] != 'hlt'):
    print("Missing hlt instruction")
    exit()



# Checking var

varpos15 = 0
for i in range(len(allinst)):
    if(i!=0):
        if(allinst[i][0]=='var' and allinst[i-1][0]!='var'):
            print(f'variable should be defined at the start {varpos15}')
            exit()
    varpos15 = varpos15 + 1

# Checking label

temp=[]
abcd = 0
for i in range(len(alllines)):
    if (alllines[i][0][-1]==':'):
        if (len(alllines[i])>=2):
            if (alllines[i][1][-1]==':'):
                print(f"General Syntax Error, error at line {abcd}")
                exit()
        if (alllines[i][0] not in temp):
            temp.append(alllines[i][0])
    
        else:
            print(f"General Syntax Error, error at line {abcd}")
            exit()
    abcd += 1

qwerty = 0
answer = []
for line in alllines:
    if(len(line) == 1):
        if(line[0] != "hlt"):
            print(f"General Syntax Error, error at line {qwerty}")
            exit()
    ans = ""
    findOpcode(line)
    answer.append(ans)
    qwerty += 1
    
    

for ans in answer:
    stdout.write(ans)
    stdout.write('\n')


