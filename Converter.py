def Converter():
    fi = open("MyBase.pl", 'r')

    fo = open("PrologPython.py", 'w')
    fo.write("name = list()\n")

    fo = open("PrologPython.py", 'r')

    line = "Not Empty String"
    removeDuplicate = 0
    
    while (1):
        line = fi.readline()

        if (not line):
            break

        if (line.find(":-") != -1):
            if (removeDuplicate == 0):
                removeDuplicate = 1
                fo = open("PrologPython.py", 'a')
                fo.write("name = sorted(set(name))\n")
                fo = open("PrologPython.py", 'r')
                
            ######### Test #########
            fo = open("PrologPython.py", 'a')
            FuncName = line.split('(')[0]
            Parameter = list()

            OpenPos = 0
            while (1):
                OpenPos = line.find('(', OpenPos)
                if (OpenPos == -1):
                    break
                ClosePos = line.find(')', OpenPos)
                key = line[OpenPos + 1 : ClosePos]

                if (key.find(',') != -1):
                    temp = key.split(',')[0].strip()
                    if (temp not in Parameter): Parameter.append(temp)
                    temp = key.split(',')[1].strip()
                    if (temp not in Parameter): Parameter.append(temp)
                else:
                    temp = key.strip()
                    if (temp not in Parameter): Parameter.append(temp)

                OpenPos = ClosePos + 1

            Condition = line.split(':-')[1].strip()
            Condition = Condition.replace("), ", ") and ")
            Condition = Condition.replace(".", "")
            Condition = Condition.replace("\=", "!=")
            Condition = Condition.replace("(", "f(")
            for i in range(len(Parameter)):
                Condition = Condition.replace(Parameter[i], "i" + str(i))
            Condition = "if" + " (" + Condition + "):"

            fo.write("def " + FuncName + "f(X, Y):\n")
            fo.write("    res = list()\n")
            for i in range(len(Parameter)):
                fo.write("    " * (i + 1) + "for i" + str(i) + " in " + "name:\n")
            fo.write("    " * (len(Parameter) + 1) + Condition + "\n")
            fo.write("    " * (len(Parameter) + 2) + "if (X == 0 and Y == 0):  res.append([i0, i1])\n")
            fo.write("    " * (len(Parameter) + 2) + "elif (X == 0 and Y == i1): res.append(i0)\n")
            fo.write("    " * (len(Parameter) + 2) + "elif (X == i0 and Y == 0): res.append(i1)\n")
            fo.write("    " * (len(Parameter) + 2) + "elif (X == i0 and Y == i1): return True\n")

            fo.write("    if(len(res) == 0): return False\n")
            fo.write("    return res\n")
            fo = open("PrologPython.py", 'r')
            ######### End Test #########
        elif (line != "\n"):
            ListName = line.split('(')[0]
            AllFile = fo.read()
            fo = open("PrologPython.py", 'a')
            
            DataInList = line.split('(')[1].split(')')[0]
            if (AllFile.find(ListName) == -1): 
                fo.write(ListName + " = list()\n")
                if (DataInList.find(',') != -1): # Function with 2 argument
                    fo.write("def " + ListName + "f(X, Y):\n")
                    fo.write("    if (X == 0 and Y == 0): return " + ListName + "\n")
                    fo.write("    if (X == 0): \n")
                    fo.write("        for k in " + ListName + ":\n")
                    fo.write("            if (k[1] == Y): return k[0]\n")
                    fo.write("    if (Y == 0):\n")
                    fo.write("        for k in " + ListName + ":\n")
                    fo.write("            if (k[0] == X): return k[1]\n")
                    fo.write("    return [X, Y] in " + ListName + "\n")
                else: # Function with 1 argument
                    fo.write("def " + ListName + "f(X):\n")
                    fo.write("    if (X == 0): return " + ListName + "\n")
                    fo.write("    else: return X in " + ListName + "\n")

            if (DataInList.find(',') != -1):
                fo.write(ListName + ".append([" + DataInList + "])\n")
            else:
                fo.write(ListName + ".append(" + DataInList + ")\n")
                fo.write("name" + ".append(" + DataInList + ")\n")
            fo = open("PrologPython.py", 'r')


Converter()