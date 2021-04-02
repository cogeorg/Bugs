#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__="""Co-Pierre Georg (co-pierre.georg@uct.ac.za)"""

import sys
import os

# ###########################################################################
# METHODS
# ###########################################################################

# -------------------------------------------------------------------------
# do_run(file_name)
# -------------------------------------------------------------------------
def do_run(base_directory, input_file_name, output_file_name):
    input_file = open(base_directory + input_file_name, "r")

    out_text = ""

    print("<<<<<< WORKING ON: " + input_file_name)
    # if True:
    #     print("    << INCLUDE DIR: " + base_directory + "include/ " + (colored.green("...TRUE") if os.path.isdir(base_directory + "include/") else colored.red("...FALSE")))

    # read input file
    for line in input_file.readlines():
        tokens = line.strip().split(",")
        print(tokens)

    # add output
    out_text += "\n"

    out_file = open(base_directory + output_file_name, 'w')
    out_file.write(out_text)
    out_file.close()
    print("    >>> FILE WRITTEN TO:" + base_directory + output_file_name)
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
    input_file_name = args[2]
    output_file_name = args[3]

#
# CODE
#
    do_run(base_directory, input_file_name, output_file_name)
