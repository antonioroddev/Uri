import java.io.FileInputStream;
import java.io.IOException;
import java.util.Scanner;

public class Combine {
    
public static void main(String[] args) throws IOException{
    
    Scanner scan = new Scanner(new FileInputStream("test.txt"));
    scan.nextLine();

    while(scan.hasNext()){

        String[] palavras = scan.nextLine().split(" ");

        int index = 0;
        String combinedWord ="";
        
        while(index < palavras[0].length() && index < palavras[1].length()){
            combinedWord = combinedWord + palavras[0].charAt(index) + palavras[1].charAt(index);
            index++;
        }

        while(index < palavras[0].length()){
            combinedWord = combinedWord + palavras[0].charAt(index);
            index++;
        }


        while(index < palavras[1].length()){
            combinedWord = combinedWord + palavras[1].charAt(index);
            index++;
        }

        System.out.println(combinedWord);
    }

}

}
