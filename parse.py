#!/usr/bin/env python3

import sys

def parse(txt_file):
    sequence_num = 0
    sequence_length = 0
    for line in txt_file:
         if '%' in line:
             if sequence_num != 0:
                 print('Sequence length: ', sequence_length, '\n')
                 sequence_length = 0
             line = line.split()
             print('ID: ', line[1])
             description = line[2:]
             print('Description: ', " ".join(description))
             sequence_num = sequence_num + 1
         else:
             sequence_length = sequence_length + len(line)
    print('Sequence length: ', sequence_length, '\n')

def TBFSDS_writer(input_file, output_file, wrap):
    if wrap == None:
        with open(input_file) as f1:
            with open(output_file, 'w') as f2:
                for line in f1:
                    f2.write(line)
    else:
        wrap = int(wrap)
        with open(input_file) as f1:
            with open(output_file, 'w') as f2:
                line_num = 0
                sequence = ''
                for line in f1:
                    if '%' in line:
                        if line_num != 0:
                            sequence = sequence.replace('\n', '')
                            for i in range(0, len(sequence), wrap):
                                f2.write(sequence[i:i+wrap])
                                f2.write('\n')
                            f2.write(line)
                            sequence = ''
                        else:
                            f2.write(line)
                            line_num = line_num + 1
                    else:
                        sequence = sequence + line
                sequence = sequence.replace('\n', '')
                for i in range(0, len(sequence), wrap):
                    f2.write(sequence[i:i+wrap])
                    f2.write('\n')

def main():
    if len(sys.argv) > 2 and sys.argv[2] == '--output':
        if len(sys.argv) > 4:
            TBFSDS_writer(sys.argv[1], sys.argv[3], sys.argv[5])
        else:
            TBFSDS_writer(sys.argv[1], sys.argv[3], None)
    else:
        for i in range(1, len(sys.argv)):
            print('Filename: ', sys.argv[i])
            with open(sys.argv[i]) as my_file:
                parse(my_file)

if __name__ == '__main__':
    main()
