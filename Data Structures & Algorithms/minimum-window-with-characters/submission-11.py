class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        count_t = Counter(t)
        need = len(count_t)
        resLen = float("infinity")
        res = [0, 0]
        l = 0
        count_s = defaultdict(int)
        have = 0
        for r in range(len(s)):
            count_s[s[r]] += 1
            if count_s[s[r]] == count_t[s[r]]:
                have += 1
            while have == need:
                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    res = [l, r]    
                count_s[s[l]] -= 1
                if count_t[s[l]] and count_s[s[l]] + 1 == count_t[s[l]]:
                    have -= 1
                l += 1
        return s[res[0]:res[1] + 1] if resLen != float("infinity") else ""
                


                