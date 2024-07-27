class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        mos = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        dic = {}

        for w in words:
            rep = ''
            for c in w:
                rep += mos[ord(c) - 97]
            
            if rep in dic:
                dic[rep] += 1
            else:
                dic[rep] = 1
        
        return len(dic)