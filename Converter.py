def Converter():
    fi = open("test.pl", 'r')
    fo = open("PrologPython.py", 'r')

    line = "Not Empty String"

    while (1):
        line = fi.readline()

        if (not line):
            break

        if (line.find(":-") != -1):
            print("Found :-")
            line = fi.readline() # Temporarily skip the next line
        elif (line != "\n"):
            ListName = line.split('(')[0]
            AllFile = fo.read()
            fo = open("PrologPython.py", 'a')
            
            if (AllFile.find(ListName) == -1):
                fo.write(ListName + " = list()\n")
            
            DataInList = line.split('(')[1].split(')')[0]
            if (DataInList.find(',') != -1):
                fo.write(ListName + ".append([" + DataInList + "])\n")
            else:
                fo.write(ListName + ".append(" + DataInList + ")\n")
            fo = open("PrologPython.py", 'r')


Converter()