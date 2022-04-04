import java.io.FileInputStream;
import java.io.IOException;
import java.util.Scanner;
import java.util.stream.Stream;

public class Plug {
    
    public static void main(String[] args) throws IOException {
        
        Scanner scan = new Scanner(new FileInputStream("test.txt"));

        int p1 = scan.nextInt() - 1;
        int p2 = scan.nextInt() - 1;
        int p3 = scan.nextInt() - 1;
        int p4 = scan.nextInt();

        Integer result = Stream.of(p1,p2,p3,p4)
            .mapToInt(i -> Integer.valueOf(i))
            .sum();

        System.out.println(result);
    }

}
