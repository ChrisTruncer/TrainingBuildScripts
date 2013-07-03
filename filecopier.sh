#!/bin/bash

# Script for copying random amount of files into each directory

# Array of file names that will be in each folder
fname[0]='clientdraft.doc'
fname[1]='dailystatus.doc'
fname[2]='onsiteaccess.pdf'
fname[3]='meetingminutes.doc'
fname[4]='ROE.pdf'
fname[5]='domainregistrar.csv'
fname[6]='targetemails.csv'
fname[7]='dbdump.sql'
fname[8]='template.txt'
fname[9]='financialstatus.xls'
fname[10]='outbrief.ppt'
fname[11]='evidence.pdf'
fname[12]='testrange.gnmap'
fname[13]='evidencecapture.zip'
fname[14]='baddata.sql'
fname[15]='databackup.zip'

# Array of the original files which are copied
base[0]='1meg'
base[1]='2meg'
base[2]='3meg'

for folders in $(cat directorylist.txt)
do
    numfiles=`shuf -i 7-12 -n 1`
    counter=1
    while [ $counter -lt $numfiles ]
    do
        origfile=`shuf -i 0-2 -n 1`
        newfilename=`shuf -i 0-15 -n 1`
        cp ${base[origfile]} $folders/${fname[newfilename]}
        ((counter++))
    done
done
