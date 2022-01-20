#!/usr/bin/env
from logic import decoded, compared, format_stylish, format_plain, format_json

import argparse


def generate_diff(filepath1, filepath2, form='stylish'):
    file1, file2 = decoded(filepath1), decoded(filepath2)
    diff = compared(file1, file2)
    if form == 'stylish':
        return format_stylish(diff)
    elif form == 'plain':
        return format_plain(diff)
    elif form == 'json':
        return format_json(diff)


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', default='stylish', help='set format of output')
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file, form=args.format))
 


if __name__ == '__main__':
    main()