/*
- 직사각형을 만드는데 필요한 4개의 점 중 3개의 좌표가 주어질 때, 나머지 한 점의 좌표를 구하려고 합니다.
   점 3개의 좌표가 들어있는 배열 v가 매개변수로 주어질 때, 직사각형을 만드는 데 필요한 나머지 한 점의 좌표를
   return 하도록 solution 함수를 완성해주세요. 단 직사각형의 각 변은 x축, y축에 평행하며, 반드시 직사각형을
   만들 수 있는 경우만 입력으로 주어집니다.

   ex) 1. v = [[1, 4], [3, 4], [3, 10]] => result = [1,10]
       2. v = [[1, 1], [2, 2], [1, 2]] => result = [2, 1]
*/

function solution(v) {
  let answer = [];
  let tmpX = {};
  let tmpY = {};

  for (let i = 0; i < v.length; i++) {
    if (tmpX.hasOwnProperty(v[i][0])) {
      tmpX[v[i][0]] += 1;
    } else {
      tmpX[v[i][0]] = 1;
    }

    if (tmpY.hasOwnProperty(v[i][1])) {
      tmpY[v[i][1]] += 1;
    } else {
      tmpY[v[i][1]] = 1;
    }
  }

  for (let x in tmpX) {
    if (tmpX[x] === 1) {
      answer[0] = Number(x);
    }
  }

  for (let y in tmpY) {
    if (tmpY[y] === 1) {
      answer[1] = Number(y);
    }
  }

  return answer;
}
