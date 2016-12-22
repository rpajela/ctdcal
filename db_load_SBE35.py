import sys
import db_load_scripts

def main(argv):
    with open(argv[0], 'r') as f:
        db_load_scripts.load_SBE35(f, int(argv[1]), int(argv[2]))

if __name__ == '__main__':
    main(sys.argv[1:])