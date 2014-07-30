"""
Script to change the old population codes which were used in
ITS and ETS sequencing to the new codes Yuri used in chloroplast
sequences.
"""
import fileinput

def fix_codes(file_name):

    f1 = open(file_name, 'r')
    f2 = open(file_name + '_fixed', 'w')
    for line in f1:
        f2.write(line.replace('>0410', '>x0401'))
    for line in f1:
        f2.write(line.replace('>0413', '>x0402'))
    for line in f1:
        f2.write(line.replace('>0405', '>x0404'))
    for line in f1:
        f2.write(line.replace('>0401', '>x0405'))
    for line in f1:
        f2.write(line.replace('>0402', '>x0406'))
    for line in f1:
        f2.write(line.replace('>0404', '>x0407'))
    for line in f1:
        f2.write(line.replace('>0411', '>x0408'))
    for line in f1:
        f2.write(line.replace('>0416', '>x0409'))
    for line in f1:
        f2.write(line.replace('>0407', '>x0410'))
    for line in f1:
        f2.write(line.replace('>0406', '>x0411'))
    for line in f1:
        f2.write(line.replace('>0409', '>x0412'))
    for line in f1:
        f2.write(line.replace('>0412', '>x0413'))
    for line in f1:
        f2.write(line.replace('>0418', '>x0414'))
    for line in f1:
        f2.write(line.replace('>0414', '>x0415'))
    for line in f1:
        f2.write(line.replace('>0415', '>x0416'))
    for line in f1:
        f2.write(line.replace('>x04', '>04'))
    f1.close()
    f2.close()

fix_codes('ETS.fas')
fix_codes('ITS.fas')

