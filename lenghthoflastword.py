class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = s.split()
        last_word  = x[len(x)-1]
        return len(last_word);
