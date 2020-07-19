import openpyxl

book = openpyxl.load_workbook('Embassies Consulates and Missions Lat Longs.xlsx')

sheet = book.active

a = []
for row in sheet.iter_rows(min_row=2, min_col=1, max_row=276, max_col=15):
    col = []
    for cell in row:
        col.append(cell.value)
    a.append(col)
print(len(a))


#arr[0] is ['Active', 'AF', "Cote d'Ivoire"]
#arr[0][0] is 'Active'

#book.save('iterbycols.xlsx')