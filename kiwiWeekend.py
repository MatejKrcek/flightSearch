import csv
import datetime

originDestination = "PRG"
finalDestination = "BRN"
listOfSingleResults = []
listOfMultiResults = []
semiResults = []

dataSource = "example1.csv"


def noDirectConnection(arrival):
    results = []
    with open(dataSource, 'rt')as f:
        data = csv.reader(f)

        for row in data:
            if arrival == row[2]:
                semiResults.append(row)

        for int in range(len(semiResults)):

            with open(dataSource, 'rt')as f:
                data = csv.reader(f)

                for row in data:
                    if originDestination == row[1] and semiResults[int][1] == row[2]:

                        arrivalDate = datetime.datetime.strptime(
                            (row[4]), "%Y-%m-%dT%H:%M:%S")
                        nextDepartureDate = datetime.datetime.strptime(
                            (semiResults[int][3]), "%Y-%m-%dT%H:%M:%S")

                        if ((nextDepartureDate - arrivalDate) > (datetime.timedelta(hours=1)) and (nextDepartureDate - arrivalDate) < (datetime.timedelta(hours=6))):
                            results.append([row, semiResults[int]])

        listOfMultiResults = results

        #* sorting algo
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
        listOfMultiResults = [x for _,x in sorted(zip(index,listOfMultiResults))] 
        
        print(listOfMultiResults)


def searchFlight(departure, arrival):
    results = []
    with open(dataSource, 'rt')as f:
        data = csv.reader(f)

        for row in data:
            if departure == row[1] and arrival == row[2]:
                results.append(row)

    listOfSingleResults = sorted(results,
                                 key=lambda row: (row[5]), reverse=True)

    if len(listOfSingleResults) == 0:
        noDirectConnection(arrival)
    else:
        print(listOfSingleResults)

searchFlight(originDestination, finalDestination)
