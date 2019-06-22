# Automotive-comtract
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
1. `git clone https://github.com/DCChen1998/Automotive-comtract.git`
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
curl -i -H "Content-Type: application/json" -X POST -d '{"name":"haha", "age":2, "owner":"owner's address"}' http://localhost:5000/POST/car
紅色引號裡要加入owner 的account，表示owner 有一台叫haha 2年的車

curl -i http://localhost:5000/GET/cars
可以看到目前所有可以租的車

curl -i -H "Content-Type: application/json" -X PUT -d '{"id":0, "account":""}' http://localhost:5000/PUT/car/rent
租車，要在紅色引號裡打renter 的account，表示renter要租id 是0的車，這時候可以重複上一步，會看到這台車沒有在上面

curl -i -H "Content-Type: application/json" -X POST -d '{"id":0, "account":""}' http://localhost:5000/POST/car/authorize
這是讓車子可以確定要用的人是不是renter，要在紅色引號裡打renter 的account

curl -i http://localhost:5000/TEST
可以看到balance 和一些資料，但目前用ios好像有錯

curl -i -H "Content-Type: application/json" -X PUT -d '{"id":0, "account":"", "oil":10, "crashes":0, "rate":5}' http://localhost:5000/PUT/car/return
還車，id 是要還的車的id，紅色引號裡打renter 的account，oil 是耗油或里程，crashes是是否有車禍，都是來算錢的，rate是給個評分（1~5)，之後在看車時就可以看到平均分數



