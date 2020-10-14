# MASTER LIST

pages_per_vol = {
    '1_133': {
        '1_*': {
            'weekday': [5, 'MNNAA'],
            'saturday': [2, 'MM']
        }
    },
    '134': {
        '1_252': {
            'weekday': [5, 'MNNAA'],
            'saturday': [2, 'MM']
        },
        '253_*': {
            'weekday': [4, 'MMAA'],
            'saturday': [2, 'MM']
        }
    },
    '135': {
        '1_40': {
            'weekday': [4, 'MMAA'],
            'saturday': [2, 'MM']
        },
        '41_*': {
            'weekday': [6, 'MMNNAA'],
            'saturday': [2, 'MM']
        }
    },
    '136_145': {
        '1_*': {
            'weekday': [6, 'MMNNAA'],
            'saturday': [2, 'MM']
        }
    },
    '146_164': {
        '1_*': {
            'weekday': [9, 'MMMNNNAAA'],
            'saturday': [3, 'MMM']
        }
    },
    '165': {
        '1_288': {
            'weekday': [9, 'MMMNNNAAA'],
            'saturday': [3, 'MMM']
        },
        '289_*': {
            'weekday': [6, 'MMMAAA'], # No noons
            'saturday': [3, 'MMM']
        }
    },
    '166_188': {
        '1_*': {
            'weekday': [6, 'MMMAAA'],
            'saturday': [3, 'MMM']
        }
    },
    '189_190': {
        '1_*': {
            'weekday': [6, 'MMMAAA'],
            'saturday': [0, '']
        }
    },
    '191': {
        '1_97': {
            'weekday': [6, 'MMMAAA'],
            'saturday': [0, '']
        },
        '98_*': {
            'weekday': [8, 'MMMMAAAA'],
            'saturday': [0, '']
        }
    },
    '192_199': {
        '1_*': {
            'weekday': [8, 'MMMMAAAA'],
            'saturday': [0, '']
        }
    }
}

closed = {
    '1901-01-23': 'Death of the Queen, business abandoned: https://trove.nla.gov.au/newspaper/article/14371864/1343690',
    '1901-04-09': 'Easter Tuesday',
    '1901-04-10': 'Easter Wednesday',
    '1902-04-01': 'Easter Tuesday',
    '1903-04-14': 'Easter Tuesday',
    '1904-04-05': 'Easter Tuesday',
    '1905-04-25': 'Easter Tuesday',
    '1905-04-26': 'Easter Wednesday',
    '1906-04-17': 'Easter Tuesday',
    '1906-04-18': 'Easter Wednesday',
    '1907-04-02': 'Easter Tuesday',
    '1908-04-21': 'Easter Tuesday',
    '1909-04-13': 'Easter Tuesday',
    '1909-04-14': 'Easter Wednesday',
    '1910-03-29': 'Easter Tuesday',
    '1910-03-30': 'Easter Wednesday',
    '1910-05-09': 'Death of the King -- https://trove.nla.gov.au/newspaper/article/15145878',
    '1911-04-18': 'Easter Tuesday',
    '1911-04-19': 'Easter Wednesday',
    '1912-04-09': 'Easter Tuesday',
    '1912-04-10': 'Easter Wednesday',
    '1913-03-25': 'Easter Tuesday',
    '1913-03-26': 'Easter Wednesday',
    '1913-10-04': 'Closed on Saturday as well as holiday Monday -- see http://nla.gov.au/nla.news-article15454723',
    '1914-04-14': 'Easter Tuesday',
    '1914-04-15': 'Easter Wednesday',
    '1915-04-06': 'Easter Tuesday',
    '1915-04-07': 'Easter Wednesday',
    '1916-04-20': 'early Easter',
    '1916-04-25': 'Easter Tuesday',
    '1916-04-26': 'Easter Wednesday',
    '1917-04-05': 'Thursday before Easter',
    '1917-04-10': 'Easter Tuesday',
    '1917-04-11': 'Easter Wednesday',
    '1918-04-02': 'Easter Tuesday',
    '1918-04-03': 'Easter Wednesday',
    '1919-04-17': 'Thursday before Easter',
    '1919-04-22': 'Easter Tuesday',
    '1919-04-23': 'Easter Wednesday',
    '1920-04-06': 'Easter Tuesday',
    '1920-04-07': 'Easter Wednesday',
    '1921-03-24': 'Thursday before Easter',
    '1921-03-29': 'Easter Tuesday',
    '1921-03-30': 'Easter Wednesday',
    '1922-04-13': 'Thursday before Easter',
    '1922-04-18': 'Easter Tuesday',
    '1922-04-19': 'Easter Wednesday',
    '1923-04-03': 'Easter Tuesday',
    '1923-04-04': 'Easter Wednesday',
    '1924-04-17': 'Thursday before Easter',
    '1924-04-22': 'Easter Tuesday',
    '1924-04-23': 'Easter Wednesday',
    '1924-10-11': 'Stock Exchange closed - http://nla.gov.au/nla.news-article28071778',
    '1925-04-09': 'Thursday before Easter',
    '1925-04-14': 'Easter Tuesday',
    '1925-04-15': 'Easter Wednesday',
    '1926-04-06': 'Easter Tuesday',
    '1926-04-07': 'Easter Wednesday',
    '1927-04-14': 'Thursday before Easter',
    '1927-04-19': 'Easter Tuesday',
    '1927-04-20': 'Easter Wednesday',
    '1928-04-05': 'Thursday before Easter',
    '1928-04-10': 'Easter Tuesday',
    '1928-04-11': 'Easter Wednesday',
    '1929-04-02': 'Easter Tuesday',
    '1929-04-03': 'Easter Wednesday',
    '1930-04-22': 'Easter Tuesday',
    '1930-04-23': 'Easter Wednesday',
    '1930-04-24': 'Day between Easter and Anzac Day',
    '1930-04-26': 'Day after Anzac Day? Business resumed on 28 April after extended Easter break - http://nla.gov.au/nla.news-article16691073',
    '1931-04-02': 'Thursday before Easter',
    '1931-04-07': 'Easter Tuesday',
    '1931-04-08': 'Easter Wednesday',
    '1932-03-24': 'Thursday before Easter',
    '1932-03-29': 'Easter Tuesday',
    '1932-03-30': 'Easter Wednesday',
    '1933-04-13': 'Thursday before Easter',
    '1933-04-18': 'Easter Tuesday',
    '1933-04-19': 'Easter Wednesday',
    '1934-04-03': 'Easter Tuesday',
    '1934-04-04': 'Easter Wednesday',
    '1935-04-18': 'Thursday before Easter',
    '1935-04-23': 'Easter Tuesday',
    '1935-04-24': 'Easter Wednesday',
    '1935-04-25': 'Thursday after Easter',
    '1936-04-09': 'Thursday before Easter',
    '1936-04-14': 'Easter Tuesday',
    '1936-04-15': 'Easter Wednesday',
    '1936-12-14': 'New King\'s birthday https://trove.nla.gov.au/newspaper/article/17310569',
    '1936-12-19': 'See https://trove.nla.gov.au/newspaper/article/17308675',
    '1937-03-30': 'Easter Tuesday',
    '1937-03-31': 'Easter Wednesday',
    '1938-04-14': 'Thursday before Easter',
    '1938-04-19': 'Easter Tuesday',
    '1938-04-20': 'Easter Wednesday',
    '1939-09-02': 'Closed due to war - http://nla.gov.au/nla.news-article17620079',
    '1939-09-04': 'Closed due to war - http://nla.gov.au/nla.news-article17620079',
    '1942-12-28': 'Holiday instead of new year\'s day http://nla.gov.au/nla.news-article17821583',
    '1944-04-11': 'Easter Tuesday',
    '1945-04-03': 'Easter Tuesday',
    '1945-08-15': 'Peace!',
    '1945-08-16': 'Peace!',
    '1946-04-23': 'Easter Tuesday',
    '1946-04-24': 'Easter Wednesday',
    '1947-04-08': 'Easter Tuesday',
    '1947-04-09': 'Easter Wednesday',
    '1948-03-30': 'Easter Tuesday',
    '1948-03-31': 'Easter Wednesday',
    '1949-04-19': 'Easter Tuesday',
    '1949-04-20': 'Easter Wednesday',
    '1950-04-11': 'Easter Tuesday',
    '1950-04-12': 'Easter Wednesday',
}

duplicates = [
    '8_63',
    '16_145',
    '17_213',
    '17_239',
    '35_93',
    '40_32',
    '40_284',
    '40_285',
    '43_79',
    '50_90',
    '52_16',
    '53_86',
    '71_228',
    '80_315',
    '87_2',
    '88_122',
    '89_63',
    '100_318',
    '101_172',
    '103_352',
    '107_235',
    '107_351',
    '108_13',
    '109_76',
    '109_331',
    '111_84',
    '111_216', # back of page
    '119_265',
    '124_22',
    '124_259',
    '136_225',
    '139_64',
    '139_264',
    '142_217',
    '143_375',
    '155_582',
    '156_206',
    '159_187',
    '160_467',
    '161_401',
    '161_441',
    '162_158',
    '169_46',
    '177_132',
    '178_107',
    '182_260',
    '184_259',
    '184_388',
    '185_282',
    '187_125',
    '188_34',
    '189_188',
    '196_342'
]

misplaced = {
    '1903-11-18': [[219, 'M'], [220, 'N']],
    '1906-03-21': [[282, 'N']],
    '1921-03-23': [[277, 'N']],
    '1922-07-03': [[1, 'N']],
    '1934-07-11': [[1, 'M'], [2, 'M'], [3, 'N'], [4, 'N'], [5, 'A'], [6, 'A']],
    '1934-07-12': [[7, 'M'], [8, 'M'], [9, 'A'], [10, 'A']],
    '1935-08-05': [[160, 'N'], [161, 'N']],
    '1935-09-07': [[295, 'M'], [296, 'M']],
    '1935-10-15': [[25, 'A']],
    '1935-10-19': [[82, 'M']],
    '1935-11-04': [[148, 'N']],
    '1936-04-07': [[21, 'N']],
    '1941-01-21': [[118, 'A'], [119, 'A'], [120, 'A']],
    '1945-07-30': [[151, 'A']],
    '1945-07-31': [[152, 'M'], [153, 'M'], [154, 'M'], [155, 'A'], [156, 'A'], [157, 'A']],
    '1949-12-08': [[209, 'M'], [210, 'M'], [211, 'M'], [212, 'M'], [213, 'A'], [214, 'A'], [215, 'A'], [216, 'A']],
    '1949-12-09': [[217, 'M'], [218, 'M'], [219, 'M'], [220, 'M'], [221, 'A'], [222, 'A'], [223, 'A'], [224, 'A']],
    '1949-12-13': [[225, 'M'], [226, 'M'], [227, 'M'], [228, 'M'], [229, 'A'], [230, 'A'], [231, 'A'], [232, 'A']],
    '1949-12-14': [[233, 'M'], [234, 'M'], [262, 'M'], [263, 'M'], [264, 'A'], [265, 'A'], [266, 'A'], [267, 'A']],
    '1949-12-19': [[313, 'M'], [314, 'M'], [315, 'M'], [316, 'M'], [317, 'A'], [318, 'A'], [319, 'A'], [320, 'A']],
}

missing = {
    '1901-01-07': [3, 'MNN'],
    '1901-01-18': [4, 'MNNA'],
    #'1901-01-23': [0, ''] # Death of the Queen business abandoned https://trove.nla.gov.au/newspaper/article/14371864/1343690
    '1901-02-25': [4, 'NNAA'],
    '1901-03-18': [0, ''],
    '1901-03-29': [0, ''], # missing
    '1901-04-04': [3, 'MNN'], # No afternoon, day before Easter
    #'1901-04-09': 0, # Extra Easter Tuesday
    #'1901-04-10': 0, # Extra Easter Wednesday
    '1901-04-15': [5, 'MNAAN'], # out of order
    #'1901-05-27': 0, # Holiday Duke of Cornwall visiting
    #'1901-05-28': 0, # Holiday Duke of Cornwall visiting
    # 1901-06-20: NNNAA - assume first N is M
    #'1901-07-03': 0, # Holiday for polling day
    '1901-09-16': [4, 'NNAA'], # No morning
    '1901-10-10': [4, 'MNAA'], # 1 Noon
    '1901-10-30': [4, 'MNAA'], # 1 Noon
    '1901-12-16': [2, 'NN'], # Noon only
    '1901-12-24': [3, 'MNN'],
    '1902-02-26': [0, ''], # ??
    '1902-03-27': [3, 'MNN'],
    '1902-04-02': [3, 'MNN'], # No afternboon
    '1902-06-26': [0, ''], # ??
    '1902-08-09': [0, ''], #??
    '1902-10-17': [6], # 008_0063 is a duplicate 
    '1902-12-24': [3, 'MNN'],
    '1903-01-06': [4, 'MNNA'], # 1 afternoon missing
    '1903-01-09': [4, 'NNAA'], # morning missing
    '1903-04-09': [3, 'MNN'], # No afternoon, day before Easter
    #'1903-04-14': 0, # Easter Tuesday
    # 1903-05-14: NNNAA - assume first N is M
    '1903-09-02': [5, 'NNNAA'], # has no morning, but 3 noons
    '1903-09-08': [4, 'NNAA'], # no morning
    '1903-09-16': [5, 'NNNAA'], # has no morning, but 3 noons
    '1903-10-01': [3, 'MNN'], # no afternoon
    '1903-11-18': [3, 'NAA'], # no morning, 1 noon -- see 219 and 220!
    '1903-11-30': [7, 'MNNAWWA'], # 2 sheets from 1903-11-18 inserted
    '1903-12-16': [0, ''], # ??
    '1903-12-24': [3, 'MNN'],
    '1904-01-20': [3, 'MNN'], # no afternoon
    '1904-03-31': [3, 'MNN'],
    '1904-08-15': [3, 'MNN'], # no afternoon
    '1904-11-09': [6], # 016_145 is a duplicate
    '1904-12-23': [3, 'MNN'],
    '1905-03-02': [6], # 017_213 is a duplicate
    '1905-03-08': [6], # 017_239 is a duplicate
    '1905-04-20': [3, 'MNN'], # No afternoon, day before Easter
    #'1905-04-25': 0, # Easter Tuesday
    #'1905-04-26': 0, # Easter Wednesday
    '1906-03-19': [6,'MNNAWA'], # extra page, 282 is from 1906-03-21
    '1906-03-21': [4, 'MNAA'], # 1 page included in 1906-03-19
    '1906-03-31': [1, 'M'],
    '1906-04-02': [4, 'MNNA'], # 1 afternoon missing
    '1906-04-06': [4, 'MNNA'], # 1 afternoon missing
    '1906-04-09': [4, 'MNNA'], # 1 afternoon missing
    '1906-04-10': [4, 'MNNA'], # 1 afternoon missing
    '1906-04-11': [4, 'MNNA'], # 1 afternoon missing
    '1906-04-12': [3, 'MNN'], # No afternoon, day before Easter
    # '1906-04-17': 0, # Easter Tuesday
    # '1906-04-18': 0, # Easter Wednesday
    '1906-04-25': [4, 'MNNA'], # 1 afternoon missing
    '1906-05-02': [4, 'MNNA'], # 1 afternoon missing
    '1906-05-03': [4, 'MNNA'], # 1 afternoon missing
    '1906-07-12': [4, 'MNNA'], # 1 afternoon missing
    '1906-07-16': [4, 'MNNA'], # 1 afternoon missing
    '1906-10-25': [3, 'MNN'], # Afternoon missing
    '1907-02-02': [1, 'M'], # Saturday 1 page only
    '1907-03-08': [4, 'MNNA'], # 1 afternoon missing
    '1907-03-28': [3, 'MNN'],
    '1907-04-29': [4, 'MNNA'], # 1 afternoon missing
    '1907-06-27': [2, 'MM'], # 2 pages only marked '11 o'clock'
    '1907-09-10': [3, 'MNN'], # No afternoon
    '1907-10-11': [4, 'MNNA'], # 1 afternoon missing
    '1907-11-29': [4, 'MNNA'], # 1 afternoon missing
    '1907-12-02': [4, 'MNNA'], # 1 afternoon missing
    '1907-12-24': [3, 'MNN'],
    '1908-03-12': [4, 'MNNA'], # 1 afternoon missing
    '1908-04-16': [3, 'MNN'], # No afternoon, day before Easter
    # '1908-04-21': 0, # Easter Tuesday
    # '1908-08-20': 0, # American Fleet visit!
    '1908-08-21': [3, 'AAA'], # No morning?
    # '1908-08-24': 0, # American Fleet visit!
    '1908-11-14': [1, 'M'], # Saturday 1 page only
    '1908-12-24': [3, 'MNN'],
    '1909-04-08': [3, 'MNN'], # No afternoon, day before Easter
    # '1909-04-13': 0, # Easter Tuesday
    # '1909-04-14': 0, # Easter Wednesday
    '1909-07-02': [4, 'MNNA'], # 1 afternoon missing
    '1909-07-24': [3], # 035_0093 is a duplicate
    '1909-12-24': [3, 'MNN'],
    '1910-03-24': [3, 'MNN'], # No afternoon, day before Easter
    # '1910-03-29': 0, # Easter Tuesday
    # '1910-03-30': 0, # Easter Wednesday
    '1910-04-15': [4, 'MNNA'], # 1 afternoon missing
    '1910-04-29': [4, 'MNNA'], # 1 afternoon missing
    '1910-05-03': [4, 'MNAA'], # 1 noon missing
    # '1910-05-09': 0, # Death of the King -- https://trove.nla.gov.au/newspaper/article/15145878
    '1910-08-31': [4, 'MNAA'], # 1 noon missing
    '1910-10-11': [6], # 040_032 is a duplicate
    '1910-12-14': [7], # 040_284 and 040_285 are duplicates
    '1910-12-23': [3, 'MNN'],
    '1911-02-09': [3, 'MNA'], # 1 noon, 1 afternoon
    '1911-03-13': [3, 'MNN'], # No afternoon
    '1911-04-13': [3, 'MNN'], # No afternoon, day before Easter
    # '1911-04-18': 0, # Easter Tuesday
    # '1911-04-19': 0, # Easter Wednesday
    '1911-05-05': [4, 'MNAA'], # 1 noon
    '1911-06-09': [4, 'MNAA'], # 1 noon
    '1911-07-21': [6], # 043_79 is a duplicate
    '1912-04-04': [3, 'MNN'], # No afternoon, day before Easter
    # '1912-04-09': 0, # Easter Tuesday
    # '1912-04-10': 0, # Easter Wednesday
    '1912-09-19': [4, 'MNAA'], # 1 noon
    '1913-01-08': [4, 'NNAA'], # No morning
    '1913-01-13': [4, 'NNAA'], # No morning
    '1913-02-06': [4, 'MNNA'], # 1 afternoon
    '1913-03-03': [4, 'MNNA'], # 1 afternoon
    '1913-03-20': [3, 'MNN'], # No afternoon, day before Easter
    # '1913-03-25': 0, # Easter Tuesday
    # '1913-03-26': 0, # Easter Wednesday
    '1913-04-10': [4, 'MNAA'], # 1 noon
    '1913-04-23': [6], # 050_0090 is a duplicate
    '1913-05-15': [4, 'MNAA'], # 1 noon
    '1913-06-04': [4, 'MNAA'], # 1 noon
    '1913-06-30': [4, 'MNAA'],
    '1913-10-03': [6], # 052_0016 is a duplicate
    # '1913-10-04': [0, ''], # Closed on Saturday as well as holiday Monday -- see http://nla.gov.au/nla.news-article15454723
    '1913-11-07': [3, 'MNN'], # No afternoon
    '1913-12-20': [1, 'M'], # Saturday 1 page only
    '1913-12-23': [4, 'MNNA'],
    '1914-01-27': [6], # N193-053_0086-header.jpg is a duplicate
    '1914-02-09': [4, 'MNAA'], # 1 noon
    '1914-02-23': [3, 'MNN'], # No afternoon
    '1914-02-26': [4, 'MNNA'], # 1 afternoon
    '1914-02-27': [5, 'AANNM'], # is out of order
    '1914-03-25': [5, 'NMNAA'], # is out of order
    '1914-04-09': [3, 'MNN'], # No afternoon, day before Easter
    #'1914-04-14': 0, # Easter Tuesday
    #'1914-04-15': 0, # Easter Wednesday
    '1914-06-18': [3, 'MNN'], # No afternoon
    # Start gap -- CHECK IF CLOSED ALL THIS TIME
    '1914-08-03': [0, ''],
    '1914-08-04': [0, ''],
    '1914-08-05': [0, ''],
    '1914-08-06': [0, ''],
    '1914-08-07': [0, ''],
    '1914-08-08': [0, ''],
    '1914-08-10': [0, ''],
    '1914-08-11': [0, ''],
    '1914-08-12': [0, ''],
    '1914-08-13': [0, ''],
    '1914-08-14': [0, ''],
    '1914-08-15': [0, ''],
    '1914-08-17': [0, ''],
    '1914-08-18': [0, ''],
    '1914-08-19': [0, ''],
    '1914-08-20': [0, ''],
    '1914-08-21': [0, ''],
    '1914-08-22': [0, ''],
    '1914-08-24': [0, ''],
    '1914-08-25': [0, ''],
    '1914-08-26': [0, ''],
    '1914-08-27': [0, ''],
    '1914-08-28': [0, ''],
    '1914-08-29': [0, ''],
    '1914-08-31': [0, ''],
    '1914-09-01': [0, ''],
    '1914-09-02': [0, ''],
    '1914-09-03': [0, ''],
    '1914-09-04': [0, ''],
    '1914-09-05': [0, ''],
    '1914-09-07': [0, ''],
    '1914-09-08': [0, ''],
    '1914-09-09': [0, ''],
    '1914-09-10': [0, ''],
    '1914-09-11': [0, ''],
    '1914-09-12': [0, ''],
    '1914-09-14': [0, ''],
    '1914-09-15': [0, ''],
    '1914-09-16': [0, ''],
    '1914-09-17': [0, ''],
    '1914-09-18': [0, ''],
    '1914-09-19': [0, ''],
    # End gap
    '1914-10-06': [3, 'MAA'], # No noon
    '1914-12-23': [3, 'MNN'],
    '1915-02-01': [5, 'ANNAA'], # is out of order and has 3 afternoons but no morning
    '1915-03-25': [4, 'MNNA'], # 1 afternoon
    # '1915-05-24': 0, # Empire Day (anniversary of birth of Queen Vic)
    '1915-07-01': [4, 'MNNA'], # 1 afternoon
    '1915-07-30': [4, 'NMAA'], # 1 noon, and out of order
    '1915-08-04': [5, 'AMNNA'], # is out of order
    '1915-08-05': [4, 'MNNA'], # 1 afternoon
    '1915-08-10': [4, 'MNNA'], # 1 afternoon
    '1915-10-22': [3, 'MNN'], # No afternoon
    '1915-11-19': [3, 'MAA'], # No noon
    '1915-12-23': [3, 'MNN'],
    # '1916-04-20': 0, # early Easter
    # '1916-04-25': 0, # Easter Tuesday
    # '1916-04-26': 0, # Easter Wednesday
    '1916-06-13': [3, 'MNA'], # 1 noon, 1 afternoon
    '1916-07-05': [4, 'NNAA'], # No morning
    '1916-07-14': [3, 'MNA'], # 1 noon, 1 afternoon
    # '1916-10-28': 0, # Public holiday for conscription referendum
    '1916-11-04': [1, 'M'], # 1 missing
    # '1916-11-18': 0, # For postponed 8-hour-day procession (from 2 October)
    '1916-11-24': [4, 'MNNA'], # 1 afternoon
    '1916-12-22': [3, 'MNN'],
    '1917-03-26': [3, 'MNN'], # No afternoon
    # '1917-04-05': 0, # Thursday before easter
    # '1917-04-10': 0, # Easter Tuesday
    # '1917-04-11': 0, # Easter Wednesday
    '1917-05-16': [4, 'MNAA'], # 1 noon
    '1917-05-23': [0, ''], # No holiday? Newspaper reports of trading.
    '1917-05-25': [4, 'MNAA'], # 1 noon
    '1917-07-16': [3, 'MNA'], # 1 noon, 1 afternoon
    '1917-09-13': [4, 'NNAA'], # No morning
    '1917-10-16': [3, 'MNN'], # No afternoon
    '1917-11-20': [3, 'MAA'], # No noon
    '1918-04-12': [4, 'NNAA'], # No morning
    '1918-07-30': [5, 'NNNAA'], # has 3 noons (but no morning)
    '1918-08-29': [6], # 71_228 is a duplicate
    '1918-10-31': [3, 'NMN'], # No afternoon? (one is unlabelled and they're out of order so hard to say)
    '1918-11-08': [1, 'M'], # Early Armistice celebrations? https://trove.nla.gov.au/newspaper/article/28099739/1257902
    # '1918-11-12': 0, # Peace! Holiday https://trove.nla.gov.au/newspaper/article/15810768 & https://trove.nla.gov.au/newspaper/article/15810602
    # '1918-11-13': 0, # Proclaimed holiday for the Armistice
    '1919-01-30': [5, 'NANNA'], # ? is out of order and seems to have 3 noons one sheet unlabelled
    '1919-03-10': [4, 'MNAA'], # 1 noon
    '1919-03-19': [3, 'MNN'], # No afternoon
    # '1919-04-17': 0, # Thursday before Easter
    # '1919-04-22': 0, # Easter Tuesday
    # '1919-04-23': 0, # Easter Wednesday
    # '1919-07-19': 0, # Peace Day -- to celebrate signing of the Treaty of Versailles
    '1919-07-18': [5, 'MANAA'],
    '1919-07-21': [5, 'ANNAA'], # are out of order
    '1919-08-27': [4, 'NNAA'], # No morning
    '1919-10-31': [4, 'NNAA'], # No morning
    '1919-11-17': [3, 'NAA'], # No morning, 1 noon
    '1920-02-25': [3, 'MNN'], # No afternoon
    '1920-03-18': [4, 'MNNA'], # 1 afternoon
    '1920-03-30': [5, 'NNNAA'], # there are three labelled 'Noon' but no morning
    # '1920-04-26': 0, # Anzac Day
    '1920-12-22': [6], # 80_315 is a duplicate
    '1920-12-23': [3, 'MNN'],
    '1921-02-09': [3, 'MNN'], # No afternoon
    '1921-03-18': [5, 'NNAMA'], # is out of order
    '1921-03-23': [2, 'MN'], # No afternoon, one noon with 31/3
    # '1921-03-24': 0, # Thursday before Easter
    # '1921-03-29': 0, # Easter Tuesday
    # '1921-03-30': 0, # Easter Wednesday
    '1921-03-31': [6, 'MWNANA'], # out of order, 2nd page is from Noon on 23/3
    '1921-04-22': [4, 'NNAM'], # 1 afternoon missing, but also out of order
    # '1921-04-25': 0, # Anzac Day was a holiday everywhere except NSW. Stock Exchange took a holiday anyway - http://nla.gov.au/nla.news-article15949228
    '1921-05-30': [3, 'MNN'], # No afternoon
    '1921-07-18': [4, 'NNAA'], # No morning
    '1921-10-07': [3, 'MNN'], # No afternoon
    '1922-03-06': [3, 'MNN'], # No afternoon
    '1922-04-12': [3, 'MNN'], # No afternoon
    # '1922-04-13': 0, # Thursday before Easter
    # '1922-04-18': 0, # Easter Tuesday
    # '1922-04-19': 0, # Easter Wednesday
    # Note that start date on this volume should be 1/7 NOT 3/7 as in series list
    '1922-07-01': [4, 'WMM'], # Starts with 2 pages from 3/7 (one of which is a duplicate)
    '1922-07-03': [4, 'MNAA'], # One noon sheet is with 1/7
    '1922-11-02': [6],
    '1922-12-22': [3, 'MNN'],
    '1923-01-23': [6], # N193-089_0063 is a duplicate
    '1923-02-14': [5, 'NNNAA'], # has no morning, but 3 noons
    '1923-03-23': [5, 'NNNAA'], # has no morning, but 3 noons
    '1923-03-28': [3, 'MNN'],
    '1923-04-10': [2, 'AA'], # No morning or noon
    '1923-04-12': [5, 'NMNAA'], # is out of order
    '1923-04-18': [3, 'MNN'], # No afternoon
    '1923-05-21': [5, 'AMNNA'], # first sheet is not labelled, probably an afternoon as one is missing
    '1923-09-18': [4, 'NNAA'], # No morning
    '1924-02-13': [3, 'MNN'], # No afternoon
    '1924-04-01': [4, 'MNAA'], # 1 noon missing
    # '1924-04-09': 0, # Holiday for arrival of the British fleet
    '1924-04-16': [3, 'MNN'], # No afternoon
    # '1924-04-17': 0, # Thursday before Easter
    # '1924-04-22': 0, # Easter Tuesday
    # '1924-04-23': 0, # Easter Wednesday
    # '1924-10-11': 0, # Stock Exchange closed - http://nla.gov.au/nla.news-article28071778
    '1925-01-27': [5, 'NMNAA'], # is out of order
    '1925-04-01': [3, 'MNN'], # No afternoon
    '1925-04-08': [3, 'MNN'], # No afternoon
    # '1925-04-09': 0, # Thursday before Easter
    # '1925-04-14': 0, # Easter Tuesday
    # '1925-04-15': 0, # Easter Wednesday
    '1925-06-12': [0, ''], # ???
    # 1925-06-13 first page unlabelled -- Saturday
    # '1925-07-23': 0, # Holiday for arrival of American fleet
    '1925-12-23': [4, 'NNN'], # No morning but 3 noons, 100_318 is a duplicate
    '1926-02-05': [5, 'AANMN'], # is out of order
    '1926-02-18': [3, 'MNN'], # No afternoon
    '1926-02-22': [6], # N193-101_0172 is a duplicate
    '1926-03-16': [5, 'AANNM'], #is out of order
    '1926-03-31': [3, 'MNN'],
    # 1926-04-10 is wrongly labelled as March
    '1926-06-24': [5, 'ANNAA'], #is out of order
    '1926-07-09': [5, 'NNNAA'], # has no morning but 3 noons
    '1926-09-30': [6], # N193-103_0352 is a duplicate
    '1926-10-20': [4, 'NNAA'], # No morning
    '1927-03-23': [3, 'MNN'], # no afternoon
    '1927-03-26': [0, ''], #???
    '1927-04-13': [3, 'MNN'], # No afternoon
    # '1927-04-14': 0, # Thursday before Easter
    # '1927-04-19': 0, # Easter Tuesday
    # '1927-04-20': 0, # Easter Wednesday
    '1927-09-01': [6], # N193-107_0235 is a duplicate
    '1927-09-14': [3, 'MNN'], # No afternoon
    '1927-09-30': [6], # N193-107_0351 is a duplicate
    '1927-10-05': [6], # N193-108_0013 is a duplicate
    '1928-01-24': [6], # N193-109_0076 is a duplicate
    '1928-02-09': [3, 'MNN'], # No afternoon
    '1928-02-22': [5, 'NMNAA'], # is out of order
    '1928-02-27': [5, 'NMNAA'], # is out of order
    '1928-03-31': [3], # N193-109_0331 is a duplicate
    '1928-04-04': [3, 'MNN'], # No afternoon
    # '1928-04-05': 0, # Thursday before Easter
    # '1928-04-10': 0, # Easter Tuesday
    # '1928-04-11': 0, # Easter Wednesday
    '1928-05-18': [4, 'NNAA'], # No morning
    '1928-06-22': [4, 'NNAA'], # No morning
    '1928-07-03': [4, 'NNAA'], # No morning
    '1928-07-23': [6], # N193-111_0084 is a duplicate
    '1928-08-01': [3, 'MNN'], # No afternoon
    '1928-08-28': [6], # N193-111_0084 is the back of a page
    '1929-03-01': [4, 'NNAA'], # No morning
    '1929-03-12': [3, 'MNN'], # No afternoon
    '1929-03-27': [3, 'MNN'], # No afternoon
    '1930-02-26': [3, 'MNN'], # No afternoon
    '1930-04-17': [3, 'MNN'], # Thursday before Easter
    # '1930-04-22': 0, # Easter Tuesday
    # '1930-04-23': 0, # Easter Wednesday
    # '1930-04-24': 0, # Day between Easter and Anzac Day
    # '1930-04-26': 0, # Day after Anzac Day? Business resumed on 28 April after extended Easter break - http://nla.gov.au/nla.news-article16691073
    '1930-05-09': [3, 'MNN'], # No afternoon
    '1930-06-27': [4, 'NNAA'], # No morning
    '1930-07-21': [5, 'NAMNA'], # is out of order
    '1930-09-08': [6], # N193-119_0265 is a duplicate
    '1930-12-23': [3, 'MNN'], # No afternoon
    '1931-03-18': [3, 'MNN'], # No afternoon
    '1931-04-01': [2, 'NN'], # No morning or afternoon
    # '1931-04-02': 0, # Thursday before Easter
    # '1931-04-07': 0, # Easter Tuesday
    # '1931-04-08': 0, # Easter Wednesday
    '1931-08-11': [3, 'MNN'], # No afternoon
    '1931-09-15': [3, 'MNN'], # No afternoon
    '1931-10-07': [6], # N193-124_0022 is a duplicate
    '1931-10-08': [4, 'MNNA'], # Missing 1 afternoon
    '1931-11-12': [5, 'NMNAA'], # is out of order
    '1931-12-08': [6], # N193-124_0259 is a duplicate
    '1931-12-23': [3, 'MNN'],
    '1932-03-02': [3, 'MNN'], # No afternoon
    '1932-03-03': [5, 'NNNAA'], # has no morning, but 3 noons
    '1932-03-19': [0, ''], # ??
    '1932-03-23': [3, 'MNN'], # No afternoon
    # '1932-03-24': 0, # Thursday before Easter
    # '1932-03-29': 0, # Easter Tuesday
    # '1932-03-30': 0, # Easter Wednesday
    '1932-04-16': [1, 'M'], # Saturday, missing 1 page
    '1932-04-22': [5, 'NMNAA'], # is out of order
    '1932-11-09': [5, 'NMNAA'], # is out of order
    '1932-12-22': [3, 'NMM'],
    '1933-03-15': [3, 'MNN'], # No afternoon
    '1933-04-07': [3, 'MNN'], # No afternoon
    '1933-04-12': [2, 'MU'], # Morning and one unlabelled
    # '1933-04-13': 0, # Thursday before Easter
    # '1933-04-18': 0, # Easter Tuesday
    # '1933-04-19': 0, # Easter Wednesday
    '1933-04-24': [4, 'MNAA'], # One noon missing
    '1933-04-27': [4, 'MNAA'], # One noon missing
    '1933-09-13': [5, 'NMNAA'], # is out of order
    '1933-12-15': [5, 'ANNAA'], #has 3 afternoons but no morning and is out of order
    '1933-12-22': [3, 'MNN'],
    '1934-02-28': [3, 'MNN'], # No afternoon
    '1934-03-28': [3, 'MNN'],
    '1934-05-02': [4, 'MNAA'], # One noon
    '1934-05-03': [5, 'AANMN'], # is out of order
    '1934-05-04': [4, 'MNAN'], # One afternoon missing and out of order
    '1934-06-08': [4, 'MNAN'], # One afternoon missing and out of order
    #'1934-06-13': 4, # 2 mornings and 2 afternoons, this continues until end of volume
    '1934-06-28': [3, 'MAA'], # 1 morning
    '1934-07-02': [14, 'WWWWWWWWWWMMAA'], # 11 & 12 July are included at the start of this vol out of order
    '1934-07-03': [4, 'NMAA'], # is out of order
    '1934-07-11': [0, ''], # Bound at the start of volume
    '1934-07-12': [0, ''], # Bound at the start of volume
    '1934-07-13': [6, 'MMNNAA'], # 2 morning, 2 noon, 2 afternoon
    '1934-08-08': [4, 'NNAA'], # No morning
    '1934-08-09': [4, 'MMNN'], # No afternoon
    '1934-10-02': [5, 'MNNAA'], # 1 morning
    '1934-11-20': [7], # N193-136_0225 is a duplicate
    # '1934-11-22': 0, # Duke of Gloucester visit & opening of Anzac Memorial
    # '1934-11-24': 0, # Duke of Gloucester visit & opening of Anzac Memorial
    '1934-12-21': [4, 'MMNN'],
    # 1935 IS A MESS!!!!! Lots of sheets are wrongly dated, out of order etc.
    '1935-02-07': [6, 'MMANAN'], # is out of order
    '1935-02-22': [5, 'MNNAA'], # 1 morning
    '1935-03-06': [4, 'MMNN'], # No afternoon
    # '1935-04-18': 0, # Thursday before Easter
    # '1935-04-23': 0, # Easter Tuesday
    # '1935-04-24': 0, # Easter Wednesday
    # '1935-04-25': 0, # Thursday after Easter
    # '1935-05-06': 0, # Holiday for the King's Silver Jubilee
    '1935-07-13': [3], # (Saturday) N193-139_0064 is a duplicate
    '1935-08-02': [8, 'MMNNAAWW'], # 2 noon sheets dated Monday 2 August are inserted after Friday
    '1935-08-05': [0, ''], # 2 (wrongly dated) sheets are with 2 August
    '1935-08-27': [7], # N193-139_0264 is a duplicate
    '1935-09-02': [4, 'MMAA'], # No Noon
    '1935-09-03': [8, 'NNAAWWMM'], # four sheets wrongly labelled 2-9, includes extra two sheets labelled Saturday 2-9, AND out of order 
    '1935-09-07': [0, ''], # The exchange was open, perhaps the two Saturday sheets included with 3-9 are from here
    '1935-10-04': [7, 'MMNNAAW'], # includes an extra sheet dated Tuesday 5 October, afternoon (see below!)
    '1935-10-15': [5, 'MMNNA'], # One afternoon missing -- seems likely it's the one labelled 5 October above
    '1935-10-18': [7, 'MMNNAWA'], # Includes one sheet labelled Saturday 18 October that should be below (also out of order)
    '1935-10-19': [1, 'M'], # See above
    '1935-11-02': [3, 'MWM'], # Includes an extra sheet dated Monday 4 November noon
    '1935-11-04': [7, 'MMMNNAA'], # 3 mornings, no obvious duplicates
    '1935-11-15': [6, 'NMMNAA'], # is out of order
    '1935-11-26': [6, 'NNMMAA'], # is out of order & wrongly dated
    '1935-11-27': [5, 'MNNAA'], # Missing one morning
    '1935-12-02': [5, 'MMNAA'], # Missing one noon
    '1935-12-04': [5, 'MMNAA'], # Missing one noon
    '1936-01-21': [1, 'M'], # One morning sheet only
    '1936-01-22': [4, 'MMAA'], # No noons
    '1936-02-26': [4, 'MMNN'], # No afternoon
    '1936-04-04': [3, 'MMW'], # Includes an extra sheet for Tuesday 5 April (p21)??
    '1936-04-08': [4, 'MMNN'], # No afternoon
    # '1936-04-09': 0, # Thursday before Easter
    # '1936-04-14': 0, # Easter Tuesday
    # '1936-04-15': 0, # Easter Wednesday
    '1936-04-20': [6, 'MMNNAM'], # - last sheet says morning (but there's already two mornings)??
    '1936-05-05': [5, 'MMNNA'], # One afternoon missing
    '1936-05-19': [5, 'MNNAA'], # One morning missing
    # 1936-05-20 last sheet is labelled Monday 20th
    '1936-05-26': [7], # N193-142_0217 is a duplicate
    '1936-06-01': [6, 'MMNNAM'], # only one afternoon and last sheet is labelled morning 
    '1936-08-26': [6, 'MMNNAM'], #  only one afternoon and last sheet is labelled morning
    '1936-09-22': [7], #  N193-143_0375 is a duplicate
    '1936-11-02': [4, 'MMNN'], # No afternoon, also some sheets labelled 2 October???
    # '1936-12-14': [0, ''], # New King's birthday https://trove.nla.gov.au/newspaper/article/17310569
    # '1936-12-19': 0, # See https://trove.nla.gov.au/newspaper/article/17308675
    '1936-12-23': [4, 'MMNN'],
    '1937-01-18': [5, 'MMNNM'], # No afternoons, but an extra morning (at the end)
    # 1937-01-25 first sheet is labelled Monday (should be Tuesday)
    '1937-02-25': [4, 'MMNN'], # No afternoon
    '1937-03-24': [4, 'MMNN'],
    '1937-04-15': [9, 'MMMNNNAAM'], # out of order
    '1937-04-20': [10, 'MMMMNNNAAA'], # 4 mornings, 3 noons, 3 afternoons
    '1937-05-28': [7, 'MMNNAAA'], # 2 morning, 2 noon, 3 afternoons
    '1937-06-24': [9, 'MMMNNNAAM'], # last sheet is labelled noon, but should be afternoon?
    '1937-08-09': [6, 'MMMNNN'], # No afternoon
    '1937-12-23': [6, 'MMMNNN'],
    '1938-04-13': [6, 'MMMNNN'], #  No afternoon
    # '1938-04-14': 0, # Thursday before Easter
    # '1938-04-19': 0, # Easter Tuesday
    # '1938-04-20': 0, # Easter Wednesday
    '1938-05-23': [9, 'MMMNNNAAM'], # last sheet labelled morning, should be afternoon? 
    '1938-07-04': [8, 'MMMNNAAA'], # 1 noon missing
    '1938-09-09': [9, 'MMMNNNAAM'], # last sheet labelled morning, should be afternoon?
    '1938-10-13': [9, 'MMMNNNAAM'], # last sheet labelled morning, should be afternoon? 
    '1938-10-26': [9, 'MMMNNNAAM'], #  last sheet labelled morning, should be afternoon? 
    '1938-10-28': [10, 'MMMNNNNAAA'], # 4 noons
    '1938-11-01': [8, 'MMMNNAAA'], # 2 noons
    '1938-11-24': [9, 'MMMNNNMMM'], # -- don't appear to be duplicates
    '1938-12-22': [6, 'MMMNNN'],
    '1939-03-08': [6, 'MMMNNN'], # no afternoon
    '1939-04-11': [3, 'AAA'], # afternoon only
    '1939-04-24': [9, 'MMMNNNAAM'], # last sheet labelled morning, should be afternoon? 
    '1939-05-01': [9, 'MMMNNNAAM'], # last sheet labelled morning, should be afternoon? 
    '1939-05-10': [6, 'NNNAAA'], # No morning
    '1939-06-01': [9, 'MMMNNNAAM'], # last sheet labelled morning, should be afternoon? 
    '1939-06-29': [6, 'NNNAAA'], # No morning
    '1939-07-11': [9, 'MMMNNNAAM'], # last sheet labelled morning, should be afternoon?
    '1939-09-01': [8, 'MMMNNNAA'], # 1 afternoon missing
    # '1939-09-02': 0, # Closed due to war - http://nla.gov.au/nla.news-article17620079
    # '1939-09-04': 0, # As above
    '1939-09-27': [10], # N193-155_0582 is a duplicate
    '1939-11-01': [10], # N193-156_0206 is a duplicate
    '1939-12-12': [6, 'NNNAAA'], # No morning
    '1939-12-22': [6, 'MMMNNN'], # No afternoon
    '1940-03-13': [6, 'MMMNNN'], # No afternoon
    '1940-03-19': [9, 'AAANNNMMM'], # is backwards
    '1940-03-21': [6, 'MMMNNN'], # No afternoon
    '1940-07-01': [8, 'MMNNNAAA'], # 1 morning missing
    '1940-07-26': [10], # N193-159_0187 is a duplicate
    '1940-08-02': [8, 'MMNNNAAA'], # 1 morning missing
    '1940-08-08': [10, 'MMMMNNNAAA'], # 4 mornings
    '1940-12-09': [10], # N193-160_0467 is a duplicate
    '1940-12-17': [6, 'MMMNNN'], # no afternoon
    '1941-01-06': [6, 'MMMNNN'], # no afternoon
    '1941-01-20': [12, 'AAAWWWMMMNNN'], # afternoon only -- see below?
    '1941-01-21': [6, 'MMMNNN'], # This includes 3 morning and 3 noon sheets that were originally labelled Monday, but then crossed out and labelled Tuesday (so there's 6 mornings and 6 noons) -- also out of order
    '1941-02-15': [0, ''], # ? Seems to have been open https://trove.nla.gov.au/newspaper/article/17720991
    '1941-03-04': [10], #  N193-161_0401 is a duplicate
    '1941-03-10': [10], # N193-161_0441 is a duplicate
    '1941-04-10': [6, 'MMMNNN'], # No afternoon
    '1941-04-19': [0, ''], # ?
    '1941-04-21': [6, 'MMMNNN'], #  No afternoon
    '1941-04-23': [6, 'MMMNNN'], #  No afternoon
    '1941-04-29': [6, 'MMMNNN'], #  No afternoon
    '1941-04-30': [10], # N193-162_0158 is a duplicate
    '1941-07-03': [9, 'AAAMMMNNN'], # is out of order
    '1941-08-30': [16, 'MMMWWWWWWWWWWWWW'], # last 13 pages are an inserted pamphlet
    '1941-09-08': [8, 'MMMNNAAA'], # 1 noon missing
    '1941-09-16': [6, 'NNNAAA'], # no morning
    '1941-11-17': [9, 'MMMNNNAAN'], # last sheet is labelled Noon, presumably should be afternoon
    '1941-12-03': [6, 'NNNAAA'], # no morning
    '1941-12-19': [6, 'MMMNNN'], # no afternoon
    '1942-01-02': [8, 'MMNNNAAA'], # 1 morning missing
    '1942-02-11': [7, 'MNNNAAA'], # 2 mornings missing
    '1942-02-20': [2, 'MA'], # MA only
    '1942-02-21': [1, 'M'], # M
    '1942-02-23': [2, 'MA'], # MA only
    '1942-02-24': [1, 'M'], # M
    '1942-02-25': [2, 'MA'], # MA only
    '1942-02-26': [2, 'MA'], # MA only
    '1942-02-27': [2, 'MA'], # MA only
    '1942-02-28': [1, 'M'], # M
    '1942-03-02': [2, 'MA'], # MA only
    '1942-03-03': [2, 'MA'], # MA only
    '1942-03-04': [2, 'MA'], # MA only
    '1942-03-05': [2, 'MA'], # MA only
    '1942-03-06': [2, 'MA'], # MA only
    '1942-03-07': [1, 'M'], # M
    '1942-03-09': [2, 'MA'], # MA only
    '1942-03-10': [2, 'MA'], # MA only
    '1942-06-24': [3, 'MMM'], # No afternoon
    # 1942-08-10 to 1942-08-21 Not in order, AAAMMM (except for Saturday of course)
    '1942-08-10': [6, 'AAAMMM'],
    '1942-08-11': [6, 'AAAMMM'],
    '1942-08-12': [6, 'AAAMMM'],
    '1942-08-13': [6, 'AAAMMM'],
    '1942-08-14': [6, 'AAAMMM'],
    '1942-08-17': [6, 'AAAMMM'],
    '1942-08-18': [6, 'AAAMMM'],
    '1942-08-19': [6, 'AAAMMM'],
    '1942-08-20': [6, 'AAAMMM'],
    '1942-08-21': [6, 'AAAMMM'],
    '1942-11-23': [6, 'AAAMMM'], # out of order AAAMMM
    # '1942-12-28': 0, # Holiday instead of new year's day http://nla.gov.au/nla.news-article17821583
    '1943-01-11': [7], # N193-169_0046 is a duplicate
    '1943-03-13': [2, 'MM'], # 1 Saturday missing
    '1943-05-14': [6, 'AAAMMM'], # is out of order AAAMMM
    '1943-06-23': [6, 'MMAAAM'], #is out of order MMAAAM
    '1943-07-05': [6, 'MAAAMM'], # is out of order MAAAMM
    '1943-07-06': [5, 'MMAAA'], # MMAAA
    '1943-10-13': [6, 'AMMMAA'], # is out of order AMMMAA
    '1943-10-15': [6, 'AAAMMM'], # is out of order AAAMMM
    '1943-10-18': [6, 'AAAMMM'], # is out of order AAAMMM
    '1943-11-22': [9, 'MMMAAAAAA'], # MMMAAAAAA - extra afternoons likely from 23-11
    '1943-11-23': [3, 'MMM'], # MMM
    '1943-12-17': [5, 'MMMAA'], # MMMAA
    '1943-12-24': [3, 'MMM'], # MMM
    '1944-03-31': [29, 'MMMAAAWWWWWWWWWWWWWWWWWWWWWWW'], # NOTE vol 173 pp 415-437 are 'Register of Sales' from February
    '1944-04-06': [3, 'MMM'], # MMM
    #'1944-04-11': 0, # Easter Tuesday
    '1944-12-22': [3, 'MMM'], # MMM
    '1945-02-01': [7], # N193-177_0132 is a duplicate
    '1945-03-29': [3, 'MMM'], # MMM
    '1945-04-27': [7], # N193-178_0107 is a duplicate
    # 1945-05-19 first sheet wrongly labelled 18 rather than 19
    '1945-07-30': [5, 'MMMAA'], # MMMAA - see 3 August
    '1945-07-31': [0, ''], # In 3 August
    '1945-08-03': [13, 'MWWWWWWWMMAAA'],
    '1945-08-15': [5, 'MMMAA'],
    '1945-09-29': [3, 'MMM'],
    '1945-12-21': [3, 'MMM'],
    '1946-04-18': [3, 'MMM'], # MMM
    # '1946-04-23': 0, # Easter Tuesday
    # '1946-04-24': 0, # Easter Wednesday
    '1946-05-15': [3, 'AAA'], # AAA
    '1946-06-03': [7], # N193-182_0260 is a duplicate
    '1946-08-27': [0, ''], # Seems to have been opem
    '1946-08-28': [0, ''],
    '1946-08-29': [0, ''],
    '1946-08-30': [0, ''],
    '1946-08-31': [0, ''],
    # ALL OF SEPTEMBER 1946 IS MISSING
    '1946-09-01': [0, ''],
    '1946-09-02': [0, ''],
    '1946-09-03': [0, ''],
    '1946-09-04': [0, ''],
    '1946-09-05': [0, ''],
    '1946-09-06': [0, ''],
    '1946-09-07': [0, ''],
    '1946-09-09': [0, ''],
    '1946-09-10': [0, ''],
    '1946-09-11': [0, ''],
    '1946-09-12': [0, ''],
    '1946-09-13': [0, ''],
    '1946-09-14': [0, ''],
    '1946-09-16': [0, ''],
    '1946-09-17': [0, ''],
    '1946-09-18': [0, ''],
    '1946-09-19': [0, ''],
    '1946-09-20': [0, ''],
    '1946-09-21': [0, ''],
    '1946-09-23': [0, ''],
    '1946-09-24': [0, ''],
    '1946-09-25': [0, ''],
    '1946-09-26': [0, ''],
    '1946-09-27': [0, ''],
    '1946-09-28': [0, ''],
    '1946-09-30': [0, ''],
    '1946-11-25': [7], # N193-184_0259 is a duplicate
    '1946-12-23': [4, 'MMM'], # MMM and N193-184_0388 is a duplicate
    '1947-03-06': [7], # N193-185_0282 is a duplicate
    '1947-04-03': [3, 'MMM'], # MMM
    # '1947-04-08': 0, # Easter Tues
    # '1947-04-09': 0, # Easter Wed
    '1947-07-26': [4], # N193-187_0125 is a duplicate
    '1947-10-08': [7], # N193-188_0034 is a duplicate
    '1947-10-09': [6, 'MMMAAM'], # last sheet is labelled morning MMMAAM
    '1947-10-25': [2, 'MM'], # Saturday mssing one morning
    '1947-12-23': [3, 'MMM'], # wrongly labelled Thursday
    '1948-02-18': [7], # N193-189_0188 is a duplicate
    '1948-03-25': [3, 'MMM'], # MMM
    '1948-07-22': [7, 'MMMAAAA'], # MMMAAAA
    '1948-12-23': [4, 'MMMM'], # MMMM
    '1949-04-14': [4, 'MMMM'], # MMMM
    #'1949-04-19': 0, # Easter Tues
    #'1949-04-20': 0, # Easter Wed
    # DO THIS!!!!!!!
    # NOVEMBER and DECEMBER 1949 are jumbled and often wrongly labelled
    '1949-11-08': [32, 'MMMMAAAAWWWWWWWWWWWWWWWWWWWWWWWW'],
    '1949-11-14': [14, 'MMMWWWWWWMAAAA'],
    '1949-11-21': [16, 'MMMMAAAAWWWWWWWW'],
    '1949-11-24': [9], # 342 is dupe
    '1949-12-08': [0, ''], # see 8 Nov
    '1949-12-09': [0, ''], # see 8 Nov
    '1949-12-13': [0, ''], # see 8 Nov
    '1949-12-14': [0, ''], # see 14 Nov
    '1949-12-19': [0, ''], # see 21 Nov
    '1949-12-22': [4, 'MMMM'],
    '1950-04-06': [4, 'MMMM'], # MMMM
    #'1950-04-11': 0, # Easter Tues
    #'1950-04-12': 0, # Easter Wed
    # Volume 199 is different so I haven't included it
}