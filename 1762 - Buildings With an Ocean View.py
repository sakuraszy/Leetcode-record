class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        result=[len(heights)-1]
        for i in range(len(heights)-2,-1,-1):
            if heights[i]>heights[result[0]]:
                result.insert(0,i)
        return result