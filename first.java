import java.util.*;
class first{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int in1, in2,in3;
        in1 = sc.nextInt();
        in2 = sc.nextInt();
        in3 = sc.nextInt();
        int max= 0;
        int k,l,k1,o,p;
        k = in1 / 100;
        l = k % 10;
        k1 = in2/ 10;
        o = k1 % 10;
        while (in3!=0){
            p = in3 %10;
            if (p > max){
                max = p;
            } 
            in3 = (int)in3 /10;
        }
        System.out.println((l*o)*max);
    }
}