class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        temp = {}

        for s in strs:

            sort_s = "".join(sorted(s))

            if sort_s in temp:
                temp[sort_s].append(s)
            else:
                temp[sort_s] = [s]

        return list(temp.values())