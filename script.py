import csv
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument("file_path")
parser.add_argument("table_name")
args = parser.parse_args()
print(args.file_path)


with open(args.file_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    result = ""
    for row in csv_reader:
        closure_sym = "'"
        if line_count == 0:
            closure_sym = "`"
            result = "INSERT INTO " + args.table_name

        result = result + "("
        for val in row:
            
            result = result + closure_sym + val + closure_sym + "," 
        result = result[:-1] + "),\n"

        if line_count == 0:
            result = result[:-2] + " VALUES\n "
        line_count += 1
        
file = open(str(time.time()) + "-insert_query.sql", "w")
file.write(result[:-2])
file.close()

print ("SQL file created.. check insert_query.sql")