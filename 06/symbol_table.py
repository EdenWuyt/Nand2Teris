variable_addr = 16      # variable is stored from address 16 in RAM
symbol_table = {
    'R0': 0,
    'R1': 1,
    'R2': 2,
    'R3': 3,
    'R4': 4,
    'R5': 5,
    'R6': 6,
    'R7': 7,
    'R8': 8,
    'R9': 9,
    'R10': 10,
    'R11': 11,
    'R12': 12,
    'R13': 13,
    'R14': 14,
    'R15': 15,
    'SCREEN': 16384,
    'KBD': 24576,
    'SP': 0,
    'LCL': 1,
    'ARG': 2,
    'THIS': 3,
    'THAT': 4
}


def add_labels(line_list):    # line_list obtained after cleaning
    line_num = 0
    for line in line_list:
        if line.startswith('('):
            label = line.split('(')[1].split(')')[0]
            symbol_table[label] = line_num
        else:
            line_num += 1


def find_symbol(name):
    global variable_addr
    if name not in symbol_table:
        symbol_table[name] = variable_addr
        addr = variable_addr
        variable_addr += 1
    else:
        addr = symbol_table[name]
    return addr
