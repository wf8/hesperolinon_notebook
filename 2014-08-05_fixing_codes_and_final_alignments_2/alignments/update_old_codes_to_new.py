"""
Script to change the old population codes which were used in
ITS and ETS sequencing to the new codes Yuri used in chloroplast
sequences.
"""
import fileinput

def fix_codes(file_name):

    f1 = open(file_name, 'r')
    text = f1.read()
    f1.close()

    f2 = open(file_name + '_fixed.fas', 'w')
    text = text.replace('>0410', '>x0401')
    text = text.replace('>0413', '>x0402')
    text = text.replace('>0405', '>x0404')
    text = text.replace('>0401', '>x0405')
    text = text.replace('>0402', '>x0406')
    text = text.replace('>0404', '>x0407')
    text = text.replace('>0411', '>x0408')
    text = text.replace('>0416', '>x0409')
    text = text.replace('>0407', '>x0410')
    text = text.replace('>0406', '>x0411')
    text = text.replace('>0409', '>x0412')
    text = text.replace('>0412', '>x0413')
    text = text.replace('>0418', '>x0414')
    text = text.replace('>0414', '>x0415')
    text = text.replace('>0415', '>x0416')
    text = text.replace('>x04', '>04')
    f2.write(text)
    f2.close()

fix_codes('ETS.fas_simplified.fas')
fix_codes('ITS.fas_simplified.fas')

