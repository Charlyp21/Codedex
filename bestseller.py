import csv

max_sales = 0
current_sales = 0
Bestsellingbook = None
file_path = 'bestsellerinfo.csv'

with open('Bestseller - Sheet1.csv', 'r', encoding='utf-8') as file:
    
    file.readline()

    csv_reader = csv.reader(file)

    for row in csv_reader:
        current_sales = float(row[4])
        if current_sales > max_sales:
            max_sales = current_sales
            Bestsellingbook = row
    
with open(file_path, 'w', encoding='utf-8') as log:
    csv_writer = csv.writer(log)
    csv_writer.writerow(['Book', 'Author', 'Sales in Millions'])
    csv_writer.writerow([Bestsellingbook[0], Bestsellingbook[1], Bestsellingbook[4]])

print(f'Informacion escrita en: {file_path}')