import java.io.FileInputStream;
import java.io.IOException;
import java.util.Scanner;
 
/*
    @author: Antônio Rodrigues;
    @Question: 3170.
    * You have to change the class name to Main before submmiting it to
    * Beecrowd platform.
    * Use
 */ 
public class ChristmasMarble{
 
    public static void main(String[] args) throws IOException {
        
        FileInputStream inputStream = new FileInputStream("test.txt");
        Scanner scan = new Scanner(inputStream);

        while(scan.hasNext()){
            
            Integer marbleAmount = scan.nextInt();
            Integer branches = scan.nextInt();

            branches = branches % 2 ==0 ? branches : branches-1;

            Integer buyingAmountNeed = (branches / 2) - marbleAmount;

            if (buyingAmountNeed > 0){
                System.out.println("Faltam " + buyingAmountNeed + " bolinha(s)");
            }else{
                System.out.println("Amelia tem todas bolinhas!");
            }
            

        }

    }
 
}