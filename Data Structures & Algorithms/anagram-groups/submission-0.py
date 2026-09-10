class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_group = {}

        for s in strs:
            sorted_s = ''.join(sorted(s))

            if sorted_s not in anagram_group:
                anagram_group[sorted_s] = []

            anagram_group[sorted_s].append(s)

        return list(anagram_group.values())        