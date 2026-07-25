class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int a=0;
        int b=numbers.length-1;
        while (a<b){
            int curr_sum=numbers[a]+numbers[b];
            if (curr_sum==target){
                return new int[]{a+1,b+1};
            }
            else if (curr_sum<target){
                a++;
            }
            else{
                b--;
            }
        }
        return new int[]{-1,-1};
    }
}