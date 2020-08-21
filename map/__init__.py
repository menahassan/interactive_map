#!/usr/bin/env python

import openpyxl
from googletrans import Translator

book = openpyxl.load_workbook('map/Embassies Consulates and Missions Lat Longs.xlsx')
sheet = book.active

translated = {}
a = []
DICT = {}
embassies_consulates = [] #list of rows as shown in excel spreadsheet
for row in sheet.iter_rows(min_row=2, min_col=1, max_row=sheet.max_row, max_col=18):
    col = []
    for cell in row:
        col.append(cell.value)
    embassies_consulates.append(col)

yearEmbassyOpen = {} #keys: countries , values: long/lat dictionary - DICT has not yet been tested
for row in sheet.iter_rows(min_row=2, max_row = 276, min_col=1, max_col=19, values_only=True):
    data = {}
    if(row[14] != None and row[13] != None and row[18] != None):
        data["long"] = row[14]
        data["lat"]= row[13]
        data["yearOpen"] = row[18].year
        data['city'] = row[3]
        
        yearEmbassyOpen[row[2]] = data

book1 = openpyxl.load_workbook('map/nodiplpresence.xlsx')
sheet1 = book1.active

nodiplpresencelist = []
for row in sheet1.iter_rows(min_row=3, min_col=1, max_row=sheet1.max_row, max_col=3):
    col = []
    for cell in row:
        col.append(cell.value)
    nodiplpresencelist.append(col)

book2 = openpyxl.load_workbook('map/airpollution.xlsx') #will later include more comprehensive data
sheet2 = book2.active

airpollution = []
for row in sheet2.iter_rows(min_row=3, min_col=1, max_row=11, max_col=2):
    col = []
    for cell in row:
        col.append(cell.value)
    airpollution.append(col)

book3 = openpyxl.load_workbook('map/issues_summaries.xlsx') #will later include more comprehensive data
sheet3 = book3.active

issues_summaries = []
for row in sheet3.iter_rows(min_row=3, min_col=1, max_row=3, max_col=3):
    col = []
    for cell in row:
        col.append(cell.value)
    issues_summaries.append(col)


for i in embassies_consulates:
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


# Get the Human development Index of countries from 1990 - 2018
book2 = openpyxl.load_workbook('map/Human_Development_Index.xlsx')

sheet2 = book2.active
countriesHDI = {} #keys: countries initial , values: first element is the name of the country, the rest is HDI starting from 1990 - 2018

for row in sheet2.iter_rows(min_row=3, max_row = 197, min_col=1, max_col=32, values_only=True):
    countryHDI = [row[1]]
    for hdi in row[3:]:
            countryHDI = countryHDI + [hdi]
    countriesHDI[row[2]] = countryHDI