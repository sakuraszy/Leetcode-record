class Solution(object):
    def trap(self, height):
        if len(height)<2:
            return 0
        total=0
        current = 0
        stop = current +1
        maxlength = len(height)-1
        while(height[maxlength-1]>height[maxlength]):
            maxlength-=1
        while(current <maxlength-1 and stop < maxlength):
            if(height[current] > height[stop]):
                total += height[current]-height[stop]
                stop +=1
            elif(height[current]==0):
                current +=1
                stop = current +1
            else:
                current = stop
                stop =current+1
            print('stop=',stop)
            print('current = ',current)
            print(total)
        if(stop == maxlength and height[stop]< height[current]):
            for x in height[current:stop]:
                total -= height[current]-x
                print(total)
        else:
            return total
        print('stop',stop)
        maxlength= current
        current = stop
        stop = current -1
        while(current>maxlength-1 and stop > maxlength):
            if(height[current] > height[stop]):
                total += height[current]-height[stop]
                stop -=1
            elif(height[current]==0):
                current -=1
                stop = current -1
            else:
                current = stop
                stop = current-1
            print('stop=',stop)
            print('current = ',current)
            print(total)
        return total
    
        """
        :type height: List[int]
        :rtype: int
        """
        