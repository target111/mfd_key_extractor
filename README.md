# Mifare Classic 1K dump file key extractor

A simple tool to extract encryption keys from Mifare Classic 1K dump files.
Dumps can be grabbed with [mfterm](https://github.com/4ZM/mfterm), [mfoc](https://github.com/nfc-tools/mfoc) or nfc-mfclassic tools from libnfc.org

## Command line options
```
./key_extractor.py -h
usage: key_extractor.py [-h] [-i INPUT] [-o OUTPUT]

A simple tool to extract keys from Mifare Classic 1K dump files.

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Mifare 1K dump input file
  -o OUTPUT, --output OUTPUT
                        Key output file
```
