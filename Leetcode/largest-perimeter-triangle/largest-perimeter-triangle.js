/**
 * @param {number[]} nums
 * @return {number}
 */
var largestPerimeter = function(nums) {
    const sortedNums = nums.sort(function(a, b) {
        return a - b;
    });
    
    let result = 0;
    let longestSideIndex = sortedNums.length - 1;
    let i = longestSideIndex - 2;
    let j = longestSideIndex - 1;
    
    while ( i >= 0 ) {        
        if ((sortedNums[i] + sortedNums[j]) > sortedNums[longestSideIndex]) {
            result = Math.max(result, sortedNums[i] + sortedNums[j] + sortedNums[longestSideIndex])
            break;
        } else {
            longestSideIndex--;
            i--;
            j--;
        }
    }
    
    return result;
};
