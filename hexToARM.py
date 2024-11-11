
from capstone import *

# Initialize Capstone disassembler
md = Cs(CS_ARCH_ARM, CS_MODE_ARM)

hex_string = input("Enter hex: ")
# Store hexadecimal strings to convert


# Convert hex to bytes
code_bytes = bytes.fromhex(hex_string)

# Disassemble each instruction
for i in md.disasm(code_bytes, 0x1000):
    print(f"0x{i.address:x}:\t{i.mnemonic}\t{i.op_str}")