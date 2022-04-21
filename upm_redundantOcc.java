import java.util.Scanner;
import java.lang.Math;
import java.util.Vector;

public class redundantOcc {
    public static void main(String[] args){
        Scanner sc= new Scanner(System.in);
        int n= sc.nextInt();
        int k= sc.nextInt();
        int s1= sc.nextInt();
        int s2= sc.nextInt();
        long x= sc.nextLong();
        long y= sc.nextLong();
        int m= sc.nextInt();
        int a= sc.nextInt();
        int b= sc.nextInt();
        sc.close();
        int[] seq= new int[n];
        seq[0]=s1;
        seq[1]=s2;
        for(int i=2;i<n;i++){
            seq[i]=(int)((s1*x+s2*y)%m);
            s1=s2;
            s2=seq[i];
        }
        int[] cnt= new int[m];
        for(int i=n-1;i>=0;i--){
            if(cnt[seq[i]]<k){
                cnt[seq[i]]++;
            }
            else{
                seq[i]=-1;
            }
        }
        int i=0;
        int j=0;
        while(i<n){
            if(seq[i]!=-1 && j>=a-1 && j<=b-1){
                System.out.print(seq[i]+" ");
            }
            if(seq[i]!=-1){
                j++;
            }
            i++;
        }
    }
}