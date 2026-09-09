class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        count_t = Counter(t)
        need = len(count_t)
        l, r = 0, 0
        count_s = defaultdict(int)
        have = 0
        res = [0,0]
        resLen = float("infinity")
        for r in range(len(s)):
            count_s[s[r]] += 1
            if count_t[s[r]] and count_s[s[r]] == count_t[s[r]]:
                have += 1

            while have == need:
                if resLen > r - l + 1:
                    resLen = r - l + 1
                    res = [l, r]
            
                count_s[s[l]] -= 1
                if count_t[s[l]] and count_s[s[l]] + 1 == count_t[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen < float("infinity") else ""
                