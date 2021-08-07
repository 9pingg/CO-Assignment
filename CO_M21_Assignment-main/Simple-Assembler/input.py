import  OpcodeTable
from sys import stdin

# line = add r1 r2 r3
ans = ""
def findOpcode(line):
    global ans
    list = line.split(' ')
    if(list[0] in OpcodeTable.opcodes):
        ans = ans + OpcodeTable.opcodes[list[0]][0]
    elif(list[1] in OpcodeTable.opcodes):
        ans = ans + OpcodeTable.opcodes[list[1]][0]

for line in stdin:
    if line == '': # If empty string is read then stop the loop
        break
    findOpcode(line) # perform some operation(s) on given string





