import java.util.*;
public class Sumeq {
  public static void main(String args[]){
    Scanner s = new Scanner(System.in);
    int n, x , sum = 0, mat1[][] , mat2[][];
    int i ,j;
    n = s.nextInt();
    x = s.nextInt();
    mat1 = new int[n][n];
    mat2 = new int[n][n];
    for(i = 0 ;i < n; i++){
      for (j = 0 ; j < n ; j++){
        mat1[i][j] = s.nextInt();
      }
    }
    
    for(i = 0 ;i < n; i++){
      for (j = 0 ; j < n ; j++){
        mat2[i][j] = s.nextInt();
      }
    }
    for(i = 0 ;i < n; i++){
      for (j = 0 ; j < n ; j++){
        System.out.print(mat1[i][j]+" ");
        System.out.print(mat2[j][i]+" ");

      }
      System.out.print(" ");
    }
  }
}
