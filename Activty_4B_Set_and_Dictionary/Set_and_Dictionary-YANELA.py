# Values of A, B, and C
A = {'a', 'b', 'c', 'd', 'f', 'g'}
B = {'b', 'c', 'h', 'l', 'm', 'o'}
C = {'c', 'd', 'f', 'h', 'i', 'j', 'k'}

# 1
# a. How many elements are there in set A and B
print("a.", len(A.intersection(B)))

# b. How many elements are there in B that is not part of A and C
print("b.", len(B - (A.union(C))))

# c. Show the following using set operations
print("i.", C - A)
print("ii.", A.intersection(C))
print("iii.", (B.intersection(A)).union(B.intersection(C)))
print("iv.", C.intersection(A) - B)
print("v.", (A.intersection(B)).intersection(C))
print("vi.", B - A.union(C))

# 2
exchange_rates = {
    "EUR": {"name": "Euro", "rate": 0.931936166},
    "GBP": {"name": "U.K. Pound Sterling", "rate": 0.827816452},
    "JPY": {"name": "Japanese Yen", "rate": 131.1994943},
    "AUD": {"name": "Australian Dollar", "rate": 1.439773864},
    "CHF": {"name": "Swiss Franc", "rate": 0.920289009},
    "CAD": {"name": "Canadian Dollar", "rate": 1.342307659},
    "NZD": {"name": "New Zealand Dollar", "rate": 1.583390808},
    "TRY": {"name": "Turkish Lira", "rate": 18.83402666},
    "NGN": {"name": "Nigerian Naira", "rate": 460.386436},
    "KGS": {"name": "Kyrgyzstan Som", "rate": 86.20468637},
    "MGA": {"name": "Malagasy ariary", "rate": 4304.101563},
    "SRD": {"name": "Surinamese dollar", "rate": 32.59911243},
    "GHS": {"name": "Ghanaian Cedi", "rate": 12.17177575},
    "CUP": {"name": "Cuban peso", "rate": 1},
    "NOK": {"name": "Norwegian Krone", "rate": 10.29227611},
    "QAR": {"name": "Qatari Rial", "rate": 3.647456564},
    "CZK": {"name": "Czech Koruna", "rate": 22.15119887},
    "HRK": {"name": "Croatian Kuna", "rate": 7.362267938},
    "RSD": {"name": "Serbian Dinar", "rate": 108.5081368},
    "NIO": {"name": "Nicaraguan C\u00f3rdoba", "rate": 36.54560531},
    "SBD": {"name": "Solomon Islands dollar", "rate": 8.41428026},
    "MWK": {"name": "Malawian kwacha", "rate": 1026.169965},
    "YER": {"name": "Yemeni rial", "rate": 250.1646044},
    "VES": {"name": "Venezuelan Bolivar", "rate": 23.11957702},
    "BDT": {"name": "Bangladeshi taka", "rate": 105.5535749},
    "RON": {"name": "Romanian New Leu", "rate": 4.561702839},
    "DZD": {"name": "Algerian Dinar", "rate": 136.0870755},
    "ARS": {"name": "Argentine Peso", "rate": 189.5406395},
    "STN": {"name": "S\u00e3o Tom\u00e9 and Pr\u00edncipe Dobra", "rate": 23.0151436},
    "BIF": {"name": "Burundian franc", "rate": 2075.047081},
    "PHP": {"name": "Philippine Peso", "rate": 54.81472581},
    "IDR": {"name": "Indonesian Rupiah", "rate": 15094.62702},
    "CNY": {"name": "Chinese Yuan", "rate": 6.787890099},
    "SGD": {"name": "Singapore Dollar", "rate": 1.325506488},
    "KRW": {"name": "South Korean Won", "rate": 1260.46907},
    "MYR": {"name": "Malaysian Ringgit", "rate": 4.292053266},
    "THB": {"name": "Thai Baht", "rate": 33.40043917},
    "TWD": {"name": "New Taiwan Dollar", "rate": 30.0665132},
    "IRR": {"name": "Iranian rial", "rate": 41997.79068},
    "BOB": {"name": "Bolivian Boliviano", "rate": 6.884075235},
    "LRD": {"name": "Liberian dollar", "rate": 156.8469751},
    "SDG": {"name": "Sudanese pound", "rate": 565.0512821},
    "TOP": {"name": "Tongan pa'anga", "rate": 2.380319723},
    "VUV": {"name": "Vanuatu vatu", "rate": 121.4193228},
    "OMR": {"name": "Omani Rial", "rate": 0.38471052},
    "ILS": {"name": "Israeli New Sheqel", "rate": 3.482745868},
    "PEN": {"name": "Peruvian Nuevo Sol", "rate": 3.854426226},
    "UZS": {"name": "Uzbekistan Sum", "rate": 11278.03328},
    "ETB": {"name": "Ethiopian birr", "rate": 53.68331303},
    "TTD": {"name": "Trinidad Tobago Dollar", "rate": 6.777487314},
    "PGK": {"name": "Papua New Guinean kina", "rate": 3.52422837},
    "BWP": {"name": "Botswana Pula", "rate": 12.92492669},
    "SEK": {"name": "Swedish Krona", "rate": 10.58459208},
    "SGD": {"name": "Singapore Dollar", "rate": 1.325506488},
    "HUF": {"name": "Hungarian Forint", "rate": 361.7082622},
    "BYN": {"name": "Belarussian Ruble", "rate": 2.786552647},
    "TJS": {"name": "Tajikistan Ruble", "rate": 10.29429222},
    "GMD": {"name": "Gambian dalasi", "rate": 63.2338594},
    "CVE": {"name": "Cape Verde escudo", "rate": 102.9766355},
    "ZMW": {"name": "Zambian kwacha", "rate": 19.22110772},
    "KHR": {"name": "Cambodian riel", "rate": 4096.096654},
    "DOP": {"name": "Dominican Peso", "rate": 56.40700086},
    "CNY": {"name": "Chinese Yuan", "rate": 6.787890099},
    "ISK": {"name": "Icelandic Krona", "rate": 141.0981925},
    "LYD": {"name": "Libyan Dinar", "rate": 4.781245694},
    "CLP": {"name": "Chilean Peso", "rate": 796.7962659},
    "BSD": {"name": "Bahamian Dollar", "rate": 1},
    "XPF": {"name": "CFP Franc", "rate": 110.9561452},
    "ALL": {"name": "Albanian lek", "rate": 107.9662927},
    "SCR": {"name": "Seychelles rupee", "rate": 13.61569354},
    "ANG": {"name": "Neth. Antillean Guilder", "rate": 1.795903979},
    "LBP": {"name": "Lebanese Pound", "rate": 4634.156998},
    "MYR": {"name": "Malaysian Ringgit", "rate": 4.292053266},
    "KZT": {"name": "Kazakhstani Tenge", "rate": 455.4250399},
    "HTG": {"name": "Haitian gourde", "rate": 150.619352},
    "BND": {"name": "Brunei Dollar", "rate": 1.323344843},
    "KMF": {"name": "Comoro franc", "rate": 460.7359398},
    "LSL": {"name": "Lesotho loti", "rate": 17.51748808},
    "TZS": {"name": "Tanzanian shilling", "rate": 2336.903499},
    "JOD": {"name": "Jordanian Dinar", "rate": 0.709595406},
    "PHP": {"name": "Philippine Peso", "rate": 54.81472581},
    "XOF": {"name": "West African CFA Franc", "rate": 611.3128462},
    "AMD": {"name": "Armenia Dram", "rate": 395.6927535},
    "UYU": {"name": "Uruguayan Peso", "rate": 39.19277801},
    "JMD": {"name": "Jamaican Dollar", "rate": 154.645614},
    "SSP": {"name": "South Sudanese pound", "rate": 741.986532},
    "MRU": {"name": "Mauritanian ouguiya", "rate": 36.36468647},
    "MNT": {"name": "Mongolian togrog", "rate": 3506.284805}
}

dollar_amount = float(input("How much dollar do you have? "))
currency_code = input("What currency you want to have? ").upper()

if currency_code in exchange_rates:
    converted_amount = dollar_amount * exchange_rates[currency_code]["rate"]
    currency_name = exchange_rates[currency_code]["name"]
    print(f"\nDollar: {dollar_amount} USD")
    print(f"{currency_name}: {converted_amount}")
else:
    print("Invalid currency code.")
