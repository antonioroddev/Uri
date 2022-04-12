import java.io.FileInputStream;
import java.io.IOException;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Bino {
   public static void main(String[] args) throws IOException {
       Scanner scan = new Scanner(new FileInputStream("test.txt"));
        scan.nextLine();

        List<String> valores = Arrays.asList(scan.nextLine().split(" "));

        long mult2 = valores.stream().filter(e -> Integer.parseInt(e) % 2 == 0).count();
        long mult3 = valores.stream().filter(e -> Integer.parseInt(e) % 3 == 0).count();
        long mult4 = valores.stream().filter(e -> Integer.parseInt(e) % 4 == 0).count();
        long mult5 = valores.stream().filter(e -> Integer.parseInt(e) % 5 == 0).count();

        System.out.println(mult2 + " Multiplo(s) de 2");
        System.out.println(mult3 + " Multiplo(s) de 3");
        System.out.println(mult4 + " Multiplo(s) de 4");
        System.out.println(mult5 + " Multiplo(s) de 5");
   } 
}
