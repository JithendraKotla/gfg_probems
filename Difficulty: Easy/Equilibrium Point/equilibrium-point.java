class Solution {
    // Function to find equilibrium point in the array.
    public static int findEquilibrium(int arr[]) {
        // code here
        int total =0;
        
        for (int i : arr){
            total+=i;
        }
        
        int sub=0;
        
        for(int i =0;i<arr.length;i++){
            
            total-=arr[i];
            
            if(sub==total){
                return i;
            }
            
            sub+=arr[i];
            
        
            
        }
        return -1;
    }
}
