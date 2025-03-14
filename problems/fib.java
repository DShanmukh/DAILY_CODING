import java.util.*;
class Fib{
  
  if(n<=1){
    return 1;
  }
  else{
    return n*Fib(n-1);
  }
}
class Naruto{
  public static void main(String args[]){
    Scanner sc=new Scanner(System.in);
    int n;
    n=sc.nextInt();
    System.out.println(Fib(n));
  }
}