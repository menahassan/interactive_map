#!/usr/bin/env python

import openpyxl
from googletrans import Translator

book = openpyxl.load_workbook('Embassies Consulates and Missions Lat Longs.xlsx')

sheet = book.active
translated = {} #list of hello translated in different languages
DICT = {} #keys: countries , values: long/lat dictionary - DICT has not yet been tested
a = []

for row in sheet.iter_rows(min_row=2, max_row = 276, min_col=1, max_col=19, values_only=True):
    data = {}
    if(row[14] != None and row[13] != None and row[18] != None):
        data["long"] = row[14]
        data["lat"]= row[13]
        data["yearOpen"] = row[18].year
        data['city'] = row[3]
        
        DICT[row[2]] = data

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
    translated[i[13]] = langs
#arr[0] is ['Active', 'AF', "Cote d'Ivoire"]
#arr[0][0] is 'Active'


# Get the Human development Index of countries from 1990 - 2018
book2 = openpyxl.load_workbook('Human_Development_Index.xlsx')

sheet2 = book2.active
countriesHDI = {} #keys: countries initial , values: first element is the name of the country, the rest is HDI starting from 1990 - 2018

for row in sheet2.iter_rows(min_row=3, max_row = 197, min_col=1, max_col=32, values_only=True):
    countryHDI = [row[1]]
    for hdi in row[3:]:
            countryHDI = countryHDI + [hdi]
    countriesHDI[row[2]] = countryHDI