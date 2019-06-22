pragma solidity ^0.5.0;
import "./ownable.sol";
import "./SafeMath.sol";

contract CarBase is Ownable{

    using SafeMath for uint256;
    using SafeMath16 for uint;

    event RentCar(uint _id, address _renter, address _owner);
    event NewCar(uint _id, string _name);
    event Price(uint _price);
    //event AvailableNum(uint _num);
    event AvailableCar(uint _id, string _name, uint _rate_sum, uint _rate_num);

    mapping (uint => address) car2owner;
    mapping (address => uint) ownerTokenCount;
    
    struct Car {
        string name;
        address payable owner;
        address payable renter;
        uint rent_time; // now + expected renting time
        uint id;
        uint age;
        uint price;
        uint crash_number;
        uint rate_sum;
        uint rate_num;
    }

    Car[] cars;
    uint AvailableCarNum = 0;

    function Add_Car(string memory _name, uint _age, address payable _owner) internal { // call by car wallet
        
        Car memory newcar = Car(_name, _owner, _owner, now, 0, _age, 10, 0, 0, 0);
        uint id = cars.push(newcar) - 1;
        cars[id].id = id;
        car2owner[id] = _owner;
        ownerTokenCount[_owner]++;
        AvailableCarNum++;
        emit NewCar(id, _name);

    }

    function Is_Rented(uint _id) public view returns (bool){
        //return cars[_id].is_rented;
        /*return vtokens[_id].car.is_rented;*/
        return (cars[_id].owner != cars[_id].renter);
    }

    function Get_Renter(uint _id) public view returns(address) { //called when is rented is true
        return cars[_id].renter;
    }

    function Get_Available_Car_Num() external view returns(uint) {
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

    function Calculate_Price(uint _tokenId, uint _oil, uint crashes) internal view returns(uint) {
        uint to_owner = cars[_tokenId].price + _oil * 50;
        if (crashes > 0) {
            to_owner += 50 * crashes;
        }
        return to_owner;
    }

}