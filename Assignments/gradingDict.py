#this should run all aspects of the program I had to change my CSV file to run it my way and it calculates the weighted averages for extra credit

from statistics import mean
import csv
import collections

with open('grades.csv', mode='r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    grades = collections.defaultdict(dict)
    for row in reader:
        grades[row[0]][row[1]] = row[2:7]
        grades[row[0]][row[7]] = row[8:11]
        grades[row[0]][row[11]] = row[12:]


def avg(lst):
    return mean(lst)


assignmentWeight = 0.10
testWeight = 0.70
labWeight = 0.20

for key, value in grades.items():
    assignLst = grades[key]['Assignment']
    assignAvgLst = [float(i) for i in assignLst]
    assignmentAvg = avg(assignAvgLst)
    # assignFmt = ("%.2f" % assignmentAvg)
    assignFmtPercent = "{:.0%}".format(assignmentAvg)

    testLst = grades[key]['Test']
    testAvgLst = [float(i) for i in testLst]
    testAvg = avg(testAvgLst)
    # testFmt = ("%.2f" % testAvg)
    testFmtPercent = "{:.0%}".format(testAvg)

    labLst = grades[key]['Lab']
    labAvgLst = [float(i) for i in labLst]
    labAvg = avg(labAvgLst)
    # labFmt = ("%.2f" % labAvg)
    labFmtPercent = "{:.0%}".format(labAvg)

    overallAvgW = (assignmentAvg * assignmentWeight + testAvg * testWeight + labAvg * labWeight) / (
                assignmentWeight + testWeight + labWeight)
    if overallAvgW >= 0.90:
        overallGrade = "A"
    elif overallAvgW >= 0.80:
        overallGrade = "B"
    elif overallAvgW >= 0.70:
        overallGrade = "C"
    elif overallAvgW >= 0.60:
        overallGrade = "D"
    else:
        overallGrade = "Grade is to low please see teacher"

    print("=========================\n      ", key)
    print("Assignment Average:", assignFmtPercent)
    print("Test Average:", testFmtPercent)
    print("Lab Average:", labFmtPercent)
    print("Overall Average:", overallGrade, "\n=========================")
