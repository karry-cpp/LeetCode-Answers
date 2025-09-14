import java.util.HashSet;
import java.util.Set;

class Solution {
    public String reverseVowels(String s) {
        
        Set<Character> vow = new HashSet<Character>(Set.of('a', 'e', 'i', 'o', 'u'));
        StringBuilder sb = new StringBuilder(s);
        int start = 0, end = s.length()-1;

        while(start < end) {
            
            if(!vow.contains(Character.toLowerCase(sb.charAt(start)))) {
                start += 1;
                continue;
            }

            if(!vow.contains(Character.toLowerCase(sb.charAt(end)))) {
                end -= 1;
                continue;
            }

            var temp = sb.charAt(start);
            sb.setCharAt(start, sb.charAt(end));
            sb.setCharAt(end, temp);

            start += 1;
            end -= 1;

        }

        return sb.toString();
    }
}