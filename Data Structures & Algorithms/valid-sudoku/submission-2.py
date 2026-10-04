class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r_count=defaultdict(set)
        c_count=defaultdict(set)
        box_count=defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue

                if (board[r][c] in r_count[r] or
                     board[r][c] in c_count[c] or
                     board[r][c] in box_count[r//3,c//3] 
                ):
                    return False
                
                r_count[r].add(board[r][c])
                c_count[c].add(board[r][c])
                box_count[r//3,c//3].add(board[r][c])
        
        return True

        