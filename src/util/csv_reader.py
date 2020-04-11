import csv, json


def readCSV(path):
    data = {}
    with open(path, newline="") as csvfile:
        reader = csv.DictReader(csvfile, quotechar='|')
        for row in reader:
            data[row["id"]] = row
    return data


def writeCSV(path, rowList, writeMode="a"):
    with open(path, writeMode, newline="") as csvfile:
        writer = csv.writer(csvfile, quotechar='|')
        for row in rowList:
            writer.writerow(row)
