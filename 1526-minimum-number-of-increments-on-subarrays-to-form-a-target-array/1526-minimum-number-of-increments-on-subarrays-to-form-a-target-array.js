/**
 * @param {number[]} target
 * @return {number}
 */
var minNumberOperations = function(target) {
    let answer = target[0];
    
    for (let i = 1; i < target.length; i++) {
        if (target[i] > target[i - 1]) {
            answer += target[i] - target[i - 1];
        }
    }
    
    return answer;
};