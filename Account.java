import java.io.FileInputStream;
import java.io.IOException;
import java.util.Scanner;

public class Account {
 
    public static void main(String[] args) throws IOException{
        
        //Scanner scan = new Scanner(new FileInputStream("test.txt"));
        Scanner scan = new Scanner(System.in);
        Integer testCases = scan.nextInt();
        for(int i = 0; i<testCases; i++){
            Integer terms = scan.nextInt();
            System.out.println(terms % 2 == 0 ? 0 : 1);
        }
        scan.close();
    }

}

