class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 
        
        counter_1 = Counter(s1)
        need = len(counter_1)
        for i in range(len(s2)):
            counter_2 = defaultdict(int)
            match = 0
            for j in range(i, len(s2)):
                counter_2[s2[j]] += 1
                if counter_1[s2[j]] < counter_2[s2[j]]:
                    break
                if counter_1[s2[j]] and counter_1[s2[j]] == counter_2[s2[j]]:
                    match += 1
                if match == need:
                    return True
        return False 
                



