import java.io.FileInputStream;
import java.io.IOException;
import java.util.Scanner;

public class Combine {
    
public static void main(String[] args) throws IOException{
    
    Scanner scan = new Scanner(new FileInputStream("test.txt"));
    scan.nextLine();

    while(scan.hasNext()){

        String[] words = scan.nextLine().split(" ");

        int index = 0;
        String combinedWord ="";

        while(index < words[0].length() && index < words[1].length()){
            combinedWord = combinedWord + words[0].charAt(index) + words[1].charAt(index);
            index++;
        }

        if (index < words[0].length()){
            combinedWord = combinedWord + words[0].substring(index);
        }

        if(index < words[1].length()){
            combinedWord = combinedWord + words[1].substring(index);
        }

        System.out.println(combinedWord);
    }

}

}
