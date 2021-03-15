#Question 1
def somme(a,b):
  return a+b

print(somme(1,1))

#Question 2
def somme3(a,b,c):
  return a+b+c

print(somme3(1,1,1))

#Question 3
valeur = 1,2
kw_valeurs = {'b':1}
kw_valeurs2 = {'a':1}
kw_valeurs3 = {'c':1}

print(somme3(**kw_valeurs3, **kw_valeurs, **kw_valeurs2))

#Quesion 3.1
def puiss(a,b):
  valeurs = a, b
  l = [x[0]**x[1] for x in valeurs]
  return l

valeurs = [[2,3], [3,3]]

print(puiss(*valeurs))

#Question 4
l= []

maliste = []
maliste.append(4)
print(maliste)

def append_chaine(l, autre) :
    str(autre)
    l = []
    l.append(autre)
    return l

print(append_chaine(maliste, 'v'))


