/**
 * @param {number[]} timeSeries
 * @param {number} duration
 * @return {number}
 */
var findPoisonedDuration = function(timeSeries, duration) {    
    return timeSeries.reduce((acc, cur, i, arr) => 
        arr[i + 1] - cur < duration ? acc + arr[i + 1] - cur : acc + duration
    , 0);
};
