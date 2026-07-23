class Solution {
    public boolean isGood(int[] nums) {
        HashMap<Integer,Integer> map=new HashMap<>();
        for(int num:nums){
            map.put(num,map.getOrDefault(num,0)+1);
        }
        int max=0;
        for(int num:nums){
            max=Math.max(max,num);
        }
        int n=nums.length-1;
        if(map.getOrDefault(n,0)!=2){
            return false;
        }
        if(max!=n){
            return false;
        }
        for(int i=1;i<n;i++){
            if(map.getOrDefault(i,0)!=1){
                return false;
            }
        }
        return true;
    }
}