# -*- coding: utf-8 -*-
# python 3.x

import csv
import sys
from tkinter import Tk
from tkinter.filedialog import askopenfile

# convert a "comma separated values" file to vcf contact cards. I used this to convert a list of student
# names and phone numbers into a vcf and save the trouble of adding one by one through phone

# USAGE:
# CSV_to_Vcards.py CSV_filename


def convert():
    # assuming file format : lastname,firstname,phonenumber,mail
    delim = input('O arquivo está separado por , ou ;?\n')
    filepath_global = askopenfile()
    somefile = filepath_global.name
    with open(somefile, 'r', encoding='utf-8', errors='ignore') as source:
        # reader now holds the whole data like ['lastname', 'firstname', 'phonenumber']
        reader = csv.reader(source, delimiter=delim)
        allvcf = open('ALL.vcf', 'w')
        i = 0
        for row in reader:
            if i == 0:
                i += 1
                continue
            firstname = row[0]
            lastname = row[1]
            phonenumber = row[2]
            email = row[3]
            # write in the "ALL.vcf" file.
            allvcf.write('BEGIN:VCARD' + "\n")
            allvcf.write('VERSION:2.1' + "\n")
            allvcf.write('N:' +firstname + ';' + row[1] + "\n")
            # remember that lastname first
            allvcf.write('FN:' + row[1] + ' ' +firstname + "\n")
            allvcf.write('TEL;CELL:' + '+' + row[2] + "\n")
            allvcf.write('EMAIL:' + row[3] + "\n")
            allvcf.write('END:VCARD' + "\n")
            allvcf.write("\n")

            i += 1  # counts

        allvcf.close()
        print(str(i-1) + " vcf cards generated")


if __name__ == '__main__':
    convert()
