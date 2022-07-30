# Flight script [Python Weekend]

My Python script for searching flights for Python Weekend in Barcelona.


## Description

How it works? I coded two main functions - *searchFlight* and *noDirectConnection*. *searchFlight* is called always - it takes two arguments - departure and arrival destination (airport codes). It loads the .csv file and goes through it - if it finds the correct results, it displays the sorted by the cheapest price. 

In case there are no direct flights, *noDirectConnection* is called. This function simply looks for more flighs which can be connected - based on the final destination. Also, the 1-6 condition (layover time must not be less than 1 hour and more than 6 hours) is applied as well as number of bags. 


## How to run it

The command link takes a few arguments


| Argument      | Type   | Description                |
| ------------- | ------ | -------------------------- |
| `data sourse` | String | with .csv suffix           |
| `departure`   | String | three letters airport code |
| `arrival`     | String | three letters airport code |
| `bags`        | int    | number of bags             |


**Example input**

Search all flights from *DHE* to *NRW* with *2* bags:
```
python3 kiwiWeekend.py example1.csv DHE NRW 2
```

**Example output**
```
tbd
```


## Features

- Search direct flights
- Search flights with a stop
- Add the number of bags
- Display the flights sorted by the best (cheapest) price
  - Even for more flights 


## Things to improve

- 