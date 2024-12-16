import csv

data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
]

try:
    with open('packing_list.csv', 'r') as file:
        csv_read=csv.reader(file)
        for row in csv_read:
            print(row)

except FileNotFoundError:
    print("Packing list file not found. Creating a new one.")
    with open('packing_list.csv', 'w') as list:
        list_writer=csv.writer(list)
        list_writer.writerows(data)