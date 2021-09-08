/**
 * @param {number[][]} trips
 * @param {number} capacity
 * @return {boolean}
 */
var carPooling = function(trips, capacity) {
    let timeLine = {};
    let max = 0;
    let currentPassengers = 0;
    
    for (let [numPassengersi, from, to] of trips) {
        timeLine[from] = timeLine[from] || 0;
        timeLine[to] = timeLine[to] || 0;
        
        timeLine[from] += numPassengersi;
        timeLine[to] -= numPassengersi;
        max = Math.max(to, max);
    }
    
    for (let i = 0; i <= max; i++) {
        currentPassengers += timeLine[i] || 0;
        
        if (currentPassengers > capacity) return false;
    }
    
    return true;
};