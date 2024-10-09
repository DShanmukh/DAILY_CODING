import java.util.Scanner;
class Upper{
  public static void main (String args[])
  {
    Scanner sc=new Scanner(System.in);
    int n;
    n=sc.nextInt();
    int a[][],s=0,l=0,i,j;
    a=new int[n][n];
    for (i=0;i<n;i++)
    {
      for(j=0;j<n;j++)
      {
        a[i][j]=sc.nextInt();
      }
    }
    for(i=0;i<n;i++)
    {
      for(j=i;j<n;j++)
      {
        s+=a[i][j];
      }
    }
    for(i=0;i<n;i++)
    {
      for(j=0;j<i+1;j++)
      {
        l+=a[i][j];
      }
    }
    System.out.print(s+" "+l);
  }
}