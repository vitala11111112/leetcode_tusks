class Solution:
    def isPalindrome(self, s: str) -> bool:
        answer = False
        s = s.lower().split()
        orig = ""
        for i in s:
            orig += i
            
        counter = 0
        while counter < len(orig):
            if orig[counter] not in "1234567890qwertyuiopasdfghjklzxcvbnm":
                orig = orig.replace(orig[counter],"")
                counter -= 1
            counter += 1
        if orig == orig[::-1]:
            answer = True
        return answer
        