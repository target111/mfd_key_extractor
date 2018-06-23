#!/usr/bin/python3

import binascii, os, argparse

def writeToFile(key, key_file):
    with open(key_file, "a") as f:
        f.write(key + "\n")

def getKeys(dump, key_file):
    dump = dump.decode('utf-8')

    zone = 0
    pos  = 0

    while zone <= 128 * 15:
        for l in range(0 + zone, 128 + zone):
            pos += 1

            if pos == 97:
                print("Key A: " + "".join(dump[l:l + 12]))
                writeToFile("".join(dump[l:l + 12]), key_file)
            elif pos == 117:
                print("Key B: " + "".join(dump[l:l + 12]))
                writeToFile("".join(dump[l:l + 12]), key_file)

        pos  = 0
        zone = zone + 128

def parse_args():
    arg_parser = argparse.ArgumentParser(description="""
A simple tool to extract keys from Mifare Classic 1K dump files.
""",formatter_class=argparse.RawDescriptionHelpFormatter)
    arg_parser.add_argument('-i', '--input', help='Mifare 1K dump input file')
    arg_parser.add_argument('-o', '--output', help='Key output file')
    args = arg_parser.parse_args()

    return args

def run(args):
    if os.path.isfile(args.input):
        with open(args.input, "rb") as f:
            getKeys(binascii.hexlify(f.read()), args.output)

def main():
    run(parse_args())

if __name__ == "__main__":
    main()
