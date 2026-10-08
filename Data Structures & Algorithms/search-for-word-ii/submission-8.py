class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False 

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        res = set()
        visited = set()
        # Build the Trie
        root = TrieNode()
        for w in words:
            root.addWord(w)

        def backtrack(r,c, node, word):
            if (min(r,c) < 0 or r >= ROWS or c >= COLS or (r,c) in visited or board[r][c] not in node.children):
                return  
            
            visited.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.word:
                res.add(word)

            for dr,dc in directions:
                backtrack(r + dr, c + dc, node, word)
            visited.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                backtrack(r,c,root,"")
        return list(res)