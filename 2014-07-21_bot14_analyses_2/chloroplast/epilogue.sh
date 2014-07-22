#!/bin/bash
    date +'%s %a %b %e %R:%S %Z %Y' > /projects/ps-ngbt/backend/gordon_workspace/NGBW-JOB-MRBAYES_XSEDE-0F71450B4D014E4D823C17A53EC96E6D/term.txt
    echo "ExitCode=${10}" >> /projects/ps-ngbt/backend/gordon_workspace/NGBW-JOB-MRBAYES_XSEDE-0F71450B4D014E4D823C17A53EC96E6D/term.txt
    echo -e "Job Id: $1\nResource List: $6\nResources Used: $7\nQueue Name: $8\n" >> /projects/ps-ngbt/backend/gordon_workspace/NGBW-JOB-MRBAYES_XSEDE-0F71450B4D014E4D823C17A53EC96E6D/term.txt