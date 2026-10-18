class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False

        s1_dict = Counter(s1)
        s2_dict = Counter(s2[:n1])

        if s1_dict == s2_dict:
            return True

        for r in range(n1, n2):
            l = r - n1
            left_char, right_char = s2[l], s2[r]
            s2_dict[left_char] -= 1
            s2_dict[right_char] += 1

            if s2_dict[left_char] == 0:
                del s2_dict[left_char]

            if s1_dict == s2_dict:
                return True
                        
        return False
