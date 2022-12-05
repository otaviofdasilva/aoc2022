from io import StringIO
from itertools import islice, repeat


def topo_pilhas_9001(input):
    it = StringIO(input) if type(input) == str else input

    stack = _empilha(it)

    for m in it:
        _move_9001(stack, *_parse(m))

    return "".join(_peek(stack, i)[0] for i in range(len(stack[-1])))


def topo_pilhas(input):
    it = StringIO(input) if type(input) == str else input

    stack = _empilha(it)

    for m in it:
        _move_9000(stack, *_parse(m))

    return "".join(_peek(stack, i)[0] for i in range(len(stack[-1])))


def _print_stack(stack):
    for i in range(len(stack)):
        print(stack[i])


def _parse(i):
    return tuple(map(int, islice(i[:-1].split(" "), 1, None, 2)))


def _empilha(it):
    stack = []
    for i in it:
        l = i[:-1]
        if l:
            t = islice(l, 1, None, 4)
            stack.append(list(t))
        else:
            break

    return stack


def _pop(stack, col, n=0):

    if n:
        vs = []
        while n:
            v, i = _peek(stack, col)
            stack[i][col] = " "
            vs.insert(0, v)
            n -= 1

        return vs

    else:
        v, i = _peek(stack, col)
        stack[i][col] = " "
        return v


def _push(stack, vs, col):
    if type(vs) == int:
        _, i = _peek(stack, col)
        if not i:
            stack.insert(0, list(repeat(" ", len(stack[-1]))))
            i += 1

        stack[i - 1][col] = vs
    else:
        for v in vs:
            _, i = _peek(stack, col)

            if not i:
                stack.insert(0, list(repeat(" ", len(stack[-1]))))
                i += 1

            stack[i - 1][col] = v


def _peek(stack, col):
    i = 0
    while not stack[i][col].strip() and i < len(stack):
        i += 1

    return stack[i][col], i


def _move_9000(stack, quantidade, origem, destino):

    while quantidade:
        v = _pop(stack, origem - 1)
        _push(stack, v, destino - 1)
        quantidade -= 1

    return stack


def _move_9001(stack, quantidade, origem, destino):
    vs = _pop(stack, origem - 1, quantidade)
    _push(stack, vs, destino - 1)

    return stack
