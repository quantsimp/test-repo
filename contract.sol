// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleStorage {
    uint256 public storedValue;

    event ValueUpdated(uint256 oldValue, uint256 newValue, address indexed caller);

    constructor(uint256 _initialValue) {
        storedValue = _initialValue;
    }

    function setStoredValue(uint256 _newValue) public {
        uint256 oldValue = storedValue;
        storedValue = _newValue;
        emit ValueUpdated(oldValue, _newValue, msg.sender);

    function getStoredValue() public view returns (uint256) {
        return storedValue;
    }
}