import java.util.*;
class snake
{
  public static void main(String args[]){
    Scanner sc=new Scanner(System.in);
    int n;
    n=sc.nextInt();
    int a[][],i,j;
    a=new int[n][n];
    ArrayList<Integer> arr=new ArrayList<>();
    for(i=0;i<n;i++)
    {
      for(j=0;j<n;j++)
      {
        a[i][j]=sc.nextInt();
      }
    }
    for(i=0;i<n;i++)
      {
        if(i%2==0)
        {
          for(j=0;j<n;j++)
          {
            arr.add(a[i][j]);
          }
        }
        else{
          for(j=n-1;j>=0;j--)
          {
            arr.add(a[i][j]);
          }
        }

      }
      arr.forEach(e->System.out.print(e+" "));
    }
}