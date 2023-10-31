package java;

public class lcs {
    public static int LCSq(char[] s1,char[] s2,int m,int n){
        int[][] dp = new int[m+1][n+1];
        int MaxC = 0;
        for(int i=1;i<m;i++){
            for(int j=1;j<n;j++){
                if(m == 0 || n == 0){
                    return 0;
                }
                if(s1[i-1] == s2[j-1]){
                    dp[i][j] = 1 + dp[i-1][j-1];
                    MaxC= Math.max(dp[i][j],MaxC);
                }
                else {
                    dp[i][j] = 0;
                }
            }
        }
        return MaxC;
    }
    public static void main(String[] args) {
        String s3 = "ibcdfg";
        String s4 = "abcdghj";
        char[] s1 = s3.toCharArray();
        char[] s2 = s4.toCharArray();
        int m = s1.length;
        int n = s2.length;
        System.out.println(LCSq(s1,s2,m,n));
    }
}


