import java.util.Scanner;
class Sumofdiagonals{
  public static void main(String args[])
  {
    Scanner sc=new Scanner(System.in);
    int n,m,a[][],i,j;
    n=sc.nextInt();
    m=sc.nextInt();
    a=new int[n][m];
    for(i=0;i<n;i++)
    {
      for(j=0;j<m;j++){
        a[i][j]=sc.nextInt();
      }
    }
    for(j= 0 ;j< m ;j++){
      for(i=0 ; i < n;i++){
        System.out.print((a[i][j])+" ");
      }
      System.out.println();
    }
  }
}