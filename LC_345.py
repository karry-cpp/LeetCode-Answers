class Solution:
    def reverseVowels(self, st: str) -> str:
        vowels = {'a', 'i', 'o', 'u', 'e', 'A', 'E', 'I', 'O', 'U'}
        s = list(st)
        start, end = 0, len(s)-1
        #icecream

        while start < end:
            if s[start] not in vowels:
                start += 1
                continue
            if s[end] not in vowels:
                end -= 1
                continue

            temp = s[start]
            s[start] = s[end]
            s[end] = temp
            start += 1
            end -= 1


        return "".join(s)
    
print(Solution().reverseVowels("IceCreAm"))