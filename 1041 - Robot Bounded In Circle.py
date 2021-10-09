class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        ##direct [0,3]
        location=[0,0]
        direct=0
        for ins in instructions:
            if ins =="R":
                direct= (direct+1)%4
            elif ins=="L":
                direct=(direct-1)%4
            else:
                if direct==0:
                    location[1]+=1
                elif direct==1:
                    location[0]+=1
                elif direct==2:
                    location[1]-=1
                else:
                    location[0]-=1
        if (location[0]==0 and location[1]==0) or direct !=0:
            return True
        else:
            return False