# Redis Showcase

Made for demonstration purposes in IF4031 Distributed Application Development class.

## How it works

This demonstration simulates communication between three parties, a server that is connected to a redis database, a client who sends post requests to the server, and a listener who reads the data. The server will receive requests on `http://localhost:5000`, and has two routes, `/post` and `/get`. There are two clients, one of which constantly sends post requests to the database, and the other reads the data. The transmission logs will be written at `./listener.txt` and `./client.txt`.

## Requirements

1. Redis
2. Python3.8
3. pip
4. virtualenv

## Installation

1. Install redis python and pip by typing `sudo apt-get install redis python3.8 python3-pip` (If you aren't UNIX based operating system, search how to install each requirements for your current operating system)
2. Install virtualenv by using `sudo pip3 install virtualenv`
3. Create your virtualenv in folder directory by using `virtualenv venv`
4. Activate the virtualenv by using
   1. Windows: ./Venv/Scripts/Activate
   2. UNIX: source ./Venv/bin/Activate
5. Install requirements by using `pip3 install -r requirements.txt`

## Usage

To start the server, open a terminal and run: `make server`

To start clients, run: `make clients`

To clean the database and logs, run: `make clean`
