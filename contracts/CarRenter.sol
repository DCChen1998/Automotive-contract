pragma solidity ^0.5.0;
import "./ownable.sol";
import "./SafeMath.sol";

contract CarRenter is Ownable{

    using SafeMath for uint256;
    using SafeMath16 for uint16;

    event RentCar(uint16 _id, address _renter);
    event NewVtoken(uint16 _id, string _name);

    mapping (uint16 => address) car2owner;

    struct VToken {
        Car car;
        address payable renter;
        address payable owner;
    }
    
    struct Car {
        string name;
        uint rent_time; // now + expected renting time
        uint16 id;
        uint16 age;
        uint16 price;
        uint16 crash_number;
        bool is_rented;

    }

    VToken[] vtokens;
    uint64 basic_renttime = 1;

    function Create_Vtoken(string memory _name, uint16 _age) internal { // call by car wallet
        Car memory newcar = Car(_name, now, 0, _age, 10, 0, false);
        VToken memory vtoken = VToken(newcar, msg.sender, msg.sender);
        uint16 id = uint16(vtokens.push(vtoken) - 1);// add to array and update id value
        vtokens[id].car.id = id;
        emit NewVtoken(id, _name);
    }

    function Is_Rented(uint16 _id) public view returns (bool){
        //return cars[_id].is_rented;
        vtokens[_id].car.is_rented;
    }

    function Rent_Car(uint16 _id) public payable {
        require(Is_Rented(_id) == false && msg.value >= 1 ether);

        vtokens[_id].renter = msg.sender;
        vtokens[_id].car.rent_time = now + basic_renttime * 60;
        vtokens[_id].car.is_rented = true;

        emit RentCar(_id, msg.sender);
    }

    function Return_Car(uint16 _id, uint _oil) public payable {
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

}