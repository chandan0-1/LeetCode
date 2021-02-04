class Solution {
    public int findLHS(int[] nums) {
        int maxCount = 0;
        for(int i = 0;i < nums.length;i++){
            int counti = 0,countd = 0;
            boolean flag1 = false;
            boolean flag2 = false;
            for(int j = i;j < nums.length;j++){
                
                if(nums[j] == nums[i] - 1 || nums[j] == nums[i]){
                    countd++;
                    
                }
                if(nums[j] == nums[i] - 1){
                    flag1 = true;
                }
                
                 if(nums[j] == nums[i] + 1 || nums[j] == nums[i]){
                    counti++;
                     
                }
                if (nums[j] == nums[i]+1){
                    flag2 = true;
                }
            }
            if (!flag1){
                countd = 0; 
            }
            if (!flag2){
                counti = 0;
            }

            int temp =  Math.max(counti,countd); 
            
            if(temp > maxCount){
                maxCount = temp;
            }
        }
        return maxCount;
    }
}
