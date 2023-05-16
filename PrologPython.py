name = list()
male = list()
def malef(X):
    if (X == 0): return male
    else: return X in male
male.append("Hagoromo")
name.append("Hagoromo")
male.append("Indra")
name.append("Indra")
male.append("Asura")
name.append("Asura")
male.append("Tajima")
name.append("Tajima")
male.append("Madara")
name.append("Madara")
male.append("Izuna")
name.append("Izuna")
male.append("Fugaku")
name.append("Fugaku")
male.append("Itachi")
name.append("Itachi")
male.append("Sasuke")
name.append("Sasuke")
male.append("Minato")
name.append("Minato")
male.append("Naruto")
name.append("Naruto")
male.append("Boruto")
name.append("Boruto")
female = list()
def femalef(X):
    if (X == 0): return female
    else: return X in female
female.append("Ozawa")
name.append("Ozawa")
female.append("Outdra")
name.append("Outdra")
female.append("Bsura")
name.append("Bsura")
female.append("Tanara")
name.append("Tanara")
female.append("Mikoto")
name.append("Mikoto")
female.append("Sakura")
name.append("Sakura")
female.append("Sarada")
name.append("Sarada")
female.append("Kushina")
name.append("Kushina")
female.append("Hinata")
name.append("Hinata")
female.append("Himawari")
name.append("Himawari")
parent = list()
def parentf(X, Y):
    if (X == 0 and Y == 0): return parent
    if (X == 0): 
        for k in parent:
            if (k[1] == Y): return k[0]
    if (Y == 0):
        for k in parent:
            if (k[0] == X): return k[1]
    return [X, Y] in parent
parent.append(["Hagoromo", "Indra"])
parent.append(["Hagoromo", "Asura"])
parent.append(["Ozawa", "Indra"])
parent.append(["Ozawa", "Asura"])
parent.append(["Indra", "Tajima"])
parent.append(["Indra", "Fugaku"])
parent.append(["Outdra", "Tajima"])
parent.append(["Outdra", "Fugaku"])
parent.append(["Tajima", "Madara"])
parent.append(["Tajima", "Izuna"])
parent.append(["Tanara", "Madara"])
parent.append(["Tanara", "Izuna"])
parent.append(["Fugaku", "Itachi"])
parent.append(["Fugaku", "Sasuke"])
parent.append(["Mikoto", "Itachi"])
parent.append(["Mikoto", "Sasuke"])
parent.append(["Sasuke", "Sarada"])
parent.append(["Sakura", "Sarada"])
parent.append(["Asura", "Minato"])
parent.append(["Bsura", "Minato"])
parent.append(["Kushina", "Naruto"])
parent.append(["Minato", "Naruto"])
parent.append(["Naruto", "Boruto"])
parent.append(["Naruto", "Himawari"])
parent.append(["Hinata", "Boruto"])
parent.append(["Hinata", "Himawari"])
married = list()
def marriedf(X, Y):
    if (X == 0 and Y == 0): return married
    if (X == 0): 
        for k in married:
            if (k[1] == Y): return k[0]
    if (Y == 0):
        for k in married:
            if (k[0] == X): return k[1]
    return [X, Y] in married
married.append(["Hagoromo", "Ozawa"])
married.append(["Ozawa", "Hagoromo"])
married.append(["Indra", "Outdra"])
married.append(["Outdra", "Indra"])
married.append(["Tajima", "Tanara"])
married.append(["Tanara", "Tajima"])
married.append(["Fugaku", "Mikoto"])
married.append(["Mikoto", "Fugaku"])
married.append(["Sasuke", "Sakura"])
married.append(["Sakura", "Sasuke"])
married.append(["Naruto", "Hinata"])
married.append(["Hinata", "Naruto"])
married.append(["Minato", "Kushina"])
married.append(["Kushina", "Minato"])
married.append(["Asura", "Bsura"])
married.append(["Bsura", "Asura"])
hokage = list()
def hokagef(X):
    if (X == 0): return hokage
    else: return X in hokage
hokage.append("Naruto")
name.append("Naruto")
hokage.append("Minato")
name.append("Minato")
name = sorted(set(name))
def husbandf(X, Y):
    res = list()
    for i0 in name:
        for i1 in name:
            if (malef(i0) and femalef(i1) and marriedf(i0, i1)):
                if (X == 0 and Y == 0):  res.append([i0, i1])
                elif (X == 0 and Y == i1): res.append(i0)
                elif (X == i0 and Y == 0): res.append(i1)
                elif (X == i0 and Y == i1): return True
    if(len(res) == 0): return False
    return res
def wifef(X, Y):
    res = list()
    for i0 in name:
        for i1 in name:
            if (husbandf(i1, i0)):
                if (X == 0 and Y == 0):  res.append([i0, i1])
                elif (X == 0 and Y == i1): res.append(i0)
                elif (X == i0 and Y == 0): res.append(i1)
                elif (X == i0 and Y == i1): return True
    if(len(res) == 0): return False
    return res
def fatherf(X, Y):
    res = list()
    for i0 in name:
        for i1 in name:
            if (parentf(i0, i1) and malef(i0)):
                if (X == 0 and Y == 0):  res.append([i0, i1])
                elif (X == 0 and Y == i1): res.append(i0)
                elif (X == i0 and Y == 0): res.append(i1)
                elif (X == i0 and Y == i1): return True
    if(len(res) == 0): return False
    return res
def motherf(X, Y):
    res = list()
    for i0 in name:
        for i1 in name:
            if (parentf(i0, i1) and femalef(i0)):
                if (X == 0 and Y == 0):  res.append([i0, i1])
                elif (X == 0 and Y == i1): res.append(i0)
                elif (X == i0 and Y == 0): res.append(i1)
                elif (X == i0 and Y == i1): return True
    if(len(res) == 0): return False
    return res
def childf(X, Y):
    res = list()
    for i0 in name:
        for i1 in name:
            if (parentf(i1, i0)):
                if (X == 0 and Y == 0):  res.append([i0, i1])
                elif (X == 0 and Y == i1): res.append(i0)
                elif (X == i0 and Y == 0): res.append(i1)
                elif (X == i0 and Y == i1): return True
    if(len(res) == 0): return False
    return res
def sonf(X, Y):
    res = list()
    for i0 in name:
        for i1 in name:
            if (childf(i0, i1) and malef(i0)):
                if (X == 0 and Y == 0):  res.append([i0, i1])
                elif (X == 0 and Y == i1): res.append(i0)
                elif (X == i0 and Y == 0): res.append(i1)
                elif (X == i0 and Y == i1): return True
    if(len(res) == 0): return False
    return res
def daughterf(X, Y):
    res = list()
    for i0 in name:
        for i1 in name:
            if (childf(i0, i1) and femalef(i0)):
                if (X == 0 and Y == 0):  res.append([i0, i1])
                elif (X == 0 and Y == i1): res.append(i0)
                elif (X == i0 and Y == 0): res.append(i1)
                elif (X == i0 and Y == i1): return True
    if(len(res) == 0): return False
    return res
def grandparentf(X, Y):
    res = list()
    for i0 in name:
        for i1 in name:
            for i2 in name:
                if (parentf(i0, i2) and parentf(i2, i1)):
                    if (X == 0 and Y == 0):  res.append([i0, i1])
                    elif (X == 0 and Y == i1): res.append(i0)
                    elif (X == i0 and Y == 0): res.append(i1)
                    elif (X == i0 and Y == i1): return True
    if(len(res) == 0): return False
    return res
def grandmotherf(X, Y):
    res = list()
    for i0 in name:
        for i1 in name:
            if (grandparentf(i0, i1) and femalef(i0)):
                if (X == 0 and Y == 0):  res.append([i0, i1])
                elif (X == 0 and Y == i1): res.append(i0)
                elif (X == i0 and Y == 0): res.append(i1)
                elif (X == i0 and Y == i1): return True
    if(len(res) == 0): return False
    return res
def grandfatherf(X, Y):
    res = list()
    for i0 in name:
        for i1 in name:
            if (grandparentf(i0, i1) and malef(i0)):
                if (X == 0 and Y == 0):  res.append([i0, i1])
                elif (X == 0 and Y == i1): res.append(i0)
                elif (X == i0 and Y == 0): res.append(i1)
                elif (X == i0 and Y == i1): return True
    if(len(res) == 0): return False
    return res
def grandchildf(X, Y):
    res = list()
    for i0 in name:
        for i1 in name:
            if (grandparentf(i1, i0)):
                if (X == 0 and Y == 0):  res.append([i0, i1])
                elif (X == 0 and Y == i1): res.append(i0)
                elif (X == i0 and Y == 0): res.append(i1)
                elif (X == i0 and Y == i1): return True
    if(len(res) == 0): return False
    return res
def grandsonf(X, Y):
    res = list()
    for i0 in name:
        for i1 in name:
            if (grandchildf(i0, i1) and malef(i0)):
                if (X == 0 and Y == 0):  res.append([i0, i1])
                elif (X == 0 and Y == i1): res.append(i0)
                elif (X == i0 and Y == 0): res.append(i1)
                elif (X == i0 and Y == i1): return True
    if(len(res) == 0): return False
    return res
def granddaughterf(X, Y):
    res = list()
    for i0 in name:
        for i1 in name:
            if (grandchildf(i0, i1) and femalef(i0)):
                if (X == 0 and Y == 0):  res.append([i0, i1])
                elif (X == 0 and Y == i1): res.append(i0)
                elif (X == i0 and Y == 0): res.append(i1)
                elif (X == i0 and Y == i1): return True
    if(len(res) == 0): return False
    return res
def siblingf(X, Y):
    res = list()
    for i0 in name:
        for i1 in name:
            for i2 in name:
                if (parentf(i2, i0) and parentf(i2, i1) and i0 != i1):
                    if (X == 0 and Y == 0):  res.append([i0, i1])
                    elif (X == 0 and Y == i1): res.append(i0)
                    elif (X == i0 and Y == 0): res.append(i1)
                    elif (X == i0 and Y == i1): return True
    if(len(res) == 0): return False
    return res
def brotherf(X, Y):
    res = list()
    for i0 in name:
        for i1 in name:
            if (siblingf(i0, i1) and malef(i0)):
                if (X == 0 and Y == 0):  res.append([i0, i1])
                elif (X == 0 and Y == i1): res.append(i0)
                elif (X == i0 and Y == 0): res.append(i1)
                elif (X == i0 and Y == i1): return True
    if(len(res) == 0): return False
    return res
def sisterf(X, Y):
    res = list()
    for i0 in name:
        for i1 in name:
            if (siblingf(i0, i1) and femalef(i0)):
                if (X == 0 and Y == 0):  res.append([i0, i1])
                elif (X == 0 and Y == i1): res.append(i0)
                elif (X == i0 and Y == 0): res.append(i1)
                elif (X == i0 and Y == i1): return True
    if(len(res) == 0): return False
    return res
def auntf(X, Y):
    res = list()
    for i0 in name:
        for i1 in name:
            for i2 in name:
                if (sisterf(i0, i2) and parentf(i2, i1)):
                    if (X == 0 and Y == 0):  res.append([i0, i1])
                    elif (X == 0 and Y == i1): res.append(i0)
                    elif (X == i0 and Y == 0): res.append(i1)
                    elif (X == i0 and Y == i1): return True
    if(len(res) == 0): return False
    return res
def unclef(X, Y):
    res = list()
    for i0 in name:
        for i1 in name:
            for i2 in name:
                if (brotherf(i0, i2) and parentf(i2, i1)):
                    if (X == 0 and Y == 0):  res.append([i0, i1])
                    elif (X == 0 and Y == i1): res.append(i0)
                    elif (X == i0 and Y == 0): res.append(i1)
                    elif (X == i0 and Y == i1): return True
    if(len(res) == 0): return False
    return res
def niecef(X, Y):
    res = list()
    for i0 in name:
        for i1 in name:
            for i2 in name:
                if (femalef(i0) and parentf(i2, i0) and siblingf(i2, i1)):
                    if (X == 0 and Y == 0):  res.append([i0, i1])
                    elif (X == 0 and Y == i1): res.append(i0)
                    elif (X == i0 and Y == 0): res.append(i1)
                    elif (X == i0 and Y == i1): return True
    if(len(res) == 0): return False
    return res
def nephewf(X, Y):
    res = list()
    for i0 in name:
        for i1 in name:
            for i2 in name:
                if (malef(i0) and parentf(i2, i0) and siblingf(i2, i1)):
                    if (X == 0 and Y == 0):  res.append([i0, i1])
                    elif (X == 0 and Y == i1): res.append(i0)
                    elif (X == i0 and Y == 0): res.append(i1)
                    elif (X == i0 and Y == i1): return True
    if(len(res) == 0): return False
    return res
