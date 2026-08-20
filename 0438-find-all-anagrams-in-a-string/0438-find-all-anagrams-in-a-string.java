class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> res=new ArrayList<>();
        int n=p.length();
        if(s.length()<n){
            return res;
        }
        int pCount[]=new int[26];
        int sCount[]=new int[26];
        for(char ch:p.toCharArray()){
            pCount[ch-'a']++;
        }
        int left=0;
        for(int right=0;right<s.length();right++){
            sCount[s.charAt(right)-'a']++;
            if(right-left+1>n){
                sCount[s.charAt(left)-'a']--;
                left++;
            }
            if(right-left+1==n){
                if(Arrays.equals(sCount,pCount)){
                    res.add(left);
                }
            }
        }
        return res;
    }
}