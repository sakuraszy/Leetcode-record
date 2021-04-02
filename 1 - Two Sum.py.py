```python
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> temp = new HashMap<Integer,Integer>();
        for( int i =0;i < nums.length;i = i+1){
            if(temp.containsKey(target - nums[i] )){
                return new int[]{i,temp.get(target - nums[i])};
            }else{
                temp.put(nums[i],i);
            }
        }
        return new int[]{0,0};
    }
}
