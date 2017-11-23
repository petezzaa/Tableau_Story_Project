import csv
from pprint import pprint

#put data into a list of dictionaries
f = open('C:\Users\Quentin\Documents\Udacity\Project_Tableau\\Missile Tests (north_korea_missile_test_database)_2.csv')
reader = csv.DictReader(f)
dict_list = []
for line in reader:
    print dict_list.append(line)

#clean data
for d in dict_list:
    type = d['Missile Type']
    dist = d['Distance Travelled - Split 1']
    apogee = d['Apogee - Split 1']
    #change landing location to Pacific Ocean
    if d['Landing Location'] == '330km east of Hachinohe and 4000 km out into Pacific Ocean':
        d['Landing Location'] = 'Pacific Ocean'
    #replace missing distance data with median distance for each missile type
    if d['Test Outcome'] == 'Success':
        if d['Distance Travelled'] == 'Unknown':
            if type == 'SLV':
                d['Distance Travelled - Split 1'] = 1380
            elif type == 'MRBM':
                d['Distance Travelled - Split 1'] = 1000
            elif type == 'ICBM':
                d['Distance Travelled - Split 1'] = 966
            elif type == 'IRBM':
                d['Distance Travelled - Split 1'] = 594
            elif type == 'SRBM':
                d['Distance Travelled - Split 1'] = 490
            elif type == 'SLBM':
                d['Distance Travelled - Split 1'] = 265
        # replace missing apogee data with median apogee for each missile type
        if d['Apogee'] == 'Unknown':
            if type == 'SLV':
                d['Apogee - Split 1'] = 502
            elif type == 'MRBM':
                d['Apogee - Split 1'] = 150
            elif type == 'ICBM':
                d['Apogee - Split 1'] = 3263
            elif type == 'IRBM':
                d['Apogee - Split 1'] = 550
            elif type == 'SRBM':
                d['Apogee - Split 1'] = 150
            elif type == 'SLBM':
                d['Apogee - Split 1'] = 10

#pprint(dict_list)

#write cleaned data to a csv
keys = dict_list[0].keys()
with open('missile_data_(clean).csv', 'wb') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(dict_list)

f.close()

print 'All Done!'