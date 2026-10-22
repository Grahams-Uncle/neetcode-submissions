class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0

        patterns = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                p = word[:i] + "*" +  word[i + 1:]
                patterns[p].append(word)
        for i in range(len(beginWord)):
            p = beginWord[:i] + "*" +  beginWord[i + 1:]
            patterns[p].append(beginWord)

        visited = set()
        q = deque([beginWord])
        res = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res 
                visited.add(word)
                for i in range(len(word)):
                    p = word[:i] + "*" +  word[i + 1:]
                    for nei in patterns[p]:
                        if (nei != word) and (nei not in visited):
                            q.append(nei)
            res += 1
        return 0

        








        
