class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        word = title.split()
        for i in range(len(word)) :
            if len(word[i]) <= 2 : word[i] = word[i].lower()
            else : word[i] = word[i].capitalize()

        return " ".join(word)