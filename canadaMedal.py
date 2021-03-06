import csv
import matplotlib.pyplot as plt

canada = []
world = []
bronzes = []

categories = []

with open('data/OlympicsWinter.csv') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    print("there are ", line_count, "lines")

    for row in reader:
        if line_count is 0:
            categories.append(row)
            line_count += 1

        elif row[4] == "CAN":
            canada.append([int(row[0]), row[5], row[6], row[7]])
        else:
            world.append([int(row[0]), row[5], row[6], row[7]])

print("there are ", line_count, "lines")

print('total medal for canada:', len(canada))
print('rest of the world:', len(world))

print(canada[0])

print('processed', line_count, 'rows of data')

gold_1924 = []
gold_1948 = []
gold_1972 = []
gold_2002 = []
gold_2014 = []

for medal in canada:
    if medal[0] == 1924 and medal [3] == "Gold":
        gold_1924.append(medal)
    elif medal [0] == 1948 and medal [3] == "Gold":
        gold_1948.append(medal)
    elif medal [0] == 1972 and medal [3] == "Gold":
        gold_1972.append(medal)
    elif medal [0] == 2002 and medal [3] == "Gold":
        gold_2002.append(medal)
    elif medal [0] == 2014 and medal [3] == "Gold":
        gold_2014.append(medal)

print('canada won', len(gold_1924), 'gold medals in 1924')
print('canada won', len(gold_2014), 'gold medals in 2014')

#filter the 2014 array by gender 

men = []
women = []

for gender in canada:
    if gender[1] == "Men" and gender [3] == "Gold":
        men.append(gender)
    else:
        women.append(gender)

print('men canada medalds', len(men))
print('women canada medal', len(women))

pct_men = len(men) / len(canada) * 100
pct_women = len(women) / len(canada) * 100 

print('men percentage', pct_men)
print('women percentage', pct_women)
print("lines", line_count)

#pieChart***** Start
labels = "Men", "Women"
sizes = [pct_men, pct_women]
colors = ['lightcoral', 'lightskyblue']
explode = (0.1, 0.1)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("Who won the most medal in Canada?")
plt.show()


