class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pos1 = 0
        pos2 =0
        count = 0
        totallen= len(nums1)+len(nums2)
        temp = 0
        while(pos1<len(nums1) or pos2<len(nums2)):
            if(pos1 >= len(nums1)):
                nextv = nums2[pos2]
                pos2+=1
            elif(pos2 >= len(nums2)):
                nextv = nums1[pos1]
                pos1+=1
            else:
                if(nums1[pos1]< nums2[pos2]):
                    nextv = nums1[pos1]
                    pos1+=1
                else:
                    nextv= nums2[pos2]
                    pos2+=1
            count +=1
            if totallen%2 ==1:
                if count ==(int(totallen/2)+1):
                    return nextv
            else:
                if count ==int(totallen/2):
                    temp +=nextv
                elif count ==(int(totallen/2)+1):
                    temp+=nextv
                    return temp/2
                