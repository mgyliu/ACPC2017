import java.util.Scanner;

class GetInputFromUser {
    public static void main(String args[]) {
        int a;
        int b;
        Scanner in = new Scanner(System.in);

        while(true){

            a = in.nextInt();
            b = in.nextInt();
            float result = (float)a/b;
            System.out.println(result);
        }
    }
}


