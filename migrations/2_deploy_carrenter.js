const CarRenter = artifacts.require("./CarRenter.sol");

module.exports = function(deployer) {
  deployer.deploy(CarRenter);
};
