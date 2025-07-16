def cleaning(file):             # remove comments and empty lines
    file_list = []
    with open(file) as f:
        for line in f:
            trim_f_with_no_comment = line.split('//')[0].strip()
            if trim_f_with_no_comment != '':
                file_list.append(trim_f_with_no_comment)
    return file_list


def addr(command):
    return command.split('@')[1]


def jump(command):
    jump = ''
    splited_by_semi_colon = command.split(';')
    if len(splited_by_semi_colon) > 1:
        jump = splited_by_semi_colon[1]
    return jump


def dest(command):
    dest = ''
    splited_by_equal_sign = command.split('=')
    if len(splited_by_equal_sign) > 1:
        dest = splited_by_equal_sign[0]
    return dest


def comp(command):
    comp = ''
    splited_by_equal_sign = command.split('=')
    if len(splited_by_equal_sign) == 1:
        comp = splited_by_equal_sign[0].split(';')[0]
    else:
        comp = splited_by_equal_sign[1].split(';')[0]
    return comp
