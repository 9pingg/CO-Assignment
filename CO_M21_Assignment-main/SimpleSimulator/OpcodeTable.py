# opcode, Instruction Type, no fo ops, contains imm value or not
#  if contains then imm = 1
imm = 1
noimm = 0
opcodes = {
    
"00000": ("add", "A"),
"00001": ("sub", "A"),
"00010": ("mov", "B"),
"00011": ("move", "C",),
"00100": ("ld", "D"),
"00101": ("st", "D"),
"00110": ("mul", "A"),
"00111": ("div", "C"),
"01000": ("rs", "B"),
"01001": ("ls", "B"),
"01010": ("xor", "A"),
"01011": ("or", "A"),
"01100": ("and", "A"),
"01101": ("not", "C"),
"01110": ("cmp", "C"),
"01111": ("jmp", "E"),
"10000": ("jlt", "E"),
"10001": ("jgt", "E"),
"10010": ("je", "E"),
"10011": ("hlt", "F"),

}