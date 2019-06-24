from flask import Flask, jsonify, request, abort
import CarRenter

app = Flask(__name__)
#users = [{'owner': CarRenter.owner, 'customer': CarRenter.customer}]
users = []
count = 0 #the count of assigned ganache account
car_count = 0
reserve_account = {
    'name': 'reserved',
    'account': CarRenter.Get_Unused_Account(0)
}
users.append(reserve_account)
owner = {
    'name': 'owner',
    'account': CarRenter.Get_Unused_Account(1)
}
renter = {
    'name': 'renter',
    'account': CarRenter.Get_Unused_Account(2)
}
users.append(owner)
users.append(renter)
# check if the account has been registered
def is_registered(account):
    for i, user in enumerate(users):
        if user['account'] == account:
            global count
            count = i
            return True
        else:
            continue
    return False

#get /user
@app.route('/GET/users', methods=['GET'])
def get_users():
    all_users = []
    for i in range(len(users)):
        user = {
            'name': users[i]['name'],
            'account': users[i]['account'],
            'balance': CarRenter.Get_Balance(i)
        }
        all_users.append(user)
    return jsonify(all_users)
    #return jsonify(users)

#add new user and assign an account to him
#use:curl -i -H "Content-Type: application/json" -X POST -d '{"name":"blabla"}' http://localhost:5000/POST/user
@app.route('/POST/user', methods=['POST'])
def new_user():
    if not request.json or not 'name' in request.json:
        abort(400)
    if len(users) >= 10:
        abort(400)
    user = {
        'name': request.json['name'],
        'account': CarRenter.Get_Unused_Account(len(users))
    }
    users.append(user)
    return jsonify(user)

@app.route('/POST/user/balance', methods=['POST'])
def get_balance():
    if not request.json or not 'account' in request.json:
        abort(400)
    if not is_registered(request.json['account']): #global variable count is set
        abort(401)
    balance = {
        'balance': CarRenter.Get_Balance(count)
    }
    return jsonify(balance)
    

#get
#use:curl -i http://localhost:5000/GET/cars
@app.route('/GET/cars', methods=['GET'])
def get_cars():
    return jsonify(CarRenter.Get_Available_Car(users[0]['account']))

#authorize: called by car to make sure the account == renter
#use:curl -i -H "Content-Type: application/json" -X POST -d {"id":0, "account": "blabla"} http://localhost:5000/POST/car/authorize
@app.route('/POST/car/authorize', methods=['POST'])
def authorize():
    if not request.json or not 'id' in request.json or not 'account' in request.json:
        abort(400)
    if not is_registered(request.json['account']):
        abort(401)
    if CarRenter.Is_Rented(request.json['id']) == False:
        abort(400)
    renter = CarRenter.Get_Renter(request.json['id'])
    if renter == request.json['account']:
        message = {
            'authorized': True
        }
        return jsonify(message)
    else:
        message = {
            'authorized': False
        }
        return jsonify(message)

#use:curl -i -H "Content-Type: application/json" -X POST -d '{"name":"blabla", "age":87, "owner":"account"}' http://localhost:5000/POST/car
@app.route('/POST/car', methods=['POST'])
def create_vtoken():
    if not request.json or not 'name' in request.json or not 'age' in request.json or not 'owner' in request.json:
        abort(400)
    if is_registered(request.json['owner']):
        global car_count
        Car = {
            'name': request.json['name'],
            'age': request.json['age'],
            'owner': request.json['owner'],
            'id': car_count
        }
        car_count += 1
        CarRenter.Create_Vtoken(Car['name'], Car['age'], Car['owner'])
        return jsonify(Car), 201
    else:
        abort(401)

#CarRenter.Create_Vtoken('haha', 2, owner['account'])

#rent car
#use:curl -i -H "Content-Type: application/json" -X PUT -d '{"id":0, "account":"account"}' http://localhost:5000/PUT/car/rent
@app.route('/PUT/car/rent', methods=['PUT'])
def rent_car():
    if not request.json or not 'id' in request.json or not 'account' in request.json:
        abort(400)
    if is_registered(request.json['account']) and CarRenter.Is_Rented(request.json['id']) == False and CarRenter.Get_Renter(request.json['id']) != request.json['account']:
        id = request.json['id']
        account = request.json['account']
        detail = CarRenter.Rent_Car(id, account)
        return jsonify(detail), 201
    else:
        abort(404)

#return car
#use:curl -i -H "Content-Type: application/json" -X PUT -d '{"id":0, "account":"account", "oil":10, "crashes":0, "rate":5}' http://localhost:5000/PUT/car/return
@app.route('/PUT/car/return', methods=['PUT'])
def return_car():
    if not request.json or not 'id' in request.json or not 'account' in request.json or not 'oil' in request.json or not 'crashes' in request.json or not 'rate' in request.json:
        abort(400)
    if is_registered(request.json['account']) and CarRenter.Is_Rented(request.json['id']) == True and CarRenter.Get_Renter(request.json['id']) == request.json['account']:
        id = request.json['id']
        account = request.json['account']
        oil = request.json['oil']
        crashes = request.json['crashes']
        rate = request.json['rate']
        detail = CarRenter.Return_Car(id, oil, crashes, rate, account)
        if detail == False:
            abort(400)
        else:
            return jsonify(detail), 201
    else:
        abort(401)

@app.route('/TEST', methods=['GET'])
def test():
    thing = {
        'is_rented': CarRenter.Is_Rented(0),
        'Balance1': CarRenter.Get_Balance(1), #because account[0] is reserved
        'Balance2': CarRenter.Get_Balance(2)
    }
    return jsonify(thing)



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
