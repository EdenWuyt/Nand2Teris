import asm_parser as parser
import hack_code as code
import symbol_table as symbol
import sys

# read the file
file = sys.argv[1]
name = file.split('.')[0]

# cleaning and adding labels to symbol table
line_list = parser.cleaning(file)
symbol.add_labels(line_list)

output_list = []
for line in line_list:
    if line.startswith('('):            # label
        pass
    elif line.startswith('@'):          # a commands
        addr = parser.addr(line)
        if not addr.isdigit():
            addr = symbol.find_symbol(addr)
        addr_binary = code.addr(int(addr))
        output_list.append('0' + addr_binary)
    else:                               # c commands
        jump = parser.jump(line)
        dest = parser.dest(line)
        comp = parser.comp(line)
        jump_binary = code.jump(jump)
        dest_binary = code.dest(dest)
        comp_binary = code.comp(comp)
        output_list.append('111' + comp_binary + dest_binary + jump_binary)

with open(name+'_result.hack', 'w') as f:
    for i in range(len(output_list)):
        f.write(output_list[i])
        if i != len(output_list) - 1:
            f.write('\n')
