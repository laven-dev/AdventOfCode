import sys,sympy
with open(sys.argv[1] if len(sys.argv)>1 else "input.txt") as f: d=[x.split() for x in f.read().splitlines()]
td,tmp,s,g=[],[],0,0;[tmp.extend(l) if l!=[] else (td.extend(tuple(tmp)),tmp.clear()) for l in d]
def mm(data:list[str])->list[list]:
    ba,bb,t=[int(data[2][2:][:-1]),int(data[3][2:])],[int(data[6][2:][:-1]),int(data[7][2:])],[int(data[9][2:][:-1]),int(data[10][2:])]
    for _ in range(11):td.pop(0)
    return [ba,bb,t]
def slv(i:list[list[int]],rng:int)->int:
    a,b=sympy.symbols('a b',integer=True)
    xe,ye=sympy.Eq((i[0][0]*a)+(i[1][0]*b),i[2][0]+rng),sympy.Eq((i[0][1]*a)+(i[1][1]*b),i[2][1]+rng)
    r=sympy.solve([xe,ye],(a,b))
    return r[a]*3+r[b] if r else 0
while td:m=mm(td);s+=slv(m,0);g+=slv(m,int(1e13))
print(f"S: {s}, G: {g}")