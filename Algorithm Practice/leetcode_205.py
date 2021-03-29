class Solution:
    def __init__(self):
        self.map = {}

    def isIsomorphic(self, s: str, t: str) -> bool:
        for idx, c in enumerate(s):
            if c in self.map.keys() and self.map[c] != t[idx]:
                return False
            elif c not in self.map.keys():
                if t[idx] in self.map.values():
                    return False
                self.map[c] = t[idx]

        return True
