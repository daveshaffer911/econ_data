def text_repl(string_item):
    return (string_item.replace('PEAGE', 'PRTAGE').replace('PTERNHLY', 'PRERNHLY')
            .replace('PTERNWA', 'PRERNWA').replace('GEMETSTA', 'GTMETSTA')
            .replace('PERACE', 'PRDTRACE').replace('PTDTRACE', 'PRDTRACE')
            .replace('HRHHID (partII)', 'HRHHID2').replace('PRORIGIN', 'PRDTHSP')
            .replace('PTIO1OCD', 'PEIO1OCD').replace('PUAFEVER', 'PEAFEVER')
            .replace('PTERN2', 'PUERN2')) #.replace('\x0cRNUMHOU', 'HRNUMHOU')


VarList = ['PWORWGT', 'PWCMPWGT', 'PWLGWGT', 'PRERNWA',
           'PTERNWA', 'PWSSWGT', 'HRHHID (partII)', 
           'HRHHID2', 'HRYEAR', 'HRYEAR4', 'PRERNHLY',
           'PTERNHLY', 'HRMONTH', 'PESEX', 'PEMLR',
           'PENLFRET', 'PENLFACT', 'PRDISC', 'GESTFIPS',
           'HRMIS', 'PRCOW1', 'PRFTLF', 'PREMPNOT', 
           'PRSJMJ', 'PEEDUCA', 'PENATVTY',
           'PRWKSTAT', 'PRMJOCC1', 'GTMETSTA', 'GEMETSTA',
           'PEDWWNTO', 'PRUNTYPE', 'PRMJIND1', 'GTCBSA',
           'PERACE', 'PTDTRACE', 'PRDTRACE', 'PRORIGIN',
           'HUHHNUM', 'PRDTHSP', 'PRCHLD', 'PRTAGE',
           'PEAGE', 'PULINENO', 'PRWNTJOB', 'PEERNLAB',
           'PRUNEDUR', 'PEHRUSL1', 'PRMARSTA', 'PRCITSHP',
           'PRDTOCC1', 'PRDTIND1', 'PEHRUSL2', 'PEHRUSLT',
           'PEIO1COW', 'PEIO1OCD', 'PEIO1ICD', 'PEIO2COW',
           'HRHHID', 'HRSAMPLE', 'HRSERSUF', 'PTIO1OCD',
           'PRDISFLG', 'PUAFEVER', 'PEAFEVER', 'PECERT1',
           'GTCSA', 'PEHRACTT', 'PEHRACT1', 'PEERNCOV',
           'PESCHENR', 'PRNMCHLD', 'PTERN2', 'PEHRACT2',
           'PUERN2', 'PRAGNA', 'QSTNUM', 'OCCURNUM']
            # 'HRNUMHOU', 'HWHHWGT', '\x0cRNUMHOU', 'HRHTYPE' 

DataDict = {'January_2017_Record_Layout.txt':
            {'start': '2017-01-01', 'end': '2018-12-01',
             're': f'({"|".join(VarList)})\s+(\d+)\s+.*?\t+.*?(\d\d*).*?(\d\d+)'},
            'January_2015_Record_Layout.txt':
            {'start': '2015-01-01', 'end': '2016-12-31',
             're': f'({"|".join(VarList)})\s+(\d+)\s+.*?\t+.*?(\d\d*).*?(\d\d+)'},
            'January_2014_Record_Layout.txt':
            {'start': '2014-01-01', 'end': '2014-12-31',
             're': f'({"|".join(VarList)})\s+(\d+)\s+.*?\t+.*?(\d\d*).*?(\d\d+)'},
            'January_2013_Record_Layout.txt':
            {'start': '2013-01-01', 'end': '2013-12-31',
             're': f'({"|".join(VarList)})\s+(\d+)\s+.*?\t+.*?(\d\d*).*?(\d\d+)'},
            'may12dd.txt':
            {'start': '2012-05-01', 'end': '2012-12-31',
             're': f'({"|".join(VarList)})\s+(\d+)\s+.*?\t+.*?(\d\d*).*?(\d\d+)'},
            'jan10dd.txt':
            {'start': '2010-01-01', 'end': '2012-04-30',
             're': f'\n(?:\x0c)?({"|".join(VarList)})\s+(\d+)\s+.*? \s+.*?(\d\d*).*?(\d\d+)'},
            'jan09dd.txt':
            {'start': '2009-01-01', 'end': '2009-12-31',
             're': f'\n(?:\x0c)?({"|".join(VarList)})\s+(\d+)\s+.*? \s+.*?(\d\d*).*?(\d\d+)'},
            'jan07dd.txt':
            {'start': '2007-01-01', 'end': '2008-12-31',
             're': f'\n(?:\x0c)?({"|".join(VarList)})\s+(\d+)\s+.*? \s+.*?(\d\d*).*?(\d\d+)'},
            'augnov05dd.txt':
            {'start': '2005-08-01', 'end': '2006-12-31',
             're': f'\n(?:\x0c)?({"|".join(VarList)})\s+(\d+)\s+.*? \s+.*?(\d\d*).*?(\d\d+)'},
            'may04dd.txt':
            {'start': '2004-05-01', 'end': '2005-7-31',
             're': f'\n(?:\x0c)?({"|".join(VarList)})\s+(\d+)\s+.*? \s+.*?(\d\d*).*?(\d\d+)'},
            'jan03dd.txt':
            {'start': '2003-01-01', 'end': '2004-04-30',
             're': f'\n(?:\x0c)?({"|".join(VarList)})\s+(\d+)\s+.*? \s+.*?(\d\d*).*?(\d\d+)'},
            'jan98dd.asc':
            {'start': '1998-01-01', 'end': '1999-10-31',
             're': 'D (\w+)\s+(\d{1,2})\s+(\d+)\s+'},
            'jan98dd2.asc':
            {'start': '1999-11-01', 'end': '2002-12-31',
             're': 'D (\w+)\s+(\d{1,2})\s+(\d+)\s+'},
            'sep95_dec97_dd.txt':
            {'start': '1995-09-01', 'end': '1997-12-31',
             're': f'\n(?:\x0c)?({"|".join(VarList)})\s+(\d+)\s+.*? \s+.*?(\d\d*).*?(\d\d+)'},
            'jun95_aug95_dd.txt':
            {'start': '1995-06-01', 'end': '1995-08-31',
             're': f'\n(?:\x0c)?({"|".join(VarList)})\s+(\d+)\s+.*? \s+.*?(\d\d*).*?(\d\d+)'},
            'apr94_may95_dd.txt':
            {'start': '1994-04-01', 'end': '1995-05-31',
             're': f'\n(?:\x0c)?({"|".join(VarList)})\s+(\d+)\s+.*? \s+.*?(\d\d*).*?(\d\d+)'},
            'jan94_mar94_dd.txt':
            {'start': '1994-01-01', 'end': '1995-03-31',
             're': f'\n(?:\x0c)?({"|".join(VarList)})\s+(\d+)\s+.*? \s+.*?(\d\d*).*?(\d\d+)'},
#            'cps89.ddf':
#            {'start': '1989-01-01', 'end': '1991-12-31',
#             're': '(\w{1,2}[\$\-%]\w*|PADDING)\s*CHARACTER\*(\d{3})\s*\.{0,1}\s*\((\d*):(\d*)\).*'},
#            'cps92.ddf':
#            {'start': '1992-01-01', 'end': '1993-12-31',
#             're': '(\w{1,2}[\$\-%]\w*|PADDING)\s*CHARACTER\*(\d{3})\s*\.{0,1}\s*\((\d*):(\d*)\).*'}
            }
             
             
StatesMap = {1: 'AL',
             30: 'MT',
             2: 'AK',
             31: 'NE',
             4: 'AZ',
             32: 'NV',
             5: 'AR',
             33: 'NH',
             6: 'CA',
             34: 'NJ',
             8: 'CO',
             35: 'NM',
             9: 'CT',
             36: 'NY',
             10: 'DE',
             37: 'NC',
             11: 'DC',
             38: 'ND',
             12: 'FL',
             39: 'OH',
             13: 'GA',
             40: 'OK',
             15: 'HI',
             41: 'OR',
             16: 'ID',
             42: 'PA',
             17: 'IL',
             44: 'RI',
             18: 'IN',
             45: 'SC',
             19: 'IA',
             46: 'SD',
             20: 'KS',
             47: 'TN',
             21: 'KY',
             48: 'TX',
             22: 'LA',
             49: 'UT',
             23: 'ME',
             50: 'VT',
             24: 'MD',
             51: 'VA',
             25: 'MA',
             53: 'WA',
             26: 'MI',
             54: 'WV',
             27: 'MN',
             55: 'WI',
             28: 'MS',
             56: 'WY',
             29: 'MO'}

RegionsMap = {'AK': 'West',
              'HI': 'West',
              'WA': 'West',
              'OR': 'West',
              'CA': 'West',
              'NV': 'West',
              'ID': 'West',
              'MT': 'West',
              'UT': 'West',
              'AZ': 'West',
              'CO': 'West',
              'WY': 'West',
              'NM': 'West',
              'ND': 'Midwest',
              'SD': 'Midwest',
              'NE': 'Midwest',
              'KS': 'Midwest',
              'MN': 'Midwest',
              'IA': 'Midwest',
              'MO': 'Midwest',
              'WI': 'Midwest',
              'IL': 'Midwest',
              'IN': 'Midwest',
              'MI': 'Midwest',
              'OH': 'Midwest',
              'TX': 'South',
              'OK': 'South',
              'AR': 'South',
              'LA': 'South',
              'MS': 'South',
              'AL': 'South',
              'TN': 'South',
              'KY': 'South',
              'WV': 'South',
              'VA': 'South',
              'MD': 'South',
              'DE': 'South',
              'DC': 'South',
              'NC': 'South',
              'SC': 'South',
              'GA': 'South',
              'FL': 'South',
              'PA': 'Northeast',
              'NJ': 'Northeast',
              'NY': 'Northeast',
              'CT': 'Northeast',
              'RI': 'Northeast',
              'MA': 'Northeast',
              'NH': 'Northeast',
              'VT': 'Northeast',
              'ME': 'Northeast'}
          
