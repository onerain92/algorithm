/**
 * @param {number[][]} grid
 * @return {number}
 */
var islandPerimeter = function(grid) {
    let perimeter = 0;
    
    if (!grid.length) return perimeter;
    
    for (let x = 0; x < grid.length; x++) {
        for (let y = 0; y < grid[0].length; y++) {
            if (grid[x][y] === 1) {
                perimeter = getPerimeter(grid, x, y, perimeter);
            }
        }
    }
    
    return perimeter;
};

function getPerimeter(grid, x, y, perimeter) {    
    if (!(grid[x - 1] && grid[x - 1][y])) {
        perimeter += 1;
    }
    
    if (!(grid[x + 1] && grid[x + 1][y])) {
        perimeter += 1;
    }
    
    if (!grid[x][y - 1]) {
        perimeter += 1;
    }
    
    if (!grid[x][y + 1]) {
        perimeter += 1;
    }
    
    return perimeter;
}
