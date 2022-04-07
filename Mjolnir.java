import java.io.FileInputStream;
import java.io.IOException;
import java.util.Scanner;

public class Mjolnir {
    public static void main(String[] args) throws IOException {
        
        Scanner scan = new Scanner(new FileInputStream("test.txt"));
        scan.nextInt();
        scan.nextLine();
        while(scan.hasNext()){
            System.out.println(scan.nextLine()
                .split(" ")[0].equals("Thor") ? "Y" : "N");
        }     

    }
}
