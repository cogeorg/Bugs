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

    out_text = "Project ID;Name;Created Timestamp;Updated Timestamp;Versions Count;Dependent Projects Count;Dependent Repositories Count;Repository ID\n"
    out_file = open(base_directory + output_file_name, 'w')
    out_file.write(out_text)
    out_file.close() # ensure file is empty
    out_file = open(base_directory + output_file_name, 'a')

    print("<<<<<< WORKING ON: " + base_directory + input_file_name)
    _count = 0
    _found = 0

    with open(base_directory + input_file_name) as infile:
        for line in infile:
            _count += 1
            tokens = line.strip().split(",")
            num_tokens = len(tokens)  # to correct the comma issue

            if tokens[1] == "NPM" or tokens[1] == "npm":
                out_text = tokens[0] + ";" + tokens[2] + ";" + tokens[3] + ";" + tokens[4] # the remainder needs to be taken from the end, due to fields including commas
                out_text += ";" + tokens[num_tokens-11] + ";" + tokens[num_tokens-6] + ";" + tokens[num_tokens - 2] + ";" + tokens[num_tokens - 1] + "\n"
                out_file.write(out_text)
                _found += 1

    # add output
    out_text += "\n"
    out_file.write(out_text)
    out_file.close()
    print("    >>> FOUND: " + str(_found) + " OF TOTAL: " + str(_count) + " ENTRIES")
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
