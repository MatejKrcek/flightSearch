import csv
import datetime
import argparse
from heapq import merge
import json
from ntpath import join

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


# ! TOTAL PRICE = TICEKTS a BAG prices!!!!!!!!

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

            listOfFlights = []
            outputList = []

            for element in listOfMultiResults:
                totalFlightTime = datetime.datetime.strptime(
                    (element[0][4]), "%Y-%m-%dT%H:%M:%S") - datetime.datetime.strptime((element[0][3]), "%Y-%m-%dT%H:%M:%S") + datetime.datetime.strptime(
                    (element[1][4]), "%Y-%m-%dT%H:%M:%S") - datetime.datetime.strptime((element[1][3]), "%Y-%m-%dT%H:%M:%S")

                firstConnection = [{
                    "flight_no": element[0][0],
                    "origin": element[0][1],
                    "destination": element[0][2],
                    "departure": element[0][3],
                    "arrival": element[0][4],
                    "base_price": float(element[0][5]),
                    "bag_price": float(element[0][6]),
                    "bags_allowed": int(element[0][7])},
                ]

                secondConnection = [{
                    "flight_no": element[1][0],
                    "origin": element[1][1],
                    "destination": element[1][2],
                    "departure": element[1][3],
                    "arrival": element[1][4],
                    "base_price": float(element[1][5]),
                    "bag_price": float(element[1][6]),
                    "bags_allowed": int(element[1][7])},
                ]

                firstConnection.append(secondConnection)

                preOutput = [{
                    "flights": firstConnection,
                    "bags_allowed": int(max(firstConnection[0]["bags_allowed"], firstConnection[1][0]["bags_allowed"])),
                    "bags_count": int(bagsRequired),
                    "destination": finalDestination,
                    "origin": originDestination,
                    "total_price": float(firstConnection[0]["base_price"] + (firstConnection[0]["bag_price"] * bagsRequired) + firstConnection[1][0]["base_price"] + (firstConnection[1][0]["bag_price"] * bagsRequired)),
                    "travel_time": str(totalFlightTime)
                }]

                listOfFlights.append(preOutput)
            
            output = json.dumps(listOfFlights)
            # print(output[1:-1])
            print(output[0])

            # preOutput["flights"] = firstConnection

            # for index in range(len(element)):
            #     print(index)
            #     outputSingleFlight = [
            #         {"flight_no": element[index][0],
            #          "origin": element[index][1],
            #          "destination": element[index][2],
            #          "departure": element[index][3],
            #          "arrival": element[index][4],
            #          "base_price": float(element[index][5]),
            #          "bag_price": float(element[index][6]),
            #          "bags_allowed": int(element[index][7])},
            #     ]
            #     # "bags_allowed": int(element[7]),
            #     # "bags_count": int(bagsRequired),
            #     # "destination": finalDestination,
            #     # "origin": originDestination,
            #     # "total_price": float(element[5]),
            #     # "travel_time": str(totalFlightTime)

            #     listOfFlights.append(outputSingleFlight)

            # preOutput["flights"] = listOfFlights[0][0]
            # preOutput["flights"] = listOfFlights[1][0]

            # preOutput["bags_allowed"] = int(max(
            #     preOutput["flights"][0]["bags_allowed"], preOutput["flights"][1]["bags_allowed"]))
            # preOutput["bags_count"] = int(bagsRequired)
            # preOutput["destination"] = finalDestination
            # preOutput["origin"] = originDestination
            # preOutput["total_price"] = float(
            #     preOutput["flights"][0]["base_price"] + preOutput["flights"][1]["base_price"])
            # preOutput["travel_time"] = str(totalFlightTime)

            # outputList.append(preOutput)

            # outputMultiFlight = []
            # outputMultiFlight.append(listOfFlights[0][0])
            # outputMultiFlight.append(listOfFlights[1][0])

            # preOutput["flights"] = outputMultiFlight
            # preOutput["bags_allowed"] = int(max(
            #     preOutput["flights"][0]["bags_allowed"], preOutput["flights"][1]["bags_allowed"]))
            # preOutput["bags_count"] = int(bagsRequired)
            # preOutput["destination"] = finalDestination
            # preOutput["origin"] = originDestination
            # preOutput["total_price"] = float(
            #     preOutput["flights"][0]["base_price"] + preOutput["flights"][1]["base_price"])
            # preOutput["travel_time"] = str(totalFlightTime)

            # outputList.append(preOutput)
            #     print(preOutput)
            #     print('---')
            # print(outputList)

            # output = json.dumps(preOutput)
            # print(output)

            # print(listOfMultiResults)

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
            output = {}
            listOfFlights = []

            for element in listOfSingleResults:
                totalFlightTime = datetime.datetime.strptime(
                    (element[4]), "%Y-%m-%dT%H:%M:%S") - datetime.datetime.strptime(
                    (element[3]), "%Y-%m-%dT%H:%M:%S")

                outputSingleFlight = [{
                    "flights": [
                        {"flight_no": element[0],
                         "origin": element[1],
                         "destination": element[2],
                         "departure": element[3],
                         "arrival": element[4],
                         "base_price": float(element[5]),
                         "bag_price": float(element[6]),
                         "bags_allowed": int(element[7])}
                    ],
                    "bags_allowed": int(element[7]),
                    "bags_count": int(bagsRequired),
                    "destination": finalDestination,
                    "origin": originDestination,
                    "total_price": float(element[5]),
                    "travel_time": str(totalFlightTime)

                }]

                listOfFlights.append(outputSingleFlight)

            output = json.dumps(listOfFlights)
            print(output[1:-1])

    except:
        print("Sorry, I'm sorry, but I couldn't find your flight. Try using different criteria.")


searchFlight(originDestination, finalDestination)
