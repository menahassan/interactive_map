import openpyxl
from googletrans import Translator

book = openpyxl.load_workbook('Embassies Consulates and Missions Lat Longs.xlsx')

sheet = book.active
translated = ""
DICT = {} #keys: countries , values: long/lat dictionary - DICT has not yet been tested
a = []

for row in sheet.iter_rows(min_row=2, max_row = 276, min_col=1, max_col=15, values_only=True):
    longlat = {}
    longlat["long"] = row[14]
    longlat["lat"]= row[13]
    DICT[row[2]] = longlat

for row in sheet.iter_rows(min_row=2, min_col=1, max_row=276, max_col=15):
    col = []
    for cell in row:
        col.append(cell.value)
    a.append(col)
    
translator = Translator()
translation = translator.translate('hello', dest='en')
translated = translation.text
#arr[0] is ['Active', 'AF', "Cote d'Ivoire"]
#arr[0][0] is 'Active'

#book.save('iterbycols.xlsx')
