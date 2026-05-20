from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        
        # Step 1: build map
        for word in strs:
            sorted_word = tuple(sorted(word))   # use sorted letters as key
            anagram_map[sorted_word].append(word)
        
        # Step 2: collect groups
        result = []
        for value in anagram_map.values():
            result.append(value)
        
        return result
