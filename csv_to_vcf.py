# -*- coding: utf-8 -*-
#python 3.x

import csv
import sys
from tkinter import Tk
from tkinter.filedialog import askopenfile

#convert a "comma separated values" file to vcf contact cards. I used this to convert a list of student
#names and phone numbers into a vcf and save the trouble of adding one by one through phone

#USAGE:
#CSV_to_Vcards.py CSV_filename

def convert():
    #assuming file format : lastname,firstname,phonenumber,mail
    delim = input('O arquivo está separado por , ou ;?\n')
    filepath_global = askopenfile()
    somefile = filepath_global.name
    with open( somefile, 'r' ) as source:
        reader = csv.reader( source, delimiter = delim ) #reader now holds the whole data like ['lastname', 'firstname', 'phonenumber']
        allvcf = open('ALL.vcf', 'w') 
        i = 0
        for row in reader:

            if i == 0:
                i+=1
                continue
            #write in the "ALL.vcf" file.
            allvcf.write( 'BEGIN:VCARD' + "\n")
            allvcf.write( 'VERSION:2.1' + "\n")
            allvcf.write( 'N:' + row[0] + ';' + row[1] + "\n")
            allvcf.write( 'FN:' + row[1] + ' ' + row[0] + "\n") #remember that lastname first
            allvcf.write( 'TEL;CELL:' + row[2] + "\n")
            allvcf.write( 'EMAIL:' + row[3] + "\n")
            allvcf.write( 'END:VCARD' + "\n")
            allvcf.write( "\n")

            i += 1#counts

        allvcf.close()
        print (str(i-1) + " vcf cards generated")



if __name__ == '__main__':
    convert()