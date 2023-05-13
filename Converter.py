def Converter():
    fi = open("test.pl", 'r')

    fo = open("PrologPython.py", 'w')
    fo.write("name = list()\n")

    fo = open("PrologPython.py", 'r')

    line = "Not Empty String"

    while (1):
        line = fi.readline()

        if (not line):
            break
        
        removeDuplicate = 0

        if (line.find(":-") != -1):
            if (removeDuplicate == 0):
                removeDuplicate = 1
                fo = open("PrologPython.py", 'a')
                fo.write("name = sorted(set(name))\n")
                fo = open("PrologPython.py", 'r')
                
            print("Found :-")
            break
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