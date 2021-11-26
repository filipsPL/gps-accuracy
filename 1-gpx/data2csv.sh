#!/bin/bash

for f in *.tcx
do
    echo $f
    baza=$(basename $f .tcx | sed -e 's/Koko_Nut_/polar/g' -e 's/activity_786315/8291/g')
    #gpsbabel -t -i gtrnctr -f $f -x track,speed -o unicsv -F $baza.csv
    ./tcx_parser2.py --tcx $f > $baza.csv
done
