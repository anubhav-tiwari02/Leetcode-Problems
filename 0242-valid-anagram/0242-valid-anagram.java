class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character,Integer> map1=new HashMap<>();
        for(int i=0;i<s.length();i++){
            char ch=s.charAt(i);
            map1.put(ch,map1.getOrDefault(ch,0)+1);
        }
        HashMap<Character,Integer> map2=new HashMap<>();
        for(int j=0;j<t.length();j++){
            char ch2=t.charAt(j);
            map2.put(ch2,map2.getOrDefault(ch2,0)+1);
        }
        return map1.equals(map2);

    }
}