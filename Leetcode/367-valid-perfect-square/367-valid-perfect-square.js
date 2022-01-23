/**
 * @param {number} num
 * @return {boolean}
 */
var isPerfectSquare = function(num) {
    const squareRoot = num ** 0.5;
    
    if (squareRoot % 1 === 0) return true;
    
    return false;
};