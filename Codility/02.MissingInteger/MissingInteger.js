function solution(A) {
  if (A.length === 1) {
    if (A[0] > 1 || A[0] < 0) return 1;
    if (A[0] === 0 || A[0] === 1) return A[0] + 1;
  }

  let arr = A.sort((a, b) => {
    return a - b;
  });

  let max = Math.max.apply(null, arr);
  let positiveIndex = 0;

  if (max < 0) {
    return 1;
  } else {
    for (let i = 0; i < arr.length; i++) {
      if (arr[i] < 0) {
        continue;
      } else {
        positiveIndex = i;
        break;
      }
    }
  }

  arr = arr.slice(positiveIndex);
  if (arr[0] > 1) return 1;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === arr[i + 1] || arr[i] + 1 === arr[i + 1]) {
      continue;
    } else {
      return arr[i] + 1;
    }
  }
}
