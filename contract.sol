// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleStorage {
    uint256 public storedValue;

    constructor(uint256 _initialValue) {
        storedValue = _initialValue;
    }

    function setStoredValue(uint256 _newValue) public {
        storedValue = _newValue;
    }

    function getStoredValue() public view returns (uint256) {
        return storedValue;
    }
}