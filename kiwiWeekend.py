import csv
import datetime
import sys
import getopt

originDestination = "PRG"  # str(sys.argv[2])
finalDestination = "BRN"  # str(sys.argv[3])
dataSource = "example1.csv"  # str(sys.argv[1])
bagsRequired = 0  # int(sys.argv[4])

listOfSingleResults = []
listOfMultiResults = []
semiResults = []


def noDirectConnection(arrival):
    results = []
    with open(dataSource, 'rt')as f:
        data = csv.reader(f)

        for row in data:
            if arrival == row[2] and bagsRequired <= int(row[7]):
                semiResults.append(row)

                # ! co kdyz to nenajde? Chtelo by to nejakou zpravu

        for i in range(len(semiResults)):

            with open(dataSource, 'rt')as f:
                data = csv.reader(f)

                for row in data:
                    if originDestination == row[1] and semiResults[i][1] == row[2] and bagsRequired <= int(row[7]):

                        arrivalDate = datetime.datetime.strptime(
                            (row[4]), "%Y-%m-%dT%H:%M:%S")
                        nextDepartureDate = datetime.datetime.strptime(
                            (semiResults[i][3]), "%Y-%m-%dT%H:%M:%S")

                        if ((nextDepartureDate - arrivalDate) > (datetime.timedelta(hours=1)) and (nextDepartureDate - arrivalDate) < (datetime.timedelta(hours=6))):
                            results.append([row, semiResults[i]])

        listOfMultiResults = results

        # * sorting algo
        prices = []
        index = []
        price = 0
        i = 0
        for item in listOfMultiResults:
            for element in item:
                price = price + float(element[5])
            i = i + 1
            index.append(i-1)
            prices.append(price)
            price = 0
        prices, index = zip(*sorted(zip(prices, index)))
        listOfMultiResults = [x for _, x in sorted(
            zip(index, listOfMultiResults))]

        print(listOfMultiResults)


def searchFlight(departure, arrival):
    results = []
    with open(dataSource, 'rt')as f:
        data = csv.reader(f)

        for row in data:
            if departure == row[1] and arrival == row[2] and bagsRequired <= int(row[7]):
                results.append(row)

    listOfSingleResults = sorted(results,
                                 key=lambda row: (row[5]))

    if len(listOfSingleResults) == 0:
        noDirectConnection(arrival)
    else:
        print(listOfSingleResults)


searchFlight(originDestination, finalDestination)
