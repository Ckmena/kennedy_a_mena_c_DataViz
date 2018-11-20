import csv
import numpy as np
import matplotlib.pyplot as plt

year = [] # strip out the first row of text
gender= [] # push the installs data here
medals = [] #push the ratings data here

with open ("data/Olympics-Winter.csv") as csvfile:
    readerCSV = csv.reader(csvfile)
    line_count = 0
    #print('Works')

    for row in readerCSV:
        gender = row[5] 
        medals = row[7]

        gender.append(gender)
        medals.append(medals)

        print(gender)
        print(medals)
        
        #if line_count is 0: # strip the header out
            #print('pushing text row to categories array')
            #gender.append(row)
            #line_count += 1

        #else:
            #print("collect the rest of the data")
            #genderData = (row[2])
            #gender.append(float(genderData))
            

            #print('collect the rest of the data') 
            #medalData = row[5]
            #medalData = medalData.replace(",", "")
            #medalData = medalData.replace("Free", "0")
            #medals.append(int(np.char.strip(medalData, "+")))
            #line_count += 1

#print('processed', line_count, "rows of data")
#print('first line', gender[0])
#print('last line', gender[-1])

#np_gender = np.array(gender)
