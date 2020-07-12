#!/usr/bin/python3
import subprocess
import json
import csv
import pandas as pd
from io import StringIO 
from pprint import pprint 
#YAML config file for 
#servers 
#endpoint for elastic definition


#Other idea would be a script to install speedtest-cli or have it contained somehow if it were some virtual environment, Ask Michael

#Check for Pandas Dataframe instead of lists

def command ( args ):
    output=subprocess.check_output(args,  stdin=None, stderr=None, shell=False, cwd=None, encoding=None, errors=None, universal_newlines=None, timeout=None, text=None,).decode("utf-8").strip()
    return output

def parse_csv_output_string(output_string):
    output_lines=output_string.splitlines()
    output_list=[]
    for line in  csv.reader(output_lines, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True):
            output_list=line
            break
    return output_list

args=["speedtest-cli","--csv-header" ]
#speedtest-cli --server 14232
output=command(args) 
output_headers=parse_csv_output_string(output)
args=["speedtest-cli","--server", "14232","--csv"]

#speedtest-cli --server 14232
output=subprocess.check_output(args,  stdin=None, stderr=None, shell=False, cwd=None, encoding=None, errors=None, universal_newlines=None, timeout=None, text=None,).decode("utf-8").strip()
#output_list=csv.reader(output, quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True)

#Michael's suggestions start
#print(type(output), output)

#data = StringIO(output)
#df = pd.read_csv(data, sep=",")
#print(df)

#data = output
#df = pd.DataFrame([x.split(',') for x in data.split('')])
#print(df)

#Michael's suggestions end

output_lines=output.splitlines()
output_list=[]
#How can I do this without for loop if there will only be one line always?
for l in  csv.reader(output_lines, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True):
    output_list=l

print(output_list)

resulting_string=dict(zip(output_headers,output_list))
pprint(resulting_string)
