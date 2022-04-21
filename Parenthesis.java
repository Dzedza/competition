import java.util.Scanner;
import java.util.Stack;

public class Parethesis
{

    public static void main(String[] args)
    {
        Scanner sc = new Scanner (System.in);

        String s = sc.nextLine();
        Stack<Character> stack = new Stack<>();
        int q = Integer.parseInt(sc.nextLine());
        String open = "[{(<";
        String closed = "]{)>";
        StringBuilder result = new StringBuilder();

        for(int i = 0; i < q; ++i)
        {
            String[] tmp = sc.nextLine().split(" ");
            int b = Integer.parseInt(tmp[0]);
            int e = Integer.parseInt(tmp[1]);

            String check =  s.substring(b, e+1);

            for(int j = 0; j < check.length(); ++j)
            {
                if(open.indexOf(check.charAt(j)) != -1 )
                {
                    stack.push(check.charAt(j));
                }
                else {
                    char c = stack.pop();
                    if (open.indexOf(c) != closed.indexOf(check.charAt(j)))
                    {
                        result.append("0");
                    }
                    else result.append("1");

                }
            }

        }
        System.out.println(result);
    }



}