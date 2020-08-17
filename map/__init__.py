#!/usr/bin/env python

import openpyxl
from googletrans import Translator

book = openpyxl.load_workbook('Embassies Consulates and Missions Lat Longs.xlsx')

sheet = book.active
translated = {} #list of hello translated in different languages
DICT = {} #keys: countries , values: long/lat dictionary - DICT has not yet been tested
a = []

for row in sheet.iter_rows(min_row=2, max_row = 276, min_col=1, max_col=15, values_only=True):
    longlat = {}
    longlat["long"] = row[14]
    longlat["lat"]= row[13]
    DICT[row[2]] = longlat

for row in sheet.iter_rows(min_row=2, min_col=1, max_row=276, max_col=18):
    col = []
    for cell in row:
        col.append(cell.value)
    a.append(col)

for i in a:
    langs = {}
    translator = Translator()
    translation = translator.translate('hello', dest=str(i[17]).lower())
    txt = translation.text
    langs["word"] = txt
    langs["language"] = str(i[17])
    langs["langFull"]=str(i[16])
    translated[i[13]] = langs
#arr[0] is ['Active', 'AF', "Cote d'Ivoire"]
#arr[0][0] is 'Active'
