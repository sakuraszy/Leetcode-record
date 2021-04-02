class Solution:
    def maxArea(self, height: List[int]) -> int:
        left= 0
        right = len(height)-1
        mc =0
        for w in range(len(height)-1,0,-1):
            if height[left]<height[right]:
                mc = max(mc,height[left]*w)
                left+=1
            else:
                mc = max(mc,height[right]*w)
                right-=1
        return mc