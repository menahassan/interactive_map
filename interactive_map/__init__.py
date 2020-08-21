import openpyxl

book = openpyxl.load_workbook('Embassies Consulates and Missions Lat Longs.xlsx')

sheet = book.active

arr = []

for row in sheet.iter_rows(min_row=2, min_col=1, max_row=6, max_col=17):
    col = []
    for cell in row:
        col.append(cell.value)
    arr.append(col)


#arr[0] is ['Active', 'AF', "Cote d'Ivoire"]
#arr[0][0] is 'Active'

#book.save('iterbycols.xlsx')