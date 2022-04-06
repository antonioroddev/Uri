import java.io.FileInputStream;
import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;

public class WhatTea {
    public static void main(String[] args) throws IOException {
        Scanner scan = new Scanner(new FileInputStream("test.txt"));
        Integer teaType = scan.nextInt();
        scan.nextLine();
        long correctAnswers = Arrays
            .stream(scan.nextLine().split(" "))
            .filter(e -> Integer.valueOf(e) == teaType)
            .count();
        System.out.println(correctAnswers);
    }
}
