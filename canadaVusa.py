import csv
import matplotlib.pyplot as plt

canada = []
usa = []

with open('data/OlympicsWinter.csv') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    for row in reader:
        if line_count is 0:
            categories.append(row)
            line_count += 1

        elif row[4] == "CAN":
            canada.append([int(row[0]), row[5], row[6], row[7]])
        else row[4] == "USA"
            usa.append([int(row[0]), row[5], row[6], row[7]])

print('total medal for canada:', len(canada))
print('Total medal for USA:', len(usa))

print(canada[0])

print('processed', line_count, 'rows of data')