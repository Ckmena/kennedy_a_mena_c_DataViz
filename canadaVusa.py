import csv
import matplotlib.pyplot as plt

canada = []
usa = []
world = []

categories = []


with open('data/OlympicsWinter.csv') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0
        
    for row in reader:
        if line_count is 0:
            categories.append(row)
            line_count += 1
        else:
            
            if row[4] == "CAN":
                canada.append([int(row[0]), row[5], row[6], row[7]])
            elif row[4] == "USA":
                usa.append([int(row[0]), row[5], row[6], row[7]])
            else:
                world.append([int(row[0]), row[5], row[6], row[7]])
            line_count += 1

print('total medal for canada:', len(canada))
print('Total medal for USA:', len(usa))
print('total rest of the worl:', len(world))

# print(canada[0])
print('processed', line_count, 'rows of data')

#PERCENTAGES!! 
pct_can = len(canada) / line_count * 100
pct_usa = len(usa) / line_count * 100 
pct_world = len(world) / line_count * 100

print('Canada percentage', pct_can)
print('USA percentage', pct_usa)
print('The Rest', pct_world)

#***** PIE CHART *****
labels = "Canada", "United States", "The rest"
sizes = [pct_can, pct_usa, pct_world]
colors = ["tomato", "darkturquoise","darkorange"]
explode = (0.5, 0.1, 0.1)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("Who did better Canada or The United States of America?")
plt.show()

