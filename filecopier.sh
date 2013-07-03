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
fname[16]='usertesting.png'
fname[17]='budgetreduction.doc'
fname[18]='travelauthorization.pdf'
fname[19]='MeetingMinutes.doc'
fname[20]='SecurityAwarenessTraining.pdf'
fname[21]='PartialInventory.xls'
fname[22]='Biography.doc'
fname[23]='RedTeamTraining.pdf'
fname[24]='Timesheet.xls'
fname[25]='TrainingReceipt.pdf'
fname[26]='ProfessionalDevelopmentForm.doc'
fname[27]='ERDiagram.jpg'
fname[28]='FedRampWriteup.doc'
fname[29]='ReportingMatrix.doc'
fname[30]='QuarterlyChecklist.xls'

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
        newfilename=`shuf -i 0-30 -n 1`
        cp ${base[origfile]} $folders/${fname[newfilename]}
        ((counter++))
    done
done
