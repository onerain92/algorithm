// Solution 1
var findKthPositive = function (arr, k) {
  let oneToThousand = [0];

  for (let i = 1; i <= arr[arr.length - 1] + k; i++) {
    oneToThousand[i] = i;
  }

  for (let i = 0; i < arr.length; i++) {
    const index = oneToThousand.indexOf(arr[i]);
    oneToThousand.splice(index, 1);
  }

  return oneToThousand[k];
};


// Solution 2
var findKthPositive = function (arr, k) {
  let oneToThousand = new Map();

  for (let i = 1; i <= arr[arr.length - 1] + k; i++) {
    oneToThousand.set(i, 1);
  }

  for (let i = 0; i < arr.length; i++) {
    oneToThousand.delete(arr[i]);
  }

  const keys = [...oneToThousand.keys()];

  return keys[k - 1];
};
