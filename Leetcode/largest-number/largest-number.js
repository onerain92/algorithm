/**
 * @param {number[]} nums
 * @return {string}
 */
var largestNumber = function(nums) {
    const sortedNums = nums.sort(function(a, b) {
        a = String(a);
        b = String(b);
        return Number(b + a) - Number(a + b);
    })
    
    return Number(sortedNums.join('')) === 0 ? '0' : sortedNums.join('');
};
