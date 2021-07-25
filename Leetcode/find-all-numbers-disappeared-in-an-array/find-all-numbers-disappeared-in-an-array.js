/**
 * @param {number[]} nums
 * @return {number[]}
 */
// solution1
var findDisappearedNumbers = function (nums) {
  const result = [];
  const visitedNums = new Array(nums.length).fill(0);

  for (let i = 0; i < nums.length; i++) {
    if (!visitedNums[nums[i] - 1]) {
      visitedNums[nums[i] - 1] = 1;
    }
  }

  visitedNums.forEach((visit, index) => {
    if (!visit) result.push(index + 1);
  });

  return result;
};

// solution 2
const findDisappearedNumbers = nums => {
  const result = [];

  for (let i = 0; i < nums.length; i++) {
    const index = Math.abs(nums[i]) - 1;
    if (nums[index] > 0) {
      nums[index] = -nums[index];
    }
  }

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] > 0) {
      result.push(i + 1);
    }
  }

  return result;
};
