class Solution:
    def frequencySort(self, s: str) -> str:

        freq_map = {}
        result = []

        for ch in s:
            freq_map[ch] = freq_map.get(ch,0) + 1
        
        for ch in sorted(freq_map,key = freq_map.get,reverse = True):
            result.append(ch * freq_map[ch])

        return "".join(result)


        
        