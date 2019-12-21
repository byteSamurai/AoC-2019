#!/usr/bin/python3.7

import numpy

lines = [line for line in open('input.txt')]
#test
lines.append("3,9,8,9,10,9,4,9,99,-1,8")  # input == 8
lines.append("3,3,1108,-1,8,3,4,3,99")  # input == 8
lines.append("3,9,7,9,10,9,4,9,99,-1,8")  # input < 8
lines.append("3,3,1107,-1,8,3,4,3,99")  # input < 8
lines.append("3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9")  # print 0 on zero or 1 on non-zero
lines.append("3,3,1105,-1,9,1101,0,0,12,4,12,99,1")  # print 0 on zero or 1 on non-zero
# 999 -> <8, 1000 -> ==8, 1001 -> >8
lines.append("3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,"
             "999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99")

prog = lines[0].split(',')
prog = numpy.array(list(map(int, prog)))


def instr_len(op_code: int):
    if op_code > 99:
        rev_param = str(op_code).zfill(5)[::-1]
        op_code = int(rev_param[1] + rev_param[0])

    return {
        1: 4,
        2: 4,
        3: 2,
        4: 2,
        5: 3,
        6: 3,
        7: 4,
        8: 4
    }.get(op_code)


def resolve_parameter_mode(prog: list, param: int, *args):
    if param < 100:
        nested_params = [prog[a:a + 1] for a in args]
        return [param, *nested_params]

    rev_param = str(param).zfill(5)[::-1]
    op_code = int(rev_param[1] + rev_param[0])
    arg_param = list(rev_param[2:])
    resolved_params = []
    args = list(args)
    if args:
        for i, is_immediate in enumerate(arg_param):
            if bool(int(is_immediate)):
                resolved_params.append([args[i]])
            elif len(args) > i:
                resolved_params.append(prog[args[i]:args[i] + 1])

    return [op_code, *resolved_params]


def operate(wp: int, ops_code: int, *args, ) -> int:
    if ops_code == 1:
        args[2][0] = args[0][0] + args[1][0]
    elif ops_code == 2:
        args[2][0] = args[0][0] * args[1][0]
    elif ops_code == 3:
        args[0][0] = int(input("Enter input args: "))
        # args[0][0] = 1
    elif ops_code == 4:
        print(args[0][0])
    elif ops_code == 5:
        if args[0][0] != 0:
            return args[1][0]
    elif ops_code == 6:
        if args[0][0] == 0:
            return args[1][0]
    elif ops_code == 7:
        args[2][0] = 1 if args[0][0] < args[1][0] else 0
    elif ops_code == 8:
        args[2][0] = 1 if args[0][0] == args[1][0] else 0

    return wp + instr_len(ops_code)


def process(_prog):
    wp = 0
    p = _prog.copy()

    while True:
        op_code = p[wp]
        if op_code == 99:
            break

        op_len = instr_len(p[wp])

        instruction = p[wp:op_len + wp]
        resolved_instruction = resolve_parameter_mode(p, *instruction)

        wp = operate(wp, *resolved_instruction)

        if wp > len(p):
            break


# 6627023

process(prog)

# for i in range(0, 99):
#    for j in range(0, 99):
#        if process(prog, i, j) == 19690720:
#            print(f"found it:{i},{j}")
#            sys.exit()
