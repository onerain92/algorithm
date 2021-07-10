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

// Solution 3
var findKthPositive = function (arr, k) {
  const n = arr.length;
  let left = 0;
  let right = n - 1;
  let missing = compute(arr[n - 1], n);

  while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    missing = compute(arr[mid], mid + 1);

    if (missing >= k) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }

  if (right === -1) return k;

  return arr[right] + k - compute(arr[right], right + 1);
};

function compute(actual, expected) {
  return actual - expected;
}
