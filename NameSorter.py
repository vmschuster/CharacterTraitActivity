import csv
from collections import Counter
import random

def main():
    # colours for the character trait
    colours = ["#edecf2","#6d98ba","#8793dd","#c1d4f2","#3669a2"]

    with open('traits.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)

    alldata = dict()
    alldata["All"] = []
    for i in range(1, len(data)):
        alldata["All"] = alldata["All"] + data[i][3:8]
        if str(data[i][2]) in alldata:
            alldata[str(data[i][2])] = alldata[str(data[i][2])] + data[i][3:8]
        else:
            alldata[str(data[i][2])] = data[i][3:8]

    for key in alldata.keys():
        alldata[key] = list(map(str.strip, alldata[key]))
        alldata[key] = list(map(lambda x:x.lower(), alldata[key]))
        alldata[key] = dict(Counter(alldata[key]))

        with open(str(key)+".csv", 'w') as csv_file:
            writer = csv.writer(csv_file)
            for key1, value in alldata[key].items():
                writer.writerow([value, key1, colours[random.randint(0,4)]])



if __name__ == "__main__":
    main()