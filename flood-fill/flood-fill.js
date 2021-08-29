/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} newColor
 * @return {number[][]}
 */
var floodFill = function(image, sr, sc, newColor) {
    const target = image[sr][sc];
    if (target === newColor) return image;
    
    const queue = [[sr, sc]];
    while (queue.length > 0) {
        const [row, col] = queue.shift();
        
        if (image[row][col] === target) {
            image[row][col] = newColor;
            
            if(row - 1 >= 0 && image[row - 1][col] === target) {
                queue.push([row - 1, col]);
            }
            if(row + 1 < image.length && image[row + 1][col] === target){
                queue.push([row + 1, col]);
            }
            if(col + 1 < image[0].length && image[row][col + 1] === target){
               queue.push([row, col+1]);
            }
            if(col - 1 >= 0 && image[row][col - 1] === target){
               queue.push([row, col-1]);
            }
        }
    }
    
    return image;
};
