#!/usr/bin/env python

import openpyxl

book = openpyxl.load_workbook('Embassies Consulates and Missions Lat Longs.xlsx')
sheet = book.active

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

book = openpyxl.load_workbook('airpollution.xlsx')
sheet = book.active

airpollution = []
for row in sheet.iter_rows(min_row=3, min_col=1, max_row=11, max_col=2):
    col = []
    for cell in row:
        col.append(cell.value)
    airpollution.append(col)

book = openpyxl.load_workbook('co2emissions.xlsx')
sheet = book.active

co2emissions = []
for row in sheet.iter_rows(min_row=3, min_col=1, max_row=11, max_col=2):
    col = []
    for cell in row:
        col.append(cell.value)
    co2emissions.append(col)

book = openpyxl.load_workbook('povertyrate.xlsx')
sheet = book.active

povertyrate = []
for row in sheet.iter_rows(min_row=3, min_col=1, max_row=11, max_col=2):
    col = []
    for cell in row:
        col.append(cell.value)
    povertyrate.append(col)

book = openpyxl.load_workbook('issues_summaries.xlsx')
sheet = book.active

issues_summaries = []
for row in sheet.iter_rows(min_row=3, min_col=1, max_row=5, max_col=4):
    col = []
    for cell in row:
        col.append(cell.value)
    issues_summaries.append(col)
