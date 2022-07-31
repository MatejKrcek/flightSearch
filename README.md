# Flight script [Python Weekend]

My Python script for searching flights for Python Weekend in Barcelona.


## Description

How does it work? I coded two main functions - *searchFlight* and *noDirectConnection*. *searchFlight* is called always - it takes two arguments - departure and arrival destination (airport codes). It loads the .csv file and goes through it - if it finds the direct flight connection, it displays it sorted by the cheapest price. 

In case there are no direct flights, *noDirectConnection* is called. This function simply looks for more flights which can be connected - based on the stop destination. Also, the 1-6 condition (layover time must not be less than 1 hour and more than 6 hours) is applied as well as the number of bags. All the results are sorted by the total flights and displayed as JSON. 


## How to run it

The command link takes a few arguments


| Argument      | Type   | Description                          |
| ------------- | ------ | ------------------------------------ |
| `data source` | String | with .csv suffix                     |
| `departure`   | String | three letters airport code           |
| `arrival`     | String | three letters airport code           |
| `bags`        | int    | number of bags */optional argument/* |


**Example input**

Search all flights from *PRG* to *STN* with *2* bags:
```
python3 solution.py data.csv PRG STN --bags=2
```

**Example output**
```json
[
    {
        "flights":[
          {
            "flight_no": "FR1374",
            "origin": "PRG",
            "destination": "STN",
            "departure": "2021-09-19T05:00:00",
            "arrival": "2021-09-19T06:00:00",
            "base_price": 18.0,
            "bag_price": 10.0,
            "bags_allowed": 2
          }
        ], 
        "bags_allowed": 2,
        "bags_count": 0,
        "destination": "PRG",
        "origin": "BRN",
        "total_price": 38.0,
        "travel_time": "1:00:00"
    }
]
```

**Example input #2**

Search all flights from *PRG* to *LAX* with *1* bags:
```
python3 solution.py data3.csv PRG LAX --bags=1
```

**Example output #2**
```json
[
   {
      "flights":[
         {
            "flight_no":"AA1110",
            "origin":"PRG",
            "destination":"STN",
            "departure":"2021-09-19T04:40:00",
            "arrival":"2021-09-19T06:50:00",
            "base_price":22.0,
            "bag_price":10.0,
            "bags_allowed":2
         },
         {
            "flight_no":"AA1113",
            "origin":"STN",
            "destination":"LAX",
            "departure":"2021-09-19T11:00:00",
            "arrival":"2021-09-19T19:50:00",
            "base_price":100.0,
            "bag_price":7.0,
            "bags_allowed":2
         }
      ],
      "bags_allowed":2,
      "bags_count":1,
      "destination":"LAX",
      "origin":"PRG",
      "total_price":139.0,
      "travel_time":"11:00:00"
   },
   {
      "flights":[
         {
            "flight_no":"AA1111",
            "origin":"PRG",
            "destination":"STN",
            "departure":"2021-09-19T05:40:00",
            "arrival":"2021-09-19T07:50:00",
            "base_price":31.0,
            "bag_price":15.0,
            "bags_allowed":1
         },
         {
            "flight_no":"AA1113",
            "origin":"STN",
            "destination":"LAX",
            "departure":"2021-09-19T11:00:00",
            "arrival":"2021-09-19T19:50:00",
            "base_price":100.0,
            "bag_price":7.0,
            "bags_allowed":2
         }
      ],
      "bags_allowed":1,
      "bags_count":1,
      "destination":"LAX",
      "origin":"PRG",
      "total_price":153.0,
      "travel_time":"11:00:00"
   },
   {
      "flights":[
         {
            "flight_no":"AA1110",
            "origin":"PRG",
            "destination":"STN",
            "departure":"2021-09-19T04:40:00",
            "arrival":"2021-09-19T06:50:00",
            "base_price":22.0,
            "bag_price":10.0,
            "bags_allowed":2
         },
         {
            "flight_no":"AA1112",
            "origin":"STN",
            "destination":"LAX",
            "departure":"2021-09-19T11:44:00",
            "arrival":"2021-09-19T19:50:00",
            "base_price":123.0,
            "bag_price":13.0,
            "bags_allowed":2
         }
      ],
      "bags_allowed":2,
      "bags_count":1,
      "destination":"LAX",
      "origin":"PRG",
      "total_price":168.0,
      "travel_time":"10:16:00"
   },
   {
      "flights":[
         {
            "flight_no":"AA1111",
            "origin":"PRG",
            "destination":"STN",
            "departure":"2021-09-19T05:40:00",
            "arrival":"2021-09-19T07:50:00",
            "base_price":31.0,
            "bag_price":15.0,
            "bags_allowed":1
         },
         {
            "flight_no":"AA1112",
            "origin":"STN",
            "destination":"LAX",
            "departure":"2021-09-19T11:44:00",
            "arrival":"2021-09-19T19:50:00",
            "base_price":123.0,
            "bag_price":13.0,
            "bags_allowed":2
         }
      ],
      "bags_allowed":1,
      "bags_count":1,
      "destination":"LAX",
      "origin":"PRG",
      "total_price":182.0,
      "travel_time":"10:16:00"
   }
]
```



## Things to improve

The program currently shows flights based on this assumption - if there is a direct connection (from A -> B), show the connection (A -> B). If there is no direct connection, look for stops (A-> B -> C). It could show both results at the same time. I believe direct flights are always cheaper, so in the end, it doesn't matter for the user. Moreover, the return option could be added. 

## Contant

matej@krcek.cz