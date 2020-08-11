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