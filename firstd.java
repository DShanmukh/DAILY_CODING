import java.util.*;
public class firstd{
  public static void main(String args[])
  {
    Scanner sc = new Scanner(System.in);
    int [] a = {1,3,2};
    int input1 = 2;
    int []a1 = {2,3,57,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97};
    int []a2 = new int[a1.length];
    int k = 0;
    for (int i = 0 ;i < a1.length;i++)
    {
      if (i == input1){
        k = a1[i-1];
      }
    }
    for (int i =0;i< a.length;i++)
    {
      a2[i] = a[i]+k;
    }
    return a2;
  }

}