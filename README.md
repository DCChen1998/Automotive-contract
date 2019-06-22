# Automotive-contract
Smart contract of automotive application

## Requirements

- python3
- NPM (Tested with v6.4.1)
- Ganache
```
npm install -g ganache-cli
```
- Truffle v5.0.19
```
npm install -g truffle
```

## Installation and Setup
1. `git clone https://github.com/DCChen1998/Automotive-contract.git`
2. Start local blockchain server on terminal.
```
ganache-cli
```

## Compile and Deploy Contract
Compile on another terminal.
```
truffle migration
```

## Run Web App Server
1. `cd test`
2. run app.py

## Test
Test on another terminal and see test_cmd.txt
1. Create owner
```
curl -i -H "Content-Type: application/json" -X POST -d '{"name":"owner"}' http://localhost:5000/POST/user
```
2. Create renter
```
curl -i -H "Content-Type: application/json" -X POST -d '{"name":"renter"}' http://localhost:5000/POST/user
```
3. Check all current users
```
curl -i http://localhost:5000/GET/users
```
4. Create car
```
curl -i -H "Content-Type: application/json" -X POST -d '{"name":"haha", "age":2, "owner":"owner's address"}' http://localhost:5000/POST/car
```
5. Check all cars can rent
```
curl -i http://localhost:5000/GET/cars
```
6. Rent car
```
curl -i -H "Content-Type: application/json" -X PUT -d '{"id":0, "account":"renter's address"}' http://localhost:5000/PUT/car/rent
```
7. Check whether the user is the renter
```
curl -i -H "Content-Type: application/json" -X POST -d '{"id":0, "account":"address"}' http://localhost:5000/POST/car/authorize
```
8. Return car
```
curl -i -H "Content-Type: application/json" -X PUT -d '{"id":0, "account":"renter's address", "oil":10, "crashes":0, "rate":5}' http://localhost:5000/PUT/car/return
```
