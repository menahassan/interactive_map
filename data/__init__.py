#!/usr/bin/env python

import openpyxl
#from googletrans import Translator
book2 = openpyxl.load_workbook('Population.xlsx')

sheet2 = book2.active
#translated = {} #list of hello translated in different languages
DICT = {} #keys: countries , values: long/lat dictionary - DICT has not yet been tested
a = []

for row in sheet2.iter_rows(min_row=5, max_row = 268, min_col=1, max_col=44, values_only=True):
    years = {}
    years["recent"] = row[43]
    years["early"]= row[4]
    years["eightyone19"] = row[5]
    years["eightytwo19"] = row[6]
    years["eightythree19"] = row[7]
    years["eightyfour19"] = row[8]
    years["eightyfive19"] = row[9]
    years["eightysix19"] = row[10]
    years["eightyseven19"] = row[11]
    years["eightyeight19"] = row[12]
    years["eightynine19"] = row[13]
    years["ninety19"] = row[14]
    years["ninetyone19"] = row[15]
    years["ninetytwo19"] = row[16]
    years["ninetythree19"] = row[17]
    years["ninetyfour19"] = row[18]
    years["ninetyfive19"] = row[19]
    years["ninetysix19"] = row[20]
    years["ninetyseven19"] = row[21]
    years["ninetyeight19"] = row[22]
    years["ninetynine19"] = row[23]
    years["thousand20"] = row[24]
    years["one20"] = row[25]
    years["two20"] = row[26]
    years["three20"] = row[27]
    years["four20"] = row[28]
    years["five20"] = row[29]
    years["six20"] = row[30]
    years["seven20"] = row[31]
    years["eight20"] = row[32]
    years["nine20"] = row[33]
    years["ten20"] = row[34]
    years["eleven20"] = row[35]
    years["twelve20"] = row[36]
    years["thirteen20"] = row[37]
    years["fourteen20"] = row[38]
    years["fifteen20"] = row[39]
    years["sixteen20"] = row[40]
    years["seventeen20"] = row[41]
    years["eighteen20"] = row[42]
    DICT[row[0]] = years
#for i in a:
#    langs = {}
#    translator = Translator()
#    translation = translator.translate('hello', dest=str(i[17]).lower())
#    txt = translation.text
#    langs["word"] = txt
#    langs["language"] = str(i[17])
#    translated[i[13]] = langs
#arr[0] is ['Active', 'AF', "Cote d'Ivoire"]
#arr[0][0] is 'Active'