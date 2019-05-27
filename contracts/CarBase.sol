pragma solidity ^0.5.0;
import "./ownable.sol";
import "./SafeMath.sol";

contract CarBase is Ownable{

    using SafeMath for uint256;
    using SafeMath16 for uint16;

    event RentCar(uint _id, address _renter);
    event NewCar(uint _id, string _name);
    event Price(uint _price);
    //event AvailableNum(uint16 _num);
    event AvailableCar(uint _id, string _name, uint16 _rate_sum, uint16 _rate_num);

    mapping (uint => address) car2owner;
    mapping (address => uint) ownerTokenCount;
    
    struct Car {
        string name;
        address payable owner;
        address payable renter;
        uint rent_time; // now + expected renting time
        uint id;
        uint16 age;
        uint16 price;
        uint16 crash_number;
        uint16 rate_sum;
        uint16 rate_num;
    }

    Car[] cars;
    uint16 AvailableCarNum = 0;

    function Add_Car(string memory _name, uint16 _age, address payable _owner) internal { // call by car wallet
        
        Car memory newcar = Car(_name, _owner, _owner, now, 0, _age, 10, 0, 0, 0);
        uint id = cars.push(newcar) - 1;
        cars[id].id = id;
        car2owner[id] = _owner;
        ownerTokenCount[_owner]++;
        AvailableCarNum++;
        emit NewCar(id, _name);

        /*Car memory newcar = Car(_name, now, 0, _age, 10, 0, false);
        VToken memory vtoken = VToken(newcar, msg.sender, msg.sender);
        uint16 id = uint16(vtokens.push(vtoken) - 1);// add to array and update id value
        vtokens[id].car.id = id;
        car2owner[id] = msg.sender;
        emit NewVtoken(id, _name);*/
    }

    function Is_Rented(uint _id) public view returns (bool){
        //return cars[_id].is_rented;
        /*return vtokens[_id].car.is_rented;*/
        return (cars[_id].owner != cars[_id].renter);
    }

    /*function Get_All_Cars() external view returns (Car[] memory cars2) {
        cars2 = cars;
        return cars;
    }*/

    function Get_Available_Car_Num() external view returns(uint16) {
        //emit AvailableNum(AvailableCarNum);
        return AvailableCarNum;
    }

    function Get_All_Cars() external {
        for (uint i = 0; i < cars.length; i++){
            if (Is_Rented(i) == false) {
                emit AvailableCar(i, cars[i].name, cars[i].rate_sum, cars[i].rate_num);
            }
        }
    }

    function Calculate_Price(uint _tokenId, uint _oil, uint16 crashes) internal view returns(uint) {
        uint to_owner = cars[_tokenId].price + _oil * 50;
        if (crashes > 0) {
            to_owner += 50 * crashes;
        }
        return to_owner;
    }
/*
    function Rent_Car(uint _id) public payable {
        require(Is_Rented(_id) == false && msg.value == 1 ether);

        ownerTokenCount[cars[_id].owner]--;

        cars[_id].renter = msg.sender;
        cars[_id].rent_time = now + basic_renttime * 60;
        cars[_id].is_rented = true;
        cars[_id].owner.transfer(1 ether); //for bail

        emit RentCar(_id, msg.sender);

        require(Is_Rented(_id) == false && msg.value >= 1 ether);

        vtokens[_id].renter = msg.sender;
        vtokens[_id].car.rent_time = now + basic_renttime * 60;
        vtokens[_id].car.is_rented = true;

        vtokens[_id].owner.transfer(1 ether); // for bail

        emit RentCar(_id, msg.sender);
    }

    function Return_Car(uint _id, uint _oil) public payable {
        require(Is_Rented(_id) && msg.sender == vtokens[_id].renter);
        uint toOwner;
        uint toRenter;

        if (vtokens[_id].car.rent_time >= now) {
            toOwner = vtokens[_id].car.price + _oil * 50;
            toRenter = 1;
            vtokens[_id].owner.transfer(toOwner * 1 szabo);
            vtokens[_id].renter.transfer(toRenter * 1 ether);
        }
        else {
            toOwner = vtokens[_id].car.price + _oil * 50;
            toRenter = 0; //penalty for delay
            vtokens[_id].owner.transfer(toOwner * 1 szabo);
        }

        vtokens[_id].car.is_rented = false;
        vtokens[_id].renter = vtokens[_id].owner;

    }
    */

}