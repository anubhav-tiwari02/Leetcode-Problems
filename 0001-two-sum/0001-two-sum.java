class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> map=new HashMap<>();
        for(int i=0;i<nums.length;i++){
            int curr=nums[i];
            int more=target-curr;
            if(map.containsKey(more)){
                return new int[]{map.get(more),i};
            }
            map.put(curr,i);
        }
        return new int[]{};
    }
}