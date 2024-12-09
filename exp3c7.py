import csv
csv_file=input("enter the csv file name(with extension):")
try:
    with open(csv_file,'r')as file:
        reader=csv.reader(file)
        print("\n csv file contents as lists of strings:")
        for row in reader:
            print(row)
except FileNotFoundError:
    print(f"erroe: the file '{csv_file}'was not found")
except Exception as e:
    print(f"an unexpected error occured:{e}")
