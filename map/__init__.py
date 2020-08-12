import openpyxl

book = openpyxl.load_workbook('Embassies Consulates and Missions Lat Longs.xlsx')

sheet = book.active

DICT = {} #keys: countries , values: long/lat dictionary - DICT has not yet been tested
a = []

all_countries = ['Afghanistan',
'Albania',
'Algeria',
'Andorra',
'Angola',
'Antigua and Barbuda',
'Argentina',
'Armenia',
'Australia',
'Austria',
'Azerbaijan',
'Bahamas',
'Bahrain',
'Bangladesh',
'Barbados',
'Belarus',
'Belgium',
'Belize',
'Benin',
'Bhutan',
'Bolivia',
'Bosnia and Herzegovina',
'Botswana',
'Brazil',
'Brunei',
'Bulgaria',
'Burkina Faso',
'Burundi',
'Cambodia',
'Cameroon',
'Canada',
'Cape Verde',
'Central African Republic',
'Chad',
'Chile',
'China',
'Colombia',
'Comoros',
'Congo, Democratic Republic of the',
'Congo, Republic of the',
'Costa Rica',
'Croatia',
'Cuba',
'Cyprus',
'Czech Republic',
'Denmark',
'Djibouti',
'Dominica',
'Dominican Republic',
'East Timor',
'Ecuador',
'Egypt',
'El Salvador',
'Equatorial Guinea',
'Eritrea',
'Estonia',
'Ethiopia',
'Fiji',
'Finland',
'France',
'Gabon',
'Gambia',
'Georgia',
'Germany',
'Ghana',
'Greece',
'Grenada',
'Guatemala',
'Guinea',
'Guinea-Bissau',
'Guyana',
'Haiti',
'Honduras',
'Hungary',
'Iceland',
'India',
'Indonesia',
'Iran',
'Iraq',
'Ireland {Republic}',
'Israel',
'Italy',
'Ivory Coast',
'Jamaica',
'Japan',
'Jordan',
'Kazakhstan',
'Kenya',
'Kiribati',
'Korea North',
'Korea South',
'Kosovo',
'Kuwait',
'Kyrgyzstan',
'Laos',
'Latvia',
'Lebanon',
'Lesotho',
'Liberia',
'Libya',
'Liechtenstein',
'Lithuania',
'Luxembourg',
'Macedonia',
'Madagascar',
'Malawi',
'Malaysia',
'Maldives',
'Mali',
'Malta',
'Marshall Islands',
'Mauritania',
'Mauritius',
'Mexico',
'Micronesia',
'Moldova',
'Monaco',
'Mongolia',
'Montenegro',
'Morocco',
'Mozambique',
'Myanmar, {Burma}',
'Namibia',
'Nauru',
'Nepal',
'Netherlands',
'New Zealand',
'Nicaragua',
'Niger',
'Nigeria',
'Norway',
'Oman',
'Pakistan',
'Palau',
'Panama',
'Papua New Guinea',
'Paraguay',
'Peru',
'Philippines',
'Poland',
'Portugal',
'Qatar',
'Romania',
'Russian Federation',
'Rwanda',
'St Kitts & Nevis',
'St Lucia',
'Saint Vincent & the Grenadines',
'Samoa',
'San Marino',
'Sao Tome & Principe',
'Saudi Arabia',
'Senegal',
'Serbia',
'Seychelles',
'Sierra Leone',
'Singapore',
'Slovakia',
'Slovenia',
'Solomon Islands',
'Somalia',
'South Africa',
'South Sudan',
'Spain',
'Sri Lanka',
'Sudan',
'Suriname',
'Swaziland',
'Sweden',
'Switzerland',
'Syria',
'Taiwan',
'Tajikistan',
'Tanzania',
'Thailand',
'Togo',
'Tonga',
'Trinidad & Tobago',
'Tunisia',
'Turkey',
'Turkmenistan',
'Tuvalu',
'Uganda',
'Ukraine',
'United Arab Emirates',
'United Kingdom',
'Uruguay',
'Uzbekistan',
'Vanuatu',
'Vatican City',
'Venezuela',
'Vietnam',
'Yemen',
'Zambia',
'Zimbabwe']

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

book = openpyxl.load_workbook('nodiplpresence.xlsx')
sheet = book.active

nodiplpresencelist = []
for row in sheet.iter_rows(min_row=3, min_col=1, max_row=6, max_col=3):
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

#arr[0] is ['Active', 'AF', "Cote d'Ivoire"]
#arr[0][0] is 'Active'

#book.save('iterbycols.xlsx')
