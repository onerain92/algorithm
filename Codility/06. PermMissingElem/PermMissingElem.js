/*
An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

function solution(A);

that, given an array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].
Copyright 2009–2020 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
*/

function solution(A) {
  let obj = {};

  for (let i = 0; i < A.length; i++) {
    obj[A[i]] = i;
  }

  for (let i = 1; i <= A.length; i++) {
    if (!obj.hasOwnProperty(i)) return i;
  }

  return A.length + 1;
}

/*
해결방법:
1. 빈 객체를 생성한다.
2. A배열의 요소들을 객체의 키 값으로 사용하여 객체를 채운다.
3. A배열의 처음부터 끝까지 반복문을 돌면서 객체에 키 값들이 순서대로 들어 있는지 확인한다.
4. 만약 없으면 해당하는 순서의 i 값을 리턴한다.
5. 모든 요소들이 다 있다면 A배열의 길이 값에 1을 더한 값이 다음 숫자이므로 그 값을 리턴한다.
*/
