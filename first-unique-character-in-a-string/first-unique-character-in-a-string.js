/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function(s) {
    const letterCount = {};
    
    for (let i = 0; i < s.length; i++) {
        letterCount[s[i]] = letterCount[s[i]] + 1 || 1;
    }
    
    console.log(letterCount)
    
    for (let i = 0; i < s.length; i++) {
        if (letterCount[s[i]] === 1) {
            return i;
        }
    }
    
    return -1;
};