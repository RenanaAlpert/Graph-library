parenthetical = {'(': ')', '[': ']', '{': '}'}


def is_correct(par_sen: str):
    global parenthetical

    par_need = ""
    for par in par_sen:
        if par in parenthetical.keys():
            par_need += parenthetical[par]
        else:
            if par != par_need[-1]:
                return False
            par_need = par_need[:-1]
    if par_need == "":
        return True
    return False


print("([]){[{}]()} is", is_correct("([]){[{}]()}"))
print("([]){[{]}()} is", is_correct("([]){[{]}()}"))
print("([]){[{]}() is", is_correct("([]){[{]}()"))
