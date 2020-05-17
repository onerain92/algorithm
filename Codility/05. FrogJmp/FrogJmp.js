/*

A small frog wants to get to the other side of the road. The frog is currently located at position X and wants to get to a position greater than or equal to Y. The small frog always jumps a fixed distance, D.

Count the minimal number of jumps that the small frog must perform to reach its target.

Write a function:

function solution(X, Y, D);

that, given three integers X, Y and D, returns the minimal number of jumps from position X to a position equal to or greater than Y.

For example, given:

  X = 10
  Y = 85
  D = 30
the function should return 3, because the frog will be positioned as follows:

after the first jump, at position 10 + 30 = 40
after the second jump, at position 10 + 30 + 30 = 70
after the third jump, at position 10 + 30 + 30 + 30 = 100
Write an efficient algorithm for the following assumptions:

X, Y and D are integers within the range [1..1,000,000,000];
X ≤ Y.
Copyright 2009–2020 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

*/

function solution(X, Y, D) {
  let quotient = Math.floor((Y - X) / D);
  let remainder = (Y - X) % D;

  if (remainder !== 0) {
    return quotient + 1;
  } else {
    return quotient;
  }
}

/*
해결방법:
목표 지점의 위치에서 현재 지점의 위치를 뺸 다음
한 번의 갈 수 있는 거리만큼으로 나눴을 때,
나머지가 있으면 아직 남은 거리가 있다는 뜻이므로
몫에 1을 더한 값을 리턴하고
나머지가 없으면 딱 맞아 떨어지므로 몫을 바로 리턴합니다.
*/
