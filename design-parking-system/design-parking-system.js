/**
 * @param {number} big
 * @param {number} medium
 * @param {number} small
 */
var ParkingSystem = function(big, medium, small) {
    this.big = big;
    this.medium = medium;
    this.small = small;
};

/** 
 * @param {number} carType
 * @return {boolean}
 */
ParkingSystem.prototype.addCar = function(carType) {
    let isParkingAvailable = false;
    
    switch (carType) {
        case 1:
            isParkingAvailable = this.big > 0;
            this.big--;
            break;
        case 2:
            isParkingAvailable = this.medium > 0;
            this.medium--;
            break;
        case 3:
            isParkingAvailable = this.small > 0;
            this.small--;
            break;
    }
    
    return isParkingAvailable;
};

/** 
 * Your ParkingSystem object will be instantiated and called as such:
 * var obj = new ParkingSystem(big, medium, small)
 * var param_1 = obj.addCar(carType)
 */