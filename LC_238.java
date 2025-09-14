import java.util.Arrays;

class Solution {
    public static int[] productExceptSelf(int[] nums) {
        int [] res = new int[nums.length];

        Arrays.fill(res, 1);

        int left = 1;

        for (int i = 0; i < res.length; i++) {
            res[i] = left;
            left *= nums[i];
        }

        //[1, 1, 2, 6]

        int right = 1;
        for (int i = res.length - 1; i >= 0; i--) {
            res[i] *= right;
            right *= nums[i];
        }


        return res;
    }

    public static void main(String[] args) {
        System.out.println( Arrays.toString(productExceptSelf(new int[]{1, 2, 4, 5})));
    }
}