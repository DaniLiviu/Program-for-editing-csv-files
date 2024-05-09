
#https://github.com/noCR4SH/builtin-modules-python/blob/main/sys_example.py
#https://github.com/noCR4SH/builtin-modules-python/blob/main/csv_example.py
#Wojciech.niekrasz@gmail.com
import sys
import csv

if len(sys.argv) < 4:
    print("Usage: python reader.py in.csv out.csv <change1> <change2> ...")
    sys.exit(1)

in_file = sys.argv[1]
out_file = sys.argv[2]
changes = sys.argv[3:]

try:
    with open(in_file, 'r') as csv_file:  # Open in.csv for reading
      reader = csv.reader(csv_file)
      data = list(reader)
except IOError as e:
    print(f"Error: An error occurred while reading the in.csv file: {e}")
    
old_data = data
print(old_data)
print(old_data[0][0])
old_data[0][0] = "piano"
old_data[1][3] = "mug"
old_data[2][1] = 17
old_data[3][3] = 0
print(old_data)
try:
    with open(out_file, 'w', newline='') as open_csv_file:  
      writer = csv.writer(open_csv_file)
      writer.writerows(data)
      print(f"Modified CSV content written to: {out_file}")
except IOError as e:
    print(f"Error: An error occurred while writing to the out.csv file: {e}")

    for line in old_data:
        writer.writerow(line)