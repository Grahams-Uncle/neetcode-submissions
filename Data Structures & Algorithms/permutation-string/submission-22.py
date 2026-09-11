class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 

        count_1 = Counter(s1)
        count_2 = Counter(s2[:len(s1)])
        need = len(count_1)
        have = 0
        for c, cnt in count_1.items():
            if count_2[c] == cnt:
                have += 1
        
        l,r = 0, len(s1) - 1
        for r in range(len(s1), len(s2)):
            if need == have:
                return True 
            count_2[s2[r]] += 1
            if count_1[s2[r]] and count_2[s2[r]] == count_1[s2[r]]:
                have += 1
            elif count_1[s2[r]] and count_2[s2[r]] - 1 == count_1[s2[r]]:
                have -= 1

            count_2[s2[l]] -= 1
            if count_1[s2[l]] and count_2[s2[l]] + 1 == count_1[s2[l]]: 
                have -= 1
            elif count_1[s2[l]] and count_2[s2[l]] == count_1[s2[l]]: 
                have += 1
            l += 1
        return need == have 
            

        
        
                



