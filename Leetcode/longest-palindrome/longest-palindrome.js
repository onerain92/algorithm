/**
 * @param {string} s
 * @return {number}
 */
var longestPalindrome = function(s) {
    const sMap = {};
    let isOddExistence = false;
    let result = 0;
    
    for (let i = 0; i < s.length; i++) {
        if (sMap.hasOwnProperty(s[i])) {
            sMap[s[i]] += 1;
        } else {
            sMap[s[i]] = 1;
        }
    }
    
    for (let s in sMap) {
        if (sMap[s] % 2 === 0) result += sMap[s];
        else {
            isOddExistence = true;
            result += sMap[s] - 1;
        }
    } 
    
    return isOddExistence ? result + 1 : result ;
};
