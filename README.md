# Flight script [Python Weekend]

My Python script for searching flights for Python Weekend in Barcelona.


## Description

How it works? I coded two main functions - *searchFlight* and *noDirectConnection*. *searchFlight* is called always - it takes two arguments - departure and arrival destination (airport codes). It loads the .csv file and goes through it - if it finds the correct results, it displays the sorted by the cheapest price. 

In case there are no direct flights, *noDirectConnection* is called. This function simply looks for more flighs which can be connected - based on the final destination. Also, the 1-6 condition (layover time must not be less than 1 hour and more than 6 hours) is applied as well as number of bags. 


## How to run it

The command link takes a few arguments


| Argument      | Type   | Description                          |
| ------------- | ------ | ------------------------------------ |
| `data sourse` | String | with .csv suffix                     |
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
    "flights": [
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


## Things to improve

The program currently shows flights based on this assumption - if there is a direct connection (from A -> B), show the connection (A -> B). If there is no direct connection, look for stops (A-> B -> C). It could show both result. I believe direct flights are always cheaper, so in the end it doesn't matter.