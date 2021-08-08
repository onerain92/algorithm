/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    const rowLength = grid.length;
    const columnLength = grid[0].length;
    
    let numberOfIslands = 0;
    
    for (let x = 0; x < rowLength; x++) {
        for (let y = 0; y < columnLength; y++) {
            if (grid[x][y] === '1') {
                numberOfIslands += 1;
                dfs(x, y, rowLength, columnLength, grid)
            }
        }
    }
    
    return numberOfIslands
};

function dfs(x, y, rowLength, columnLength, grid) {
    grid[x][y] = '-1';
    
    if (x > 0 && grid[x - 1][y] === '1') {
        dfs(x - 1, y, rowLength, columnLength, grid);
    }
    if (x < rowLength - 1 && grid[x + 1][y] === '1') {
        dfs(x + 1, y, rowLength, columnLength, grid);
    }

    if (y > 0 && grid[x][y - 1] === '1') {
        dfs(x, y - 1, rowLength, columnLength, grid);
    }

    if (y < columnLength - 1 && grid[x][y + 1] === '1') {
        dfs(x, y + 1, rowLength, columnLength, grid);
    }
}
    