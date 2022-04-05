import csv
import os
from sqlite3 import Timestamp
import sys
import argparse
import datetime
import pytz

## Function to check if the log file passed exists or not

def file_status(file_name):
    if not os.path.isfile(file_name):
        print("The file {}, doesnt exist".format(file_name))
        sys.exit(1)

#Function to convert timestamp to requored format in pst
def date_converter(time_stamp):
    date_utc = datetime.datetime.utcfromtimestamp(int(time_stamp)/1000.0)
    pst_time = date_utc.astimezone(pytz.timezone('US/Pacific'))
    return pst_time.strftime("%Y-%m-%d %H:%M:%S")

#Function to parse log and print errors

def parse_log(log_parse_file):
    with open(log_parse_file, mode='r') as csv_file:
        count = 0
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if 200 < int(row['responseCode']) > 299:
                pst_time =  date_converter(row["timeStamp"])
                print("{}  {} {} {} - {} PST".format(row['label'], row['responseCode'], row['responseMessage'], row['failureMessage'], pst_time))

if __name__ == "__main__":
    my_parser = argparse.ArgumentParser(description="""Script to parse comma delimtaed log file with 
    headers timeStamp,elapsed,label,responseCode,responseMessage,threadName,dataType,success,failureMessage,bytes,sentBytes,grpThreads,allThreads,URL,Latency,IdleTime,Connect

    Script will print out the label, response code, response message, failure message for any any non-successful endpoint responses and in human-readable format in PST timezone
    """)

    my_parser.add_argument('-i','--input_file', required=True)

    args = my_parser.parse_args()

    log_file = args.input_file    

    file_status(log_file)
    parse_log(log_file)

