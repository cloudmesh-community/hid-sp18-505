import pymongo
from pymongo import MongoClient
from data.convert_coords import utm_to_latlon
from os import environ

if environ.get('MONGO_HOST') is not None:
    MONGO_HOST = environ.get('MONGO_HOST')
else:
    MONGO_HOST = '127.0.0.1'

client = MongoClient(MONGO_HOST, 27017)
db = client.swagger
raingages = db.raingages

# Remove all raingage docs
raingages.remove({})

with open('./data/raingages.csv', 'r') as f:
    line_count = 0
    for l in f.readlines():
        if line_count > 0:
            (code, name, longitude, latitude) = l.strip().split('|')
            latlon = utm_to_latlon(12, float(longitude), float(latitude), 12)            
            print(latlon)
            raingage = {
             'code': code, 
             'name': name, 
             'longitude': latlon[1], 
             'latitude': latlon[0]
            }

            raingages.insert_one(raingage)

        line_count += 1

MONTH_CHOICES = [
    ['JAN', 'JAN'],
    ['FEB', 'FEB'],
    ['MAR', 'MAR'],
    ['APR', 'APR'],
    ['MAY', 'MAY'],
    ['JUN', 'JUN'],
    ['JUL', 'JUL'],
    ['AUG', 'AUG'],
    ['SEP', 'SEP'],
    ['OCT', 'OCT'],
    ['NOV', 'NOV'],
    ['DEC', 'DEC'],
]

station_name_map = [
    {"id": "white", "name": "Whitehouse"},
    {"id": "watre", "name": "Water Retention"},
    {"id": "sw", "name": "Southwest"},
    {"id": "scs5n", "name": "SCS-5N"},
    # {"id": "scs#1", "name": "SCS" },
    {"id": "scs#1", "name": "SCS #1"},
    {"id": "ruela", "name": "Ruelas"},
    {"id": "roden", "name": "Rodent"},
    {"id": "robin", "name": "Robinson"},
    {"id": "road", "name": "Road"},
    {"id": "past3", "name": "Pasture 3"},
    {"id": "parke", "name": "Parker"},
    {"id": "pa11a", "name": "Pasture 11A"},
    {"id": "nw", "name": "Northwest"},
    {"id": "nrnch", "name": "North Ranch"},
    {"id": "ne", "name": "Northeast"},
    {"id": "muhle", "name": "Muhlenbergia"},
    {"id": "mcgib", "name": "McGibbon"},
    {"id": "limst", "name": "Limestone"},
    {"id": "johns", "name": "Johnson Ranch"},
    {"id": "ibp", "name": "IBP"},
    {"id": "hughe", "name": "Hughes"},
    {"id": "huerf", "name": "Huerfano"},
    {"id": "grari", "name": "Gravelly Ridge"},
    {"id": "fores", "name": "Forest"},
    {"id": "flori", "name": "Florida"},
    {"id": "fagan", "name": "Fagan"},
    {"id": "eriop", "name": "Eriopoda"},
    {"id": "desst", "name": "Desert Station"},
    {"id": "desri", "name": "Desert Rim"},
    {"id": "desgr", "name": "Desert Grassland"},
    {"id": "choll", "name": "Cholla"},
    {"id": "box", "name": "Box"},
    {"id": "amado", "name": "Amado"},
    {"id": "airst", "name": "Airstrip"},
    {"id": "164", "name": "Enclosure 164"},
    {"id": "45", "name": "Enclosure 45"},
    {"id": "41", "name": "Enclosure 41"},
    {"id": "205", "name": "Enclosure 205"},
    {"id": "18", "name": "Enclosure 18"},
    {"id": "131", "name": "Encl. No. 131"},
]

def find_station_name(name):
    station_name = None

    for s in station_name_map:
        if s['id'] == name:
            station_name = s['name']

    return station_name

def precip_values(values):
    output = []

    for k, v in enumerate(values):
        if v in ['-9999', '']:
            output.append(None)
        else:
            output.append(float(int(v) / 100.00))

    return output

precip_events = db.precipevents
precip_events.remove({})
with open('./data/precip.csv', 'r') as f:
    line_count = 0
    for line in f.readlines():
        if line_count > 0:
            values = line.strip().split('|')
            station = values[0].lower()
            year = values[1]
            station_name = None

            station_id_list = list(i['id'] for i in station_name_map)
            if station in station in station_id_list:
                station_name = find_station_name(station)
            else:
                station_name = station

            precip_vals = precip_values(values[2:])
            for k, v in enumerate(precip_vals):
                month = MONTH_CHOICES[k][0]
                precip = v
                precip_event = {
                    'gage': station_name,
                    'year': year,
                    'month': month,
                    'precip': precip
                }

                precip_events.insert_one(precip_event)            

        line_count += 1