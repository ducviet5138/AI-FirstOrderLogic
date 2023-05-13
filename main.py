from Converter import Converter
import os

filename = input("Enter the name of the file: ")

if os.path.exists(filename) == 0:
    print("File does not exist")
    exit()

Converter(filename)
from PrologPython import *

while (1):
    query = input("Enter the query (Type 'exit.' to exit): ")
    if (query == "exit."):
        exit()

    query = query.replace("(", "f(")
    query = query.replace(").", ")")

    if (query.find(",") != -1):
        keyA = query.split('(')[1].split(',')[0]
        keyB = query.split('(')[1].split(',')[1].split(')')[0]

        if (keyA.find('\"') == -1):
            query = query.replace(keyA, "0")
        if (keyB.find('\"') == -1):
            query = query.replace(keyB, "0")
    else:
        key = query.split('(')[1].split(')')[0]
        if (key.find('\"') == -1):
            query = query.replace(key, "0")

    print(eval(query))