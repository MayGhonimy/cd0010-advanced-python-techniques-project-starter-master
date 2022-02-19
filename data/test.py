import json 

with open('cad.json', 'r') as infile:
    contents = json.load(infile)
    for val in contents['data']:
        
        if '2000-Jan-01' in val[3] and val[0]=='2002 PB':
            print (val[7])
