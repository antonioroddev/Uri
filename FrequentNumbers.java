import java.io.FileInputStream;
import java.io.IOException;
import java.util.*;
import java.util.Scanner;
import java.util.stream.Collectors;

public class FrequentNumbers {
    public static void main(String[] args)  throws IOException{
        
        Scanner scan = new Scanner(new FileInputStream("test.txt"));
        scan.nextLine();

        List<String> numbers = new ArrayList<>();

        while(scan.hasNext()) numbers.add(scan.next());

       numbers.stream()
            .map(Integer::valueOf)
            .collect(Collectors.groupingBy(e -> e))
            .entrySet()
            .stream()
            .sorted(Map.Entry.comparingByKey())
            .forEach( e -> 
                    System.out.println(e.getKey() + 
                    " aparece " + 
                    e.getValue().size() + 
                    " vez(es)")
                        );
    }
}
