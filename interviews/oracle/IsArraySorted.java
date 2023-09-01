class IsArraySorted {  
  public static void main(String[] args) {
    int nums[] = {1, 3, 0, 23, 123, 3123};
    int prev = nums[0];
    boolean isSorted = true;

    for (int num : nums) {
      if(prev > num) isSorted = false;
    }
    System.out.println("Is sorted: " + isSorted);
  }
}
