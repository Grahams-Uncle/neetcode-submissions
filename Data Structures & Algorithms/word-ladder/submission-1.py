class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        words = set(wordList)
        index_mp = {} # word -> index 
        for idx, word in enumerate(wordList):
            index_mp[word] = idx
        
        adj = [set() for _ in range(len(wordList))] # word -> neighbors
        for i in range(len(wordList)):
            for j in range(len(wordList[i])):
                for c in range(ord('a'), ord('z') + 1):
                    new_word = wordList[i][:j] + chr(c) + wordList[i][j + 1:]
                    if new_word in wordList:
                        adj[i].add(index_mp[new_word])
                        adj[index_mp[new_word]].add(i)
        
        visit = set()
        q = deque() # queue of word index

        # add neighbors of begin words into queue
        for i in range(len(beginWord)):
            for c in range(ord("a"), ord("z") + 1):
                new_word = beginWord[:i] + chr(c) + beginWord[i+1:]
                if new_word in wordList:
                    q.append(index_mp[new_word])

        res = 1
        end_idx = index_mp[endWord]

        while q:
            res += 1
            for _ in range(len(q)):
                word_idx = q.popleft()
                if word_idx == end_idx:
                    return res 
                visit.add(word_idx)
                for nei in adj[word_idx]:
                    if nei not in visit:
                        q.append(nei)
        return 0 






        
