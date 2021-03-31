import argparse
parser = argparse.ArgumentParser(prog="Pokedex")
parser.add_argument('mode', choices=["pokemon","ability", "move"])
mutually_exclusive = parser.add_mutually_exclusive_group(required=True)
mutually_exclusive.add_argument('--inputfile', metavar='INPUTFILE', action='store')
mutually_exclusive.add_argument('--inputdata', metavar='INPUTDATA', action='store')
args = parser.parse_args()

def main():
    print(args)
    pass
    
if __name__ == '__main__':
    main()
