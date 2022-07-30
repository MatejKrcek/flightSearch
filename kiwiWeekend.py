import csv
import datetime
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('source', type=str)
parser.add_argument('departure', type=str)
parser.add_argument('arrival', type=str)
parser.add_argument('--bags', type=int)
args = parser.parse_args()

originDestination = args.departure  
finalDestination = args.arrival  
dataSource = args.source
bagsRequired = args.bags

listOfSingleResults = []
listOfMultiResults = []
semiResults = []


def noDirectConnection(arrival):
    results = []
    try:
        with open(dataSource, 'rt')as f:
            data = csv.reader(f)

            for row in data:
                if args.bags:
                    if arrival == row[2] and bagsRequired <= int(row[7]):
                        semiResults.append(row)
                else:
                    if arrival == row[2]:
                        semiResults.append(row)

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

    except:
        print("Sorry, I'm sorry, but I couldn't find your flight. Try using different criteria.")


def searchFlight(departure, arrival):
    results = []
    try:
        with open(dataSource, 'rt')as f:
            data = csv.reader(f)
            for row in data:
                if args.bags:
                    if departure == row[1] and arrival == row[2] and bagsRequired <= int(row[7]):
                        results.append(row)
                else:
                    if departure == row[1] and arrival == row[2]:
                        results.append(row)

        listOfSingleResults = sorted(results,
                                     key=lambda row: (row[5]))

        if len(listOfSingleResults) == 0:
            noDirectConnection(arrival)
        else:
            print(listOfSingleResults)

    except:
        print("Sorry, I'm sorry, but I couldn't find your flight. Try using different criteria.")


searchFlight(originDestination, finalDestination)
