//LINEAR SEARCH
class linear{
    public static void main(String[]args){
        int nums[] = {5,7,9,11,13};
        int target = 11;
        int result = LinearSearch(nums,target);
        if(result!=-1){
            System.out.print("Element found at index : " + result);
        }
        else{
            System.out.print("Element not found");
        }



    }

    public static int LinearSearch(int[] nums, int target) {
        for(int i=0; i<nums.length; i++){
            if(nums[i]==target)
                return i;
    
        }
        return -1;
        
    }  //gayu
}