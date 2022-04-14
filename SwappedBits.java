import java.io.FileInputStream;
import java.io.IOException;
import java.util.Scanner;

public class SwappedBits {
 public static void main(String[] args) throws IOException {
     
    Scanner scan = new Scanner(new FileInputStream("test.txt"));
    
    for(int i = 1; true ; i++){
        Integer value = scan.nextInt();
        if (value == 0) break;
        System.out.println("Teste " + i);
        int bill50 = value > 50 ? value / 50: 0;
        int bill10 = (value % 50) > 10 ? (value % 50) / 10: 0;
        int bill5  = (value % 50) % 10 > 5 ? ((value % 50) % 10) / 5: 0;
        int bill1  = ((value % 50) % 10) % 5 >= 1 ? ((value % 50) % 10) % 5: 0;
        System.out.printf("%d %d %d %d", bill50, bill10, bill5, bill1);
        System.out.println("\n");
    }

 }  
}
