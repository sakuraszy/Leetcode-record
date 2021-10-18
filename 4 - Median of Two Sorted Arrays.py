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
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=len(nums1)
        n=len(nums2)
        p1 = (m+1)//2+1
        p2= (m+n+1)//2-((m+1)//2)+1
        nums1.insert(0,-math.inf)
        nums2.insert(0,-math.inf)
        nums1.append(math.inf)
        nums2.append(math.inf)
        while(p1>0 and p1<m+2 and p2>0 and p2 <n+2):
            if nums1[p1-1]<=nums2[p2] and nums2[p2-1]<=nums1[p1]:
                break
            else:
                if nums1[p1-1]>nums2[p2]:
                    p1-=1
                    p2+=1
                else:                    
                    p1+=1
                    p2-=1
        if (m+n)%2==1:
            return max(nums1[p1-1],nums2[p2-1])
        else:
            return (max(nums1[p1-1],nums2[p2-1])+min(nums1[p1],nums2[p2]))/2