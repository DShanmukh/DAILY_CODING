class Solution:
    def betterString(self, str1, str2):
        def sub(s):
            substrings = ['']
            for i in s:
                new_substrings = []
                for j in substrings:
                    new_substrings.append(j)
                    new_substrings.append(i + j)
                substrings = new_substrings
            return substrings

        l = sub(str1)
        l1 = sub(str2)
        return max(len,(l,l1))

# Example usage:
solution_instance = Solution()
result = solution_instance.betterString("abc", "def")
print(result)
