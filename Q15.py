# Q15
# read data from a csv file and print it in console
import csv
file_path = 'election_data.csv'
try:
    with open(file_path, newline='')as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            print(row)
except FileNotFoundError:
    print("Error: The file {} does not exists!".format(file_path))
except Exception as exc:
    print("Error occured!")