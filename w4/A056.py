class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic = {}
        rtn = []
        for i in range(len(nums2)):
            dic[nums2[i]] = i
        
        for i in range(len(nums1)):
            rtn.append(-1)
            for j in range(dic[nums1[i]] + 1, len(nums2)):
                if nums2[j] > nums1[i]:
                    rtn[-1] = nums2[j]
                    break 

        return rtn