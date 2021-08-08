/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let maxWater = 0;
    let x = 0;
    let y = height.length - 1;
    
    while (x < y) {
        if (height[x] < height[y]) {
            maxWater = Math.max(maxWater, (y - x) * height[x]);
            x += 1;
        } else {
            maxWater = Math.max(maxWater, (y - x) * height[y]);
            y -= 1;
        }
    }
    
    return maxWater;
};