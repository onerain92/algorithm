/**
 * @param {number[]} students
 * @param {number[]} sandwiches
 * @return {number}
 */
var countStudents = function(students, sandwiches) {
    while (students.length) {
        const topOfSandwich = sandwiches[0];
        
        if (!students.includes(topOfSandwich)) {
            return students.length;
        }
        
        if (students[0] === topOfSandwich) {
            students.shift();
            sandwiches.shift();
        } else {
            students.push(students.shift());
        }
    }
    
    return 0;
};