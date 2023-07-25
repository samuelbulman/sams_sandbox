import pandas as pd
import numpy as np
import os

home_dir = os.path.expanduser('~')
downloads_folder = os.path.join(home_dir, 'Downloads') + '/'
file_to_read = 'company_domain_test_file.csv'
file_to_write = 'company_domain_test_file_cleaned.csv'

# read in the csv file containing company domains in which you want to clean up
csv_df = pd.read_csv(f"{downloads_folder}{file_to_read}")

# strip out any null values from the company domain column
csv_df = csv_df[csv_df['company_domain'].notnull()]

# strip out any duplicate company domains, keeping the first instance of the domain
csv_df = csv_df.drop_duplicates(subset=['company_domain'], keep='first')

# create a "cleaned" company domain column that will be used to store the cleaned up domains
csv_df['cleaned_company_domain'] = np.nan

# create a list of the raw company domains to iterate over
raw_domain_list = csv_df['company_domain'].tolist()

# create a list of website domain country suffixes
domain_country_codes_list = [
    '.ac',  # Ascension Island
    '.ad',  # Andorra
    '.ae',  # United Arab Emirates
    '.af',  # Afghanistan
    '.ag',  # Antigua and Barbuda
    '.ai',  # Anguilla
    '.al',  # Albania
    '.am',  # Armenia
    '.ao',  # Angola
    '.aq',  # Antarctica
    '.ar',  # Argentina
    '.as',  # American Samoa
    '.at',  # Austria
    '.au',  # Australia
    '.aw',  # Aruba
    '.ax',  # Åland Islands
    '.az',  # Azerbaijan
    '.ba',  # Bosnia and Herzegovina
    '.bb',  # Barbados
    '.bd',  # Bangladesh
    '.be',  # Belgium
    '.bf',  # Burkina Faso
    '.bg',  # Bulgaria
    '.bh',  # Bahrain
    # '.bi',  # Burundi - removing because it will replace .biz with .bi
    '.bj',  # Benin
    '.bm',  # Bermuda
    '.bn',  # Brunei Darussalam
    '.bo',  # Bolivia (Plurinational State of)
    '.bq',  # Bonaire, Sint Eustatius and Saba
    '.br',  # Brazil
    '.bs',  # Bahamas
    '.bt',  # Bhutan
    '.bv',  # Bouvet Island
    '.bw',  # Botswana
    '.by',  # Belarus
    '.bz',  # Belize
    '.ca',  # Canada
    '.cc',  # Cocos (Keeling) Islands
    '.cd',  # Congo, Democratic Republic of the
    '.cf',  # Central African Republic
    '.cg',  # Congo
    '.ch',  # Switzerland
    '.ci',  # Côte d'Ivoire
    '.ck',  # Cook Islands
    '.cl',  # Chile
    '.cm',  # Cameroon
    '.cn',  # China
    # '.co',  # Colombia - removing this because it will replace .com with .co
    '.cr',  # Costa Rica
    '.cu',  # Cuba
    '.cv',  # Cabo Verde
    '.cw',  # Curaçao
    '.cx',  # Christmas Island
    '.cy',  # Cyprus
    '.cz',  # Czechia
    '.de',  # Germany
    '.dj',  # Djibouti
    '.dk',  # Denmark
    '.dm',  # Dominica
    '.do',  # Dominican Republic
    '.dz',  # Algeria
    '.ec',  # Ecuador
    '.ee',  # Estonia
    '.eg',  # Egypt
    '.eh',  # Western Sahara
    '.er',  # Eritrea
    '.es',  # Spain
    '.et',  # Ethiopia
    '.fi',  # Finland
    '.fj',  # Fiji
    '.fk',  # Falkland Islands (Malvinas)
    '.fm',  # Micronesia (Federated States of)
    '.fo',  # Faroe Islands
    '.fr',  # France
    '.ga',  # Gabon
    '.gb',  # United Kingdom of Great Britain and Northern Ireland
    '.gd',  # Grenada
    '.ge',  # Georgia
    '.gf',  # French Guiana
    '.gg',  # Guernsey
    '.gh',  # Ghana
    '.gi',  # Gibraltar
    '.gl',  # Greenland
    '.gm',  # Gambia
    '.gn',  # Guinea
    '.gp',  # Guadeloupe
    '.gq',  # Equatorial Guinea
    '.gr',  # Greece
    '.gs',  # South Georgia and the South Sandwich Islands
    '.gt',  # Guatemala
    '.gu',  # Guam
    '.gw',  # Guinea#Bissau
    '.gy',  # Guyana
    '.hk',  # Hong Kong
    '.hm',  # Heard Island and McDonald Islands
    '.hn',  # Honduras
    '.hr',  # Croatia
    '.ht',  # Haiti
    '.hu',  # Hungary
    '.id',  # Indonesia
    '.ie',  # Ireland
    '.il',  # Israel
    '.im',  # Isle of Man
    # '.in',  # India - removing because it will replace .int and .info with .in
    '.io',  # British Indian Ocean Territory
    '.iq',  # Iraq
    '.ir',  # Iran (Islamic Republic of)
    '.is',  # Iceland
    '.it',  # Italy
    '.je',  # Jersey
    '.jm',  # Jamaica
    '.jo',  # Jordan
    '.jp',  # Japan
    '.ke',  # Kenya
    '.kg',  # Kyrgyzstan
    '.kh',  # Cambodia
    '.ki',  # Kiribati
    '.km',  # Comoros
    '.kn',  # Saint Kitts and Nevis
    '.kp',  # Korea (Democratic People's Republic of)
    '.kr',  # Korea, Republic of
    '.kw',  # Kuwait
    '.ky',  # Cayman Islands
    '.kz',  # Kazakhstan
    '.la',  # Lao People's Democratic Republic
    '.lb',  # Lebanon
    '.lc',  # Saint Lucia
    '.li',  # Liechtenstein
    '.lk',  # Sri Lanka
    '.lr',  # Liberia
    '.ls',  # Lesotho
    '.lt',  # Lithuania
    '.lu',  # Luxembourg
    '.lv',  # Latvia
    '.ly',  # Libya
    '.ma',  # Morocco
    '.mc',  # Monaco
    '.md',  # Moldova, Republic of
    '.me',  # Montenegro
    '.mf',  # Saint Martin (French part)
    '.mg',  # Madagascar
    '.mh',  # Marshall Islands
    '.mk',  # North Macedonia
    '.ml',  # Mali
    '.mm',  # Myanmar
    '.mn',  # Mongolia
    '.mo',  # Macao
    '.mp',  # Northern Mariana Islands
    '.mq',  # Martinique
    '.mr',  # Mauritania
    '.ms',  # Montserrat
    '.mt',  # Malta
    '.mu',  # Mauritius
    '.mv',  # Maldives
    '.mw',  # Malawi
    '.mx',  # Mexico
    '.my',  # Malaysia
    '.mz',  # Mozambique
    '.na',  # Namibia
    '.nc',  # New Caledonia
    # '.ne',  # Niger - removing this because it will replace .net with .ne
    '.nf',  # Norfolk Island
    '.ng',  # Nigeria
    '.ni',  # Nicaragua
    '.nl',  # Netherlands
    '.no',  # Norway
    '.np',  # Nepal
    '.nr',  # Nauru
    '.nu',  # Niue
    '.nz',  # New Zealand
    '.om',  # Oman
    '.pa',  # Panama
    '.pe',  # Peru
    '.pf',  # French Polynesia
    '.pg',  # Papua New Guinea
    '.ph',  # Philippines
    '.pk',  # Pakistan
    '.pl',  # Poland
    '.pm',  # Saint Pierre and Miquelon
    '.pn',  # Pitcairn
    '.pr',  # Puerto Rico
    '.ps',  # Palestine, State of
    '.pt',  # Portugal
    '.pw',  # Palau
    '.py',  # Paraguay
    '.qa',  # Qatar
    '.re',  # Réunion
    '.ro',  # Romania
    '.rs',  # Serbia
    '.ru',  # Russian Federation
    '.rw',  # Rwanda
    '.sa',  # Saudi Arabia
    '.sb',  # Solomon Islands
    '.sc',  # Seychelles
    '.sd',  # Sudan
    '.se',  # Sweden
    '.sg',  # Singapore
    '.sh',  # Saint Helena, Ascension and Tristan da Cunha
    '.si',  # Slovenia
    '.sj',  # Svalbard and Jan Mayen
    '.sk',  # Slovakia
    '.sl',  # Sierra Leone
    '.sm',  # San Marino
    '.sn',  # Senegal
    '.so',  # Somalia
    '.sr',  # Suriname
    '.ss',  # South Sudan
    '.st',  # Sao Tome and Principe
    '.sv',  # El Salvador
    '.sx',  # Sint Maarten (Dutch part)
    '.sy',  # Syrian Arab Republic
    '.sz',  # Eswatini
    '.tc',  # Turks and Caicos Islands
    '.td',  # Chad
    '.tf',  # French Southern Territories
    '.tg',  # Togo
    '.th',  # Thailand
    '.tj',  # Tajikistan
    '.tk',  # Tokelau
    '.tl',  # Timor#Leste
    '.tm',  # Turkmenistan
    '.tn',  # Tunisia
    '.to',  # Tonga
    '.tr',  # Turkey
    '.tt',  # Trinidad and Tobago
    '.tv',  # Tuvalu
    '.tw',  # Taiwan
    '.tz',  # Tanzania, United Republic of
    '.ua',  # Ukraine
    '.ug',  # Uganda
    '.uk',  # United Kingdom
    '.us',  # United States of America
    '.uy',  # Uruguay
    '.uz',  # Uzbekistan
    '.va',  # Holy See
    '.vc',  # Saint Vincent and the Grenadines
    '.ve',  # Venezuela (Bolivarian Republic of)
    '.vg',  # Virgin Islands (British)
    '.vi',  # Virgin Islands (U.S.)
    '.vn',  # Viet Nam
    '.vu',  # Vanuatu
    '.wf',  # Wallis and Futuna
    '.ws',  # Samoa
    '.ye',  # Yemen
    '.yt',  # Mayotte
    '.za',  # South Africa
    '.zm',  # Zambia
    '.zw'  # Zimbabwe
]

website_domain_suffixes_list = [
    '.com', # Commercial (most popular and widely used)
    '.org', # Organization (usually for non#profit organizations)
    '.net', # Network (originally intended for network#related entities)
    '.gov', # Government (restricted for U.S. government entities)
    '.edu', # Education (restricted for educational institutions)
    '.mil', # Military (restricted for U.S. military entities)
    '.int', # International organizations
    '.info', # Informational websites
    '.biz' # Business or commercial use
]

clean_domain_list_1 = []
clean_domain_list_2 = []
clean_domain_list_3 = []
clean_domain_list_4 = []

# first, strip the protocol and www. from the domain
for raw_domain in raw_domain_list:
    clean_domain = raw_domain.replace('https://', '').replace('http://', '').replace('www.', '')
    clean_domain_list_1.append(clean_domain)

# second, clean up everything after the website domain suffix
for clean_domain in clean_domain_list_1:
    counter = 0
    for suffix in website_domain_suffixes_list:
        if suffix in clean_domain:
            cleaned_domain = clean_domain.split(suffix)[0] + suffix
            clean_domain_list_2.append(cleaned_domain)
            break
        else:
            if counter == len(website_domain_suffixes_list) - 1:
                clean_domain_list_2.append(clean_domain)
                break
        counter += 1

# third, clean up any remaining domains that have country codes

# loop through clean domain list 2
for cleaned_domain in clean_domain_list_2:
    # set a counter variable to 0
    counter = 0
    # loop through the domain country codes list
    for country_code in domain_country_codes_list:
        # if the country code is in the cleaned domain, split the domain at the country code and add the country code back in to remove any excess website url paths/characters
        if country_code in cleaned_domain:
            cleansed_domain = cleaned_domain.split(country_code)[0] + country_code
            # add the cleansed domain to the clean domain list 3
            clean_domain_list_3.append(cleansed_domain)
            break
        # if the country code is not in the cleaned domain, and we've fully looped through the list of country codes, add the domain that is being looped on to the clean domain list 3
        else:
            # subtract 1 from length of list because we are starting at 0
            if counter == len(domain_country_codes_list) - 1:
                clean_domain_list_3.append(cleaned_domain)
                break
        counter += 1

# lastly, wrap domains in single quotes and add a comma after each domain except for the last domain
final_step_counter = 0
for clean_domain in clean_domain_list_3:
    if final_step_counter < len(clean_domain_list_3) - 1:
        clean_domain = "'" + clean_domain + "',"
        clean_domain_list_4.append(clean_domain)
    elif final_step_counter == len(clean_domain_list_3) - 1:
        clean_domain = "'" + clean_domain + "'"
        clean_domain_list_4.append(clean_domain)
    final_step_counter += 1

#print('-- last iteration of clean domain list --', clean_domain_list_4, sep='\n')

# add the cleaned domains into the empty 'cleaned_company_domain' column in your csv file
csv_df['cleaned_company_domain'] = clean_domain_list_4

# finally, store a data frame with the original company domain and the cleaned company domain
csv_df = csv_df[['company_domain', 'cleaned_company_domain']]

# export the csv file with cleaned domains to your local machine
csv_df.to_csv(
    f"{downloads_folder}{file_to_write}", index=False
)