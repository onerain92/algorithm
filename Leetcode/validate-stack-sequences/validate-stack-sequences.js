/**
 * @param {number[]} pushed
 * @param {number[]} popped
 * @return {boolean}
 */
var validateStackSequences = function(pushed, popped) {
    let i = 0;
    let j = 0;
    
    while (i < pushed.length) {
        if (pushed[i] === popped[j]) {
            j += 1;
            pushed.splice(i, 1);
            if (i > 0) i -= 1;
        } else {
            i += 1;
        }
    }
    
    if (pushed.length > 0) return false;
    else return true;
};