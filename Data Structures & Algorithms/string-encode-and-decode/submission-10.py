class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:
            result += str(len(s)) + "#" + s

        print(result)
        
        return result

    def decode(self, s: str) -> List[str]:
        decodeList = []

        i = 0
        lengthStr = ""
        while i < len(s):

            if s[i] == "#":
                length = int(lengthStr)
                if length == 0:
                    decodeList.append("")
                    i += 1
                elif i+1 < len(s):
                    start = i+1 #+2: skipp #
                    end = start + length #counted for exclusive

                    decodeList.append(s[start : end])
                    i = end
                    lengthStr = ""
            else:
                lengthStr += s[i]
                i += 1
            

        return decodeList