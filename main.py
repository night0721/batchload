import os
path = os.path.expanduser('~')
os.system("cls")
print("Copyright (C) Cath x Syntax. All rights reserved.\n")
print("Welcome to System Selector")
choice = input("Please choose System: (CLI, PW) ")
sys = choice.lower()
if sys == "pw":
    os.system("title Cath x Syntax PowerShell")
    os.system("cls")
    print("Cath x Syntax PowerShell")
    print("Copyright (C) Microsoft Corporation. All rights reserved.\n")
    while True:
        cmdx = input(f'PS {path}> ')
        spl = cmdx.split()
        try:
            os.system("powershell -" + cmdx)
        except Exception as e:
            print("Error:", e)
else:
    os.system("title Cath x Syntax Prompt v1.0.0")
    os.system("cls")
    print("Microsoft Windows [Cath x Syntax v1.0.0] ")
    print("Copyright (C) Microsoft Corporation. All rights reserved.\n")
    while True:
        cmdx = input(f'{path}> ')
        splitted = cmdx.split()
        try:
            if splitted[0].lower() == "batchload":
                try:
                    pathh = r'%s' % splitted[1]
                    f = open(pathh, "r")
                    lines = f.readlines()
                    for line in lines:
                        os.system(line)
                except Exception:
                    a = input("Batch Path> ")
                    pathh = r'%s' % a
                    f = open(pathh, "r")
                    lines = f.readlines()
                    for line in lines:
                        os.system(line)
            else:
                os.system(cmdx)
        except Exception as e:
            print("Error:", e)
