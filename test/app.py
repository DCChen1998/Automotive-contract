from flask import Flask, jsonify, request, abort
import CarRenter

app = Flask(__name__)
users = [{'owner': CarRenter.owner, 'customer': CarRenter.customer}]

#get /user
@app.route('/GET/users', methods=['GET'])
def get_users():
    return jsonify(users)

#get /car
@app.route('/GET/cars', methods=['GET'])
def get_cars():
    return jsonify(CarRenter.Get_Available_Car())

#use:curl -i -H "Content-Type: application/json" -X POST -d '{"name":"blabla", "age":87, "owner":"account[0]"}' http://localhost:5000/POST/car
@app.route('/POST/car', methods=['POST'])
def create_vtoken():
    if not request.json or not 'name' in request.json or not 'age' in request.json or not 'owner' in request.json:
        abort(400)
    Car = {
        'name': request.json['name'],
        'age': request.json['age'],
        'owner': request.json['owner']
    }
    CarRenter.Create_Vtoken(request.json['name'], request.json['age'], request.json['owner'])
    return jsonify(Car), 201



app.run(port=5000, debug=True)#host=

'''
Create_Vtoken(_name, _age)
Rent_Car(_tokenId)
Return_Car(_tokenId, _oil, crashes, rate)
Is_Rented(_id)
Get_Available_Car()
owner = web3.eth.accounts[0]
customer = web3.eth.accounts[1]
'''
#print(CarRenter.owner, CarRenter.customer)