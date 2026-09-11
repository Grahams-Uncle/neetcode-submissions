class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 

        count_1 = Counter(s1)
        need = len(count_1)
        for i in range(len(s2)):
            count_2 = defaultdict(int)
            have = 0
            for j in range(i, len(s2)):
                count_2[s2[j]] += 1
                if count_2[s2[j]] > count_1[s2[j]]:
                    break
                if count_2[s2[j]] == count_1[s2[j]]:
                    have += 1
                if have == need:
                    return True 
        return False 




            
                



