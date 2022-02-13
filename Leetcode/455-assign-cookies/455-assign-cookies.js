/**
 * @param {number[]} g
 * @param {number[]} s
 * @return {number}
 */
var findContentChildren = function(g, s) {
    if (s.length === 0) return 0;
    
    let result = 0;
    const greed = g.sort((a, b) => a - b);
    const cookies = s.sort((a, b) => a - b);
    
    for (let i in cookies) {
      if (cookies[i] >= greed[result]) result++;
    }
    
    return result;
};