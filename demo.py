import argparse

def main():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description='A simple command-line tool')

    # Add arguments to the parser
    parser.add_argument( '--file', type=str, help='Input file name')
    parser.add_argument('--aaa', help='Input file name')
    parser.add_argument('--file2', type=str, help='Input file name')

    # Parse the command-line arguments
    args = parser.parse_args()

    print('Input file name: {}'.format(args.file))
    print('Input file2 name: {}'.format(args.file2))
    print('Input file3 name: {}'.format(args.aaa))

if __name__ == '__main__':
    main()
