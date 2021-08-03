###########################################
__author__ = "ToorajJahangiri"
__email__ = "Toorajjahangiri@gmail.com"
###########################################

# IMPORTS
import os
import sys
import time
import argparse
from typing import Callable
from nested_cipher import *

__methods = ('b64','ab64','mb64','eb64','lb64','rb64','rab64','rmb64','reb64','rlb64')

def exe(data: bytes, method: Callable) -> bytes:
    return method(data)

def main(*argv) -> int:
    parser = argparse.ArgumentParser(prog='Nested Cipher', description='Simple Cipher Use UrlSafe Base 64')

    parser.add_argument('input', type=str, help='Input Data or File')
    parser.add_argument('--time', '-t', default=False, action='store_true', help='Processing Time Active')
    parser.add_argument('--mode', '-m', default='en', choices=['en', 'de', 'encode', 'decode'], help='Decode Active')
    parser.add_argument('--type', '-T', default='t', choices=['t', 'f'], help='Input Data Type')
    parser.add_argument('--out', '-O', type=str, help='Out Result File')
    parser.add_argument('--method', '-M', default='mb64', choices=[*__methods], help='Select Mode')

    arguments = parser.parse_args()


    if arguments.mode == 'en':
        method = eval(f"{arguments.method}_encode")
    elif arguments.mode == 'de':
        method = eval(f"{arguments.method}_decode")

    if arguments.type == 't':
        data = arguments.input.encode('utf-8')
    elif arguments.type == 'f':
        path = os.path.realpath(arguments.input)
        with open(path, 'rb') as f:
            data = f.read()

    if arguments.out is not None:
        out = os.path.realpath(arguments.out)
    else:
        out = False

    t0 = time.perf_counter_ns()
    results = exe(data, method)
    t1 = time.perf_counter_ns()

    if not out:
        print(results)
    else:
        with open(out, 'wb') as of:
            of.write(results)
    if arguments.time:
        print(f'TIME-PROCESS:<{(t1 - t0) / 1e+6:.6}> ms')



if __name__ == '__main__':
    exit(main(*sys.argv))
