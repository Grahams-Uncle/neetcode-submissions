class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0

        q = deque([beginWord]) # queue of words(str)
        res = 1
        visit = set()
        words = set(wordList)
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res 
                visit.add(word)
                for i in range(len(word)):
                    for c in range(ord("a"), ord("z") + 1):
                        new_word = word[:i] + chr(c) + word[i + 1:]
                        if (new_word not in visit) and (new_word in words):
                            q.append(new_word)
                            words.remove
            res += 1
        return 0







        
