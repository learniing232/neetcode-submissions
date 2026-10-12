class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length()!=t.length()) {return false;}
        HashMap<Integer,Integer> word = new HashMap<>();

        char[] sarray = s.toCharArray();
        char[] tarray = t.toCharArray();

        for (int i : sarray) {
            if (word.containsKey(i)) {word.put(i,word.get(i)+1);}
            else {word.put(i,1);}
        }

        for (int i : tarray) {
            if (word.containsKey(i) && word.get(i)>=1) {
                word.put(i,word.get(i)-1);
            } else {return false;}
        }
        return true;
    }
}
