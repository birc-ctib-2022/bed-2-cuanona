#!/bin/bash
python3.10 src/sort_bed.py data/input.bed | .test/scripts/cmp.sh  data/input-sorted.bed