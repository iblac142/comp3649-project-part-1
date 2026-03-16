import sys

def processCommandLine():
    if len(sys.argv) < 3:
        print("Usage: python main.py <num_regs> <filename>")
        return 0
    if (not sys.argv[1].isdigit()):
        print("Error: <num_regs> is not a positive integer")
        return 0
    if (int(sys.argv[1]) == 0):
        print("Error: <num_regs> can't be 0")
        return 0
    
    numRegs = int(sys.argv[1])
    filename = sys.argv[2]

    try:
        with open(filename) as file:
            content = file.read()
            file.close()
            content = content.splitlines()
    except FileNotFoundError:
        print ("Error: file does not exist")
        return 0

    return content, numRegs, filename