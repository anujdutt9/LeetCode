# Valid Sudoku

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Create list of 9 Empty Dictionaries
        # Each dictionary in the list denotes 1 row
        rows = [{} for _ in range(9)]
        # Each dictionary in the list denotes 1 column
        cols = [{} for _ in range(9)]
        # Each dictionary in the list denotes 1 3 x 3 box grid
        boxes = [{} for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)
                    # Get the box Index
                    box_idx = (i // 3) * 3 + (j // 3)
                    
                    # For each dictionary in the list, add key,count pairs
                    rows[i][num] = rows[i].get(num, 0) + 1
                    cols[j][num] = cols[j].get(num, 0) + 1
                    boxes[box_idx][num] = boxes[box_idx].get(num, 0) + 1
                    
                    # Check if the count for a value in a dictionary is > 1
                    if rows[i][num] > 1 or cols[j][num] > 1 or boxes[box_idx][num] > 1:
                        return False
        return True
