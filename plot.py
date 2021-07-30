from os import listdir
import csv
from os.path import isfile, join
import os


csv_path = os.path.dirname(os.path.abspath(__file__))+"/Years/"
print(csv_path)
out_path=csv_path+"ML_FILE.csv"
file = [f for f in listdir(csv_path) if isfile(join(csv_path,f))]

with  open(out_path,'w') as w_csvfile:
    field_name=['Year','Month','Day','Value']
    row1 = {}
    writer_csv = csv.DictWriter(w_csvfile,field_name,delimiter=',')
    writer_csv.writeheader()
    months_count = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
    for filename in file:
        file_input = csv_path  + filename
        with open(file_input) as r_csvfile:
            reader=csv.DictReader(r_csvfile)
            for row in reader:
                for mon in months_count:
                    row1['Year'] = filename.replace("'","").replace(".csv","")
                    row1['Month'] = months_count.index(mon) +1
                    row1['Day'] = row[filename.replace(".csv","")]
                    # if row[mon] == "XX" or row[mon] == "##" or row[mon]=='?' or row[mon]=='**':
                    if not row[mon].isdigit():
                        row1['Value'] = 0
                    else:
                        row1['Value'] = row[mon]
                    writer_csv.writerow(row1)
                
