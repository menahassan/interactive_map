#!/usr/bin/env python

import openpyxl
from googletrans import Translator

book = openpyxl.load_workbook('Embassies Consulates and Missions Lat Longs.xlsx')
sheet = book.active

translated = {}
embassies_consulates = [] #list of rows as shown in excel spreadsheet
for row in sheet.iter_rows(min_row=2, min_col=1, max_row=sheet.max_row, max_col=15):
    col = []
    for cell in row:
        col.append(cell.value)
    embassies_consulates.append(col)

book = openpyxl.load_workbook('nodiplpresence.xlsx')
sheet = book.active

nodiplpresencelist = []
for row in sheet.iter_rows(min_row=3, min_col=1, max_row=sheet.max_row, max_col=3):
    col = []
    for cell in row:
        col.append(cell.value)
    nodiplpresencelist.append(col)

book = openpyxl.load_workbook('airpollution.xlsx') #will later include more comprehensive data
sheet = book.active

airpollution = []
for row in sheet.iter_rows(min_row=3, min_col=1, max_row=11, max_col=2):
    col = []
    for cell in row:
        col.append(cell.value)
    airpollution.append(col)

book = openpyxl.load_workbook('issues_summaries.xlsx') #will later include more comprehensive data
sheet = book.active

issues_summaries = []
for row in sheet.iter_rows(min_row=3, min_col=1, max_row=3, max_col=3):
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
