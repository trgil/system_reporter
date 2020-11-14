#!/usr/bin/env python3

import argparse

'''
    System Reporter

    Create a detailed report of system configurations.
'''

def run_system_reporter(args):

    if args.all:
        args.network = True
        args.disk = True
        args.file = True

    if args.network:
        print("Creating network report")
        print("-----------------------")

    if args.disk:
        print("Creating disk report")
        print("--------------------")

    if args.file:
        print("Creating files report")
        print("---------------------")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process Command-Line Arguments.')

    parser.add_argument('-n', '--network', action='store_true', required=False,
                   help='Create report on local network configuration')
    parser.add_argument('-d', '--disk', action='store_true', required=False,
                   help='Create report on local filesystems and storage devices')
    parser.add_argument('-f', '--file', action='store_true', required=False,
                   help='Create report on local files and directories')
    parser.add_argument('-v', '--device', action='store_true', required=False,
                   help='Create report on local files and directories')
    parser.add_argument('-a', '--all', action='store_true', required=False,
                   help='Create report on local files and directories')

    run_system_reporter(parser.parse_args())
