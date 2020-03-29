function solution(N) {
  let binary = N.toString(2);
  let max = 0;
  let count = 0;

  let startOne = binary.indexOf('1');
  let isZeroExisted = binary.indexOf('0');

  if (isZeroExisted < 0) return 0;
  if (startOne < 0) return 0;
  if (startOne === binary.length - 1) return 0;

  for (let i = startOne + 1; i < binary.length; i++) {
    if (binary[i] === '0') {
      count = count + 1;
    } else if (binary[i] === '1') {
      if (count > max) {
        max = count;
        count = 0;
      } else {
        count = 0;
      }
    }
  }

  return max;
}
