/**
 * @param {string} s
 * @return {number}
 */
var calculate = function(s) {
    const stack = [];
    s = s.replace(/(\s*)/g, '');
    const arr = s.split(/([+*-\/])/);
    let lastOperator = '+';
    
    for (let i = 0; i < arr.length; i++) {
        const current = arr[i];
        
        if (lastOperator === '+') {
            stack.push(parseInt(current));
        } else if (lastOperator === '-') {
            stack.push(-parseInt(current));
        } else if (lastOperator === '*') {
            stack.push(stack.pop() * parseInt(current));
        } else if (lastOperator === '/') {
            stack.push(Math.trunc(stack.pop() / parseInt(current)));
        }
        
        lastOperator = current;
    }
    
    return stack.reduce((arr, cur) => arr + cur, 0);
};