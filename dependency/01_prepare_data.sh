#!/usr/bin/env bash

# ./10_prepare_dependencies.py \
#   /data/Data/libraries-1.4.0-2018-12-22/ \
#   dependencies.csv \
#   dependencies_npm.csv


# ./11_prepare_projects.py \
#   /data/Data/libraries-1.4.0-2018-12-22/ \
#   projects.csv \
#   projects_npm.csv


# ./12_prepare_versions.py \
#   /data/Data/libraries-1.4.0-2018-12-22/ \
#   versions.csv \
#   versions_npm-restricted.csv \
#   2010-12-18 \
#   2021-12-31


# execute in data directory:
# split -l 100000 -d -a 5 dependencies_npm.csv  ; mv x* dependencies/ ; cd dependencies ; for i in `ls` ; do mv $i $i.csv ; done ; cd ..

# then execute in this directory:
./20_merge_data.py \
  /data/Data/libraries-1.4.0-2018-12-22/ \
  dependencies/ \
  dependencies_restricted/
