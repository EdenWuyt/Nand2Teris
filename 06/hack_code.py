def binary(dec, bits):    # turn dec into n bits binary code
    result = []
    times = bits - 1
    divider = pow(2, (bits-1))
    for _ in range(times):
        result.append(str(dec // divider))
        dec = dec % divider
        divider = divider // 2
        if divider == 1:
            result.append(str(dec))
    return ''.join(result)


def addr(dec):
    return binary(dec, 15)


def jump(jump):
    jump_table = {
        '': '000',
        'JGT': '001',
        'JEQ': '010',
        'JGE': '011',
        'JLT': '100',
        'JNE': '101',
        'JLE': '110',
        'JMP': '111'
    }
    if jump not in jump_table:
        raise ValueError('No such jump!')
    else:
        return jump_table[jump]


def dest(dest):
    dest_table = {
        '': '000',
        'M': '001',
        'D': '010',
        'MD': '011',
        'A': '100',
        'AM': '101',
        'AD': '110',
        'AMD': '111'
    }
    if dest not in dest_table:
        raise ValueError('No such dest!')
    else:
        return dest_table[dest]


def comp(comp):
    if 'M' in comp:
        first_code = '1'
    else:
        first_code = '0'
    comp_table = {
        '0': '101010',
        '1': '111111',
        '-1': '111010',
        'D': '001100',
        'A': '110000',
        'M': '110000',
        '!D': '001101',
        '!A': '110001',
        '!M': '110001',
        '-D': '001111',
        '-A': '110011',
        '-M': '110011',
        'D+1': '011111',
        'A+1': '110111',
        'M+1': '110111',
        'D-1': '001110',
        'A-1': '110010',
        'M-1': '110010',
        'D+A': '000010',
        'D+M': '000010',
        'D-A': '010011',
        'D-M': '010011',
        'A-D': '000111',
        'M-D': '000111',
        'D&A': '000000',
        'D&M': '000000',
        'D|A': '010101',
        'D|M': '010101'
    }
    if comp not in comp_table:
        raise ValueError('No such comp!')
    else:
        return first_code + comp_table[comp]
