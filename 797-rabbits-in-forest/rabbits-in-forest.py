class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq_map = {}

        for ans in answers:
            if ans in freq_map:
                freq_map[ans] += 1
            else:
                freq_map[ans] = 1

        output = 0

        for k, value in freq_map.items():
            q = value // (k + 1)
            r = value % (k + 1)

            if r > 0:
                q += 1

            output += q * (k + 1)

        return output