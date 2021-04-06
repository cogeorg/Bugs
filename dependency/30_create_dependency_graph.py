#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__="""Co-Pierre Georg (co-pierre.georg@uct.ac.za)"""

import sys
import os
import re
import datetime

import networkx as nx

# ###########################################################################
# METHODS
# ###########################################################################

# -------------------------------------------------------------------------
# read_version_file(file_name)
# -------------------------------------------------------------------------
def read_version_file(file_name):
    versions = {}

    with open(file_name) as version_file:
        for line in version_file:
            tokens = line.strip().split(";")
            if "Project ID" not in line:  # drop header
                try:
                    versions[int(float(tokens[0]))].append(tokens[1])
                except:
                    versions[int(float(tokens[0]))] = [tokens[1]]

    if False:
        for key in versions:
            print(key, versions[key])

    return versions

# -------------------------------------------------------------------------
# find_matches(dependency)
# -------------------------------------------------------------------------
def find_matches(versions, from_id, from_version, dep_req, dep_id):
    matches = []

    dep_id = int(float(dep_id))
    try:
        # exact matches
        if dep_req in versions[dep_id]:
            matches.append(dep_req)
        if False: # Most packages seem to just use * for dependencies, creating a *lot* of edges. Hence, this part is optional
            if dep_req == "x" or dep_req == "*":
                for version in versions[dep_id]:
                    matches.append(version)

    except KeyError:
        if False:  # error logging
            print("   << ERROR: " + str(dep_id))

    return matches

# -------------------------------------------------------------------------
# do_run(file_name)
# -------------------------------------------------------------------------
def do_run(base_directory, input_file_name, output_file_name, version_file_name):
    line_count = 0

    G = nx.DiGraph()

    print("<<<<<< WORKING ON: " + base_directory + input_file_name + " USING VERSION FILE: " + base_directory + version_file_name)

    versions = read_version_file(base_directory + version_file_name)

    with open(base_directory + input_file_name) as infile:
        for line in infile:
            line_count += 1
            tokens = line.strip().split(",")

            from_id = int(tokens[1])
            from_version = tokens[3]

            if tokens[5] != "":
                to_id = int(float(tokens[5]))
                matches = find_matches(versions, from_id, from_version, tokens[4], to_id)
            if len(matches) > 0:
                from_node = str(from_id) + "-" + from_version
                for match in matches:
                    to_node = str(to_id) + "-" + match
                    G.add_edge(from_node, to_node)

    if True:  # debugging
        print("    >>> G: # Nodes: " + str(len(G.nodes())) + " # Edges: " + str(len(G.edges())))

    nx.write_gexf(G, base_directory + output_file_name)
    print("    >>> FILE WRITTEN TO:" + base_directory + output_file_name)
    print(">>>>>> FINISHED WORKING ON " + str(line_count) + " LINES")
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
    version_file_name = args[4]

#
# CODE
#
    do_run(base_directory, input_file_name, output_file_name, version_file_name)
