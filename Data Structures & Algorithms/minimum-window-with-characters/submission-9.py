class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        count_t = Counter(t)
        need = len(count_t)
        have = 0
        count_s = defaultdict(int)
        res = [0,0]
        length = float("infinity")
        l = 0
        for r in range(len(s)):
            count_s[s[r]] += 1
            if count_t[s[r]] and count_s[s[r]] == count_t[s[r]]:
                have += 1

            while have == need:
                if (r - l + 1) < length:
                    res = [l, r]
                    length = (r - l + 1)

                count_s[s[l]] -= 1
                if count_t[s[l]] and count_s[s[l]] + 1 == count_t[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r + 1] if length < float("infinity") else ""
                

                