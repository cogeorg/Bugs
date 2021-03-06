#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__="""Co-Pierre Georg (co-pierre.georg@uct.ac.za)"""

import sys
import os
import datetime

# ###########################################################################
# METHODS
# ###########################################################################

# -------------------------------------------------------------------------
# do_run(file_name)
# -------------------------------------------------------------------------
def do_run(base_directory, input_file_name, output_file_name, start_date, end_date):

    out_text = "Project ID;Version Number;Published Timestamp\n"
    out_file = open(base_directory + output_file_name, 'w')
    out_file.write(out_text)
    out_file.close() # ensure file is empty
    out_file = open(base_directory + output_file_name, 'a')

    print("<<<<<< WORKING ON: " + base_directory + input_file_name + " USING START: " + start_date + " END: " + end_date)
    _count = 0
    _found = 0

    start_datetime_obj = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end_datetime_obj = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    # print(start_datetime_obj.date(), start_datetime_obj.time(), end_datetime_obj.date(), end_datetime_obj.time())

    with open(base_directory + input_file_name) as infile:
        for line in infile:
            _count += 1
            tokens = line.strip().split(",")
            num_tokens = len(tokens)  # to correct the comma issue

            if tokens[1] == "NPM" or tokens[1] == "npm":
                #
                # check if version is within date range
                #

                # for this, convert src_date_time
                src_date_time = tokens[5]  # 5 = Published Timestamp ; 6 = Created Timestamp; 7 = Updated Timestamp
                src_date_time = src_date_time.replace(" UTC","").strip()
                date_time_obj = datetime.datetime.strptime(src_date_time, "%Y-%m-%d %H:%M:%S")
                if date_time_obj.date() <= end_datetime_obj.date() and date_time_obj.date() >= start_datetime_obj.date():
                    # then write text
                    out_text = tokens[3] + ";" + tokens[4] + ";" + src_date_time + "\n"
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
    start_date = args[4]
    end_date = args[5]

#
# CODE
#
    do_run(base_directory, input_file_name, output_file_name, start_date, end_date)
