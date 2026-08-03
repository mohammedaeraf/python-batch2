import java.util.Scanner;

public class RectangleArea {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the length: ");
        int length = sc.nextInt();

        System.out.print("Enter the breadth: ");
        int breadth = sc.nextInt();

        int area = length * breadth;

        System.out.println("Area = " + area);

        sc.close();
    }
}