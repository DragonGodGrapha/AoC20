import re

class Calc(int):
    def __mul__(self,im):
        return Calc(int(self)*im)
    def __truediv__(self,im):
        return Calc(int(self)+im)
    def __sub__(self,im):
        return Calc(int(self)*im)
        

def evalA(exp):
    exp = re.sub(r"(\d+)", r"Calc(\1)", exp)
    exp = exp.replace("+", "/")
    return eval(exp,{},{"Calc":Calc})

def evalB(exp):
    exp = re.sub(r"(\d+)", r"Calc(\1)", exp)
    exp = exp.replace("+", "/")
    exp = exp.replace("*", "-")
    return eval(exp,{},{"Calc":Calc})

with open('18.txt') as data:
    data=data.read().splitlines()
    
#Part A

print(f'Part A: {sum(evalA(l) for l in data)}')
print(f'Part B: {sum(evalB(l) for l in data)}')