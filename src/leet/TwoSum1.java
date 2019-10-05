

/*
  Given an array of integers, return indices of the two numbers such that they add up to a specific target.

  You may assume that each input would have exactly one solution, and you may not use the same element twice.
*/


public class TwoSum1 {
    public static void main(String[] args) {
        int[] options = new int[]{11, 15, 2, 7};
        int target = 9;

        int[] result = twoSum(options, target);
        System.out.println(result[0] + " " + result[1]);
    }

    static int[] twoSum(int[] nums, int target) {

        int length = nums.length;
        for(int i = 0; i < length; ++i) {
            for(int j = i+1; j < length; ++j) {
                int sum = nums[i] + nums[j];

                if(sum == target) {
                    return new int[]{i, j};
                }
            }
        }

        return new int[]{};
    }
}
