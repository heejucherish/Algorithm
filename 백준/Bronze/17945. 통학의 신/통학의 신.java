import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int b = scanner.nextInt();

        for (int i = -1000; i <= 1000; i++) {
            if (i * i + 2 * a * i + b == 0) {
                System.out.print(i + " ");
            }
        }

    }
}
