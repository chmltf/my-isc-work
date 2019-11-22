import datetime

def convert_time(tm):
    tm = datetime.datetime.strptime(tm, "%Y-%m-%dT%H:%M:%S.%f")
    return tm

def convert_temp(temp):
    value = temp[2:-3].strip("+").strip("C").lstrip("0")
    return float(value) + 273.15

infile = 'temp_output.csv'
outfile = 'temp_output.nc'

from csv import reader

#parse the data into Python lists
times = []
temps = []

#open infile and read data into lists
with open(infile, 'rt') as tsvfile:
    tsvreader = reader(tsvfile, delimiter=' ')
    for row in tsvreader:
        times.append(convert_time(row[0]))
        temps.append(convert_temp(row[1]))


print(times, temps)
