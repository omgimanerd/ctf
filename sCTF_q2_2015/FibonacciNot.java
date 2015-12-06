import java.math.*;

public class FibonacciNot {
  public static BigInteger[] w_vals = new BigInteger[31];
  public static int maxCalc = 1;

  public static BigInteger getW(int n) {
    if (n < 2)
      return new BigInteger(Integer.toString(n));
    else if (n > maxCalc) {
      w_vals[n] = getW(n - 1).pow(2).add(getW(n - 2).pow(2));
      maxCalc = n;
    }
    return w_vals[n];
  }

  public static void main(String[] args) {
    int N = Integer.parseInt(args[0]);
    w_vals[0] = new BigInteger("0");
    w_vals[1] = new BigInteger("1");
    System.out.println(getW(N));
  }
}
