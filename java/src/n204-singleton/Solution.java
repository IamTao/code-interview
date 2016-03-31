package n204-singleton;

class Solution {
    /**
     * @return: The same instance of this class every time
     */
    private Solution(){
         
    }
    private static  volatile Solution instance = new Solution();
    
    public static Solution getInstance() {
        // write your code here
        return instance ;
    }
};