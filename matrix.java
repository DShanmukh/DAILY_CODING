import java.util.Scanner;
class matrix{
  public static void main(String args[])
  {
    Scanner sc=new Scanner(System.in);
    int n;
    int a[][],i,j,c=0,m=0,z=0;
    n=sc.nextInt();
    a=new int[n][n];
    for(i=0;i<n;i++)
    {
      for(j=0;j<n;j++)
      {
        a[i][j]=sc.nextInt();
      }
    }
    for(j=0;j<n;j++)
    {
      c=0;
      for(i=0;i<n;i++)
      {
        if(a[i][j]==0)
        {
          c++;
        }
      }
      if(m<c)
      {
        m=c;
        z=j;
      }
    }
    if(c==0)
    {
      System.out.print("-1");
    }
    else{
      System.out.print(z);
    }
  }
}