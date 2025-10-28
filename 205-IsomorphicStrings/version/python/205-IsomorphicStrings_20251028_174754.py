# Last updated: 10/28/2025, 5:47:54 PM
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Approach - 1: Two hashmaps
        hash_map_s = dict()
        hash_map_t = {}

        for i in range(len(s)):
            if s[i] not in hash_map_s:
                hash_map_s[s[i]] = i

            if t[i] not in hash_map_t:
                hash_map_t[t[i]] = i

            if hash_map_s[s[i]] != hash_map_t[t[i]]:
                return False

        return True
