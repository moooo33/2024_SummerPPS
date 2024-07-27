class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        if month < 3:
            month += 12
            year -= 1
        a = year % 100
        b = year // 100
        d = (day + (13 * (month + 1)) // 5 + a + (a // 4) + (b // 4) - (2 * b)) % 7
        return week[d]