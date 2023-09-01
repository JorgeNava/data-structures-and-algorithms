public class IsArrayBalanced {
  public static void main(String[] args) {
    int nums[] = {1, -1};
    int balance = 0;

    for (int num : nums) {
      balance += num;
    }
    System.out.println("Is balanced: " + (balance == 0));
  }
  
}
