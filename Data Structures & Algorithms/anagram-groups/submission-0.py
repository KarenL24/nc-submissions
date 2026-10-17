class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for i in range(len(strs)):
            x = ''.join(sorted(strs[i]))
            groups[x].append(strs[i])
        
        return list(groups.values())