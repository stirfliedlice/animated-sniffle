#!/usr/bin/env python3
# -*-coding:utf-8 -*-

"""

simple text file parser for...

"""

import argparse
import logging
import os
import csv


def log_config(file_path: str) -> None:
    log_file = os.path.split(file_path)
    logging.basicConfig(
        filename='app.log',
        filemode='w',
        format='%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(message)s')


def cli_args() -> argparse.Namespace:
    """Get user arguments"""
    parser = argparse.ArgumentParser(
        prog="txt_file_parser.py",
        description="simple script to parse text file and write to csv",
        epilog="please contact me for any questions. Thanks for using %(prog)s! :)")
    parser.add_argument("path", type=str)
    args = parser.parse_args()
    return args


def check_file_size(file_path: str) -> bool:
    try:
        file_exists = os.path.getsize(file_path)
    except Exception as ex:
        logging.exception('Caught an error')
        raise


def file_open(file_path: str) -> list:
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            lines = file.readlines()
    except Exception as ex:
        logging.exception('Caught an error')
        raise
    return lines


def parse_lines(lines: list) -> list:
    data = list()
    return data


def dest_filepath(source_file: str) -> str:
    file_path, file_extension = os.path.splitext(source_file)
    dest_file = f'{file_path}.csv'
    return dest_file


def write_table(file_path: str, data) -> None:
    dest_file = dest_filepath(file_path)
    try:
        with open(dest_file, 'r', encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=',', quotechar='"')
            writer.writerow(['h', 'e', 'l', 'l', 'o'])
            writer.writerow(['w', 'o', 'r', 'l', 'd'])
    except Exception as ex:
        logging.exception('Caught an error')
        raise


def main() -> None:
    args = cli_args()
    lines = file_open(args.path)
    data = parse_lines(lines)
    write_table(args.path, data)


if __name__ == "__main__":
    main()
