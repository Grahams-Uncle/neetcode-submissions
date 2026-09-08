class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 
        
        count1 = Counter(s1)
        need = len(count1)
        count2 = Counter(s2[:len(s1)])
        match = 0
        for c, count in count1.items():
            if count2[c] == count:
                match += 1
        l = 0
        for r in range(len(s1), len(s2)):
            if match == need:
                return True
            count2[s2[r]] += 1
            if count1[s2[r]] and count2[s2[r]] == count1[s2[r]]:
                match += 1
            elif count1[s2[r]] and count2[s2[r]] - 1 == count1[s2[r]]:
                match -= 1

            count2[s2[l]] -= 1
            if count1[s2[l]] and count2[s2[l]] == count1[s2[l]]:
                match += 1
            elif count1[s2[l]] and count2[s2[l]] + 1 == count1[s2[l]]:
                match -= 1
            l += 1
        return match == need 

            
                



