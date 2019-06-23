curl -i -H "Content-Type: application/json" -X POST -d '{"name":"owner"}' http://127.0.0.1:5000/POST/user
curl -i -H "Content-Type: application/json" -X POST -d '{"name":"renter"}' http://127.0.0.1:5000/POST/user
curl -i http://127.0.0.1:5000/GET/users
curl -i -H "Content-Type: application/json" -X POST -d '{"name":"haha", "age":2, "owner":""}' http://127.0.0.1:5000/POST/car
curl -i http://127.0.0.1:5000/GET/cars
curl -i -H "Content-Type: application/json" -X PUT -d '{"id":0, "account":""}' http://127.0.0.1:5000/PUT/car/rent
curl -i -H "Content-Type: application/json" -X POST -d '{"id":0, "account":""}' http://127.0.0.1:5000/POST/car/authorize
curl -i http://127.0.0.1:5000/TEST
curl -i -H "Content-Type: application/json" -X PUT -d '{"id":0, "account":"", "oil":10, "crashes":0, "rate":5}' http://127.0.0.1:5000/PUT/car/return
curl -i http://127.0.0.1:5000/TEST
curl -i -H "Content-Type: application/json" -X PUT '{"account":