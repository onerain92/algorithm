/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDisappearedNumbers = function(nums) {
    const result = [];
    const visitedNums = new Array(nums.length).fill(0);
    
    for(let i = 0; i < nums.length; i++) {
        if (!visitedNums[nums[i] - 1]) {
            visitedNums[nums[i] - 1] = 1;
        }
    }
    
    visitedNums.forEach((visit, index) => {
        if (!visit) result.push(index + 1);
    })
    
    return result;
};