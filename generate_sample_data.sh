#!/bin/bash

name=${1:-"A"}

loopx <(mdate -e 20150101  20151231 | tarr) <(seq 0 23|maezero 1.2) <(seq 0 59|maezero 1.2) <(seq 0 59|maezero 1.2)		|
# 1:YYYYMMDD 2:HH 2:MM 3:SS
tr -d ' '	|
# 1:YYYYMMDDHHMMSS
paste -d' ' - <(yes $name|head -$((365*24*60*60))) <(seq 0 100|ransu $((365*24*60*60))) <(seq 0 3|ransu $((365*24*60*60)))	|
# 1:YYYYMMDDHHMMSS 2:name 3:dummy_value 4:drop_flag
selr 4 0	|
delf 4		|
# 1:YYYYMMDDHHMMSS 2:name 3:dummy_value
cat		> set_$name

exit 0
