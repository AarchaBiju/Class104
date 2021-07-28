import csv
import statistics
from collections import Counter

def meanData(totalWeight, number):
    mean = totalWeight/number
    print(mean)

def medianData(sortedData,totalEntries):
    if totalEntries%2==0:
        median1 = float(sortedData[totalEntries//2])
        median2 = float(sortedData[totalEntries//2-1])
        median=(median1+median2)/2
    else :
        median=sortedData[totalEntries//2]  
    print(median)    

def modeData(sortedData):
    data = Counter(sortedData)
    mode_data_for_range = {
                            "75-85": 0,
                            "85-95": 0,
                            "95-105": 0,
                            "105-115": 0,
                            "115-125": 0,
                            "125-135": 0,
                            "135-145": 0,
                            "145-155": 0,
                            "155-165": 0,
                            "165-175": 0
                        }
    for weight, occurence in data.items():
        if 75 < weight < 85:
            mode_data_for_range["75-85"] += occurence
        elif 85 < weight < 95:
            mode_data_for_range["85-95"] += occurence
        elif 95 < weight < 105:
            mode_data_for_range["95-105"] += occurence
        elif 105 < weight < 115:
            mode_data_for_range["105-115"] += occurence
        elif 115 < weight < 125:
            mode_data_for_range["115-125"] += occurence
        elif 125 < weight < 135:
            mode_data_for_range["125-135"] += occurence
        elif 135 < weight < 145:
            mode_data_for_range["135-145"] += occurence
        elif 145 < weight < 155:
            mode_data_for_range["145-155"] += occurence
        elif 155 < weight < 165:
            mode_data_for_range["155-165"] += occurence
        elif 165 < weight < 175:
            mode_data_for_range["165-175"] += occurence
    mode_range, mode_occurence = 0, 0
    for range, occurence in mode_data_for_range.items():
        if occurence > mode_occurence:
            mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
    mode = float((mode_range[0] + mode_range[1]) / 2)
    print(f"Mode is -> {mode:2f}")


with open("height-weight.csv",newline='') as f:
    reader=csv.reader(f)
    fileData=list(reader)
fileData.pop(0)  

totalWeight=0
totalPeople=0
sortedData=[]
for totalData in fileData:
    totalWeight += float(totalData[2])
    sortedData.append(float(totalData[2]))
totalPeople= len(fileData)  
sortedData.sort()  
meanData(totalWeight, totalPeople)
medianData(sortedData,totalPeople)
modeData(sortedData)
