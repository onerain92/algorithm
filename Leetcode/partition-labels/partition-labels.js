/**
 * @param {string} s
 * @return {number[]}
 */
var partitionLabels = function(s) {
    const result = [];
    const lastLetterIndex = {};
    
    let start = 0;
    let end = 0;
    
    for (let i = 0; i < s.length; i++) {
        lastLetterIndex[s[i]] = i;
    }

    for (let i = 0; i < s.length; i++) {
        end = Math.max(end, lastLetterIndex[s[i]]);

        if (i === end) {
            result.push(end - start + 1);
            start = end + 1
        }
    }
    
  return result;
};