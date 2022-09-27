# Redis Showcase
Made for demonstration purposes in IF4031 Distributed Application Development class. 

## How it works
This demonstration simulates communication between three parties, a server that is connected to a redis database, a client who sends post requests to the server, and a listener who reads the data. The server will receive requests on http://localhost:5000, and has two routes, /post and /get. There are two clients, one of which constantly sends post requests to the database, and the other reads the data. The transmission logs will be written at ./listener.txt and ./client.txt.

## Requirements
This application requires redis, Python3.8, and pip. To install these on linux, run:

`sudo apt-get install redis python3.8 python3-pip`

Other than that, this application requires some python modules which can be installed by running:

`sudo pip install -r requirements.txt`

## Usage
To start the server, open a terminal and run:

`make server`

To start clients, run:

`make clients`

To clean the database and logs, run:

`make clean`
