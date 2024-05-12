from sys import argv

def Get_Argv(ArgvType:str="Target Input")->list:
    if len(argv) == 1: # The first argv is the path of this script
        print(f"\"{ArgvType}\" not Exist !")
        exit()
    else:
        return argv[1:]