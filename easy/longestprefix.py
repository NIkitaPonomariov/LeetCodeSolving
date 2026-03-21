class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        longest = strs[0]
        for string in strs[1:]:
            idx = 0
            while idx < len(longest) and idx < len(string) and longest[idx] == string[idx]:
                idx += 1
            longest = longest[:idx]
            if longest == "": return longest
        return longest
                
        


"""
Write a function to find the longest common prefix string amongst an array of strings.
 If there is no common prefix, return an empty string "".
 Example 1: Input: strs = ["flower","flow","flight"] Output: "fl"
 Example 2: Input: strs = ["dog","racecar","car"] Output: "" 
Explanation: There is no common prefix among the input strings.
"""