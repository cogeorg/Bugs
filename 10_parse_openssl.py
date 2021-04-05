#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__="""Co-Pierre Georg (co-pierre.georg@uct.ac.za)"""

import sys
import os

from clint.textui import colored

# ###########################################################################
# METHODS
# ###########################################################################

# -------------------------------------------------------------------------
# do_run(file_name)
# -------------------------------------------------------------------------
def do_run(base_directory, app_directory, app_name, output_file_name):
    starting_file_name = base_directory + app_directory + app_name

    out_text = ""

    print("<<<<<< WORKING ON: " + starting_file_name)
    if True:
        print("    << INCLUDE DIR: " + base_directory + "include/ " + (colored.green("...TRUE") if os.path.isdir(base_directory + "include/") else colored.red("...FALSE")))

    input_file = open(starting_file_name, 'r')

    # read .txt file
    for line in input_file.readlines():
        tokens = line.strip()
        # print(tokens)

    # add output
    out_text += "\n"

    out_file = open(output_file_name, 'w')  # this is an edge list
    out_file.write(out_text)
    out_file.close()
    print("    >>> FILE WRITTEN TO:" + output_file_name)
    print(">>>>>> FINISHED")
# -------------------------------------------------------------------------


# -------------------------------------------------------------------------
#
#  MAIN
#
# -------------------------------------------------------------------------
if __name__ == '__main__':
#
# VARIABLES
#
    args = sys.argv
    base_directory = args[1]
    app_directory = args[2]
    app_name = args[3]
    output_file_name = args[4]

#
# CODE
#
    do_run(base_directory, app_directory, app_name, output_file_name)
