from egzP6btesty import runtests


def jump(M):
    x, y = 0, 0
    field_set = {}
    field_set.update({(f"({x}, {y}"): (x, y)})
    for move in M:
        if move == "UL":
            x, y = x - 1, y + 2
        elif move == "UR":
            x, y = x + 1, y + 2
        elif move == "RU":
            x, y = x + 2, y + 1
        elif move == "RD":
            x, y = x + 2, y - 1
        elif move == "DR":
            x, y = x + 1, y - 2
        elif move == "DL":
            x, y = x - 1, y - 2
        elif move == "LD":
            x, y = x - 2, y - 1
        elif move == "LU":
            x, y = x - 2, y + 1
        temp = field_set.get(f"({x}, {y})")
        if temp:
            field_set.pop((f"({x}, {y})"))
        else:
            field_set.update({f"({x}, {y})": (x, y)})
    return len(field_set)


runtests(jump, all_tests=True)
