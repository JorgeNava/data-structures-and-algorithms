class GreatesAndLowerNums {
  public static void main(String[] args) {
    int nums[] = {1, 3, 41, 24, 434, 97, 42, 35, 0};
    int largest = nums[0], smallest = nums[0];
    int largestIndex = 0, smallestIndex = 0;

    for (int i = 1; i < nums.length; i++) {
      int num = nums[i];
      if(num > largest) {
        largest = num;
        largestIndex = i;
      }
      if(num < smallest){
        smallest = num;
        smallestIndex = i;
      } 
    }

    System.out.println(largest);
    System.out.println(largestIndex);
    System.out.println(smallest);
    System.out.println(smallestIndex);
  }
}
