#!/bin/bash
    date +'%s %a %b %e %R:%S %Z %Y' > /projects/ps-ngbt/backend/gordon_workspace/NGBW-JOB-MRBAYES_XSEDE-8D2E3C73271348C69BDE8385E3F6BCEF/term.txt
    echo "ExitCode=${10}" >> /projects/ps-ngbt/backend/gordon_workspace/NGBW-JOB-MRBAYES_XSEDE-8D2E3C73271348C69BDE8385E3F6BCEF/term.txt
    echo -e "Job Id: $1\nResource List: $6\nResources Used: $7\nQueue Name: $8\n" >> /projects/ps-ngbt/backend/gordon_workspace/NGBW-JOB-MRBAYES_XSEDE-8D2E3C73271348C69BDE8385E3F6BCEF/term.txt