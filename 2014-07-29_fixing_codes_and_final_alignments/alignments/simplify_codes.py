"""
Script to make all the '04' population codes shorter so as to be consistent between
nuclear and chloroplast sequences. For example 0104A6 and 0104A7 are both shortened
to 0104.
"""

import fileinput
import re

def fix_codes(file_name):

    f1 = open(file_name, 'r')
    f2 = open(file_name + '_fixed', 'w')
    for line in f1:
        f2.write(re.sub(r'>(\d\d\d\d).*', r'>\1', line.strip() + '\n'))
    f1.close()
    f2.close()

fix_codes('ETS.fas')
fix_codes('ITS.fas')
fix_codes('matK.fas')
fix_codes('rpl16.fas')
fix_codes('trnLF.fas')
fix_codes('trnTL.fas')

