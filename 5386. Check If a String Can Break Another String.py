class Solution(object):
    def checkIfCanBreak(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n1=sorted(s1)
        n2=sorted(s2)
        r1=True
        r2=True
        for i in range(len(n1)):
            if n1[i] < n2[i]:
                r1 = False
        for i in range(len(n2)):
            if n1[i] > n2[i]:
                r2 = False
        return r1 or r2

sln=Solution()
assert True==sln.checkIfCanBreak(s1 = "abc", s2 = "xya")
assert True==sln.checkIfCanBreak(s1 = "leetcodee", s2 = "interview")
assert False==sln.checkIfCanBreak(s1 = "abe", s2 = "acd")