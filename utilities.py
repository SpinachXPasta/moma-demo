nation = ['Afghanistan', 'Albania', 'Algeria', 'American Samoa', 'Andorra',
       'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda',
       'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria',
       'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados',
       'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan',
       'Bolivia (Plurinational State of)',
       'Bonaire, Sint Eustatius and Saba', 'Bosnia and Herzegovina',
       'Botswana', 'Bouvet Island', 'Brazil',
       'British Indian Ocean Territory', 'Brunei Darussalam', 'Bulgaria',
       'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon',
       'Canada', 'Cayman Islands', 'Central African Republic', 'Chad',
       'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands',
       'Colombia', 'Comoros', 'Congo (Democratic Republic of the)',
       'Congo (Republic of the)', 'Cook Islands', 'Costa Rica', 'Croatia',
       'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', "Côte d'Ivoire",
       'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador',
       'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia',
       'Ethiopia', 'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji',
       'Finland', 'France', 'French Guiana', 'French Polynesia',
       'French Southern Territories', 'Gabon', 'Gambia', 'Georgia',
       'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada',
       'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea',
       'Guinea-Bissau', 'Guyana', 'Haiti',
       'Heard Island and McDonald Islands', 'Honduras', 'Hong Kong',
       'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq',
       'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan',
       'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati',
       "Korea (Democratic People's Republic of)", 'South Korea',
       'Kuwait', 'Kyrgyzstan', "Lao People's Democratic Republic",
       'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein',
       'Lithuania', 'Luxembourg', 'Macao',
       'Macedonia (the former Yugoslav Republic of)', 'Madagascar',
       'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta',
       'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius',
       'Mayotte', 'Mexico', 'Micronesia (Federated States of)',
       'Moldova (Republic of)', 'Monaco', 'Mongolia', 'Montenegro',
       'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia',
       'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand',
       'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island',
       'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau',
       'Palestine, State of', 'Panama', 'Papua New Guinea', 'Paraguay',
       'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal',
       'Puerto Rico', 'Qatar', 'Romania', 'Russian Federation', 'Rwanda',
       'Réunion', 'Saint Barthélemy',
       'Saint Helena, Ascension and Tristan da Cunha',
       'Saint Kitts and Nevis', 'Saint Lucia',
       'Saint Martin (French part)', 'Saint Pierre and Miquelon',
       'Saint Vincent and the Grenadines', 'Samoa', 'San Marino',
       'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia',
       'Seychelles', 'Sierra Leone', 'Singapore',
       'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia',
       'Solomon Islands', 'Somalia', 'South Africa',
       'South Georgia and the South Sandwich Islands', 'South Sudan',
       'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Svalbard and Jan Mayen',
       'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic',
       'Taiwan, Province of China', 'Tajikistan',
       'Tanzania, United Republic of', 'Thailand', 'Timor-Leste', 'Togo',
       'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey',
       'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda',
       'Ukraine', 'United Arab Emirates',
       'United Kingdom of Great Britain and Northern Ireland',
       'United States of America', 'Uruguay', 'Uzbekistan', 'Vanuatu',
       'Vatican City State', 'Venezuela (Bolivarian Republic of)',
       'Vietnam', 'Virgin Islands (British)', 'Virgin Islands (U.S.)',
       'Wallis and Futuna', 'Western Sahara', 'Yemen', 'Zambia',
       'Zimbabwe', 'Åland Islands']

dep = ['2004-04-22',
 'Architecture & Design',
 'Architecture & Design - Image Archive',
 'Drawings',
 'Film',
 'Fluxus Collection',
 'Media and Performance Art',
 'Painting & Sculpture',
 'Photography',
 'Prints & Illustrated Books']

class search():
    tempspace = ''
    tempspace2 = ''
 
    def __init__(self):
        self.dic = {'nation':'','dep':'', 'inyear':0, 'outyear':0}
        
    def ret(self):
        return self.dic

class inSr(search):
    def __init__(self, inputNation, inputDep, inputStart, inputEnd):
        search.__init__(self)
        print ("Kool",self, inputNation, inputDep, inputStart, inputEnd)
        self.nation = inputNation
        self.dep = inputDep
        self.inyear = inputStart
        self.outyear = inputEnd
        
    def setup(self):
        self.dic['nation'] = self.nation
        self.dic['dep'] = self.dep
        self.dic['inyear'] = self.inyear
        self.dic['outyear'] = self.outyear
        
    def closestCountry(self):
        self.nation = rambo(search.tempspace,nation)
        return rambo(search.tempspace,nation)
        
    def closestDep(self):
        self.dep = rambo(search.tempspace2,dep)
        return rambo(search.tempspace2,dep)
    def setdictionary(self):
        self.dic['nation'] = self.nation
        self.dic['dep'] = self.dep

    def emptyDic1(self):
        return search.tempspace
    def emptyDic2(self):
        return search.tempspace2
    def blank1(self):
        if self.dic['nation'] == ''  or self.dic['nation'] == 0 or self.dic['nation'] == None:
            return True
    def blank2(self):
        if self.dic['dep'] == '' or self.dic['dep'] == 0 or self.dic['dep'] == None:
            return True
