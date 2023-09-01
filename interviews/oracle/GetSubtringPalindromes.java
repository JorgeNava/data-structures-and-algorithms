import java.util.ArrayList;

public class GetSubtringPalindromes {
  public static void main(String[] args) {
    String str = "MALAYALAM";
    ArrayList<String> palindromes = new ArrayList<>();

    for (int i = 0; i < str.length(); i++) {
      for (int j = i; j < str.length(); j++){
        String substring = str.substring(i, j + 1);
        if(isPalindrome(substring)){
          palindromes.add(substring);
        }
      }
    }

    for (String palindrome : palindromes) {
      System.out.println(palindrome);
    }
    System.out.println(palindromes.size());
  }

  public static boolean isPalindrome(String substring){
    final int size = substring.length();
    for (int i = 0; i < size / 2; i++) {
      if(substring.charAt(i) != substring.charAt(size - i - 1)) return false;
    }
    return true;
  }
}
