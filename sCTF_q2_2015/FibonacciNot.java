import java.math.*;
import java.io.PrintWriter;
import java.lang.Exception;

public class FibonacciNot {
  public static BigInteger[] w_vals = new BigInteger[31];
  public static int maxCalc = 1;

  public static BigInteger getW(int n) {
    if (n < 2)
      return new BigInteger(Integer.toString(n));
    else if (n > maxCalc) {
      w_vals[n] = getW(n - 1).pow(2).add(getW(n - 2).pow(2));
      maxCalc = n;
      System.out.print(n + " ");
    }
    return w_vals[n];
  }

  public static BigInteger getF(int n) {
    return getW(n).multiply(getW(n - 1));
  }

  public static BigInteger sum(BigInteger n) {
    BigInteger sum = new BigInteger("0");
    BigInteger base = new BigInteger("10");
    BigInteger zero = new BigInteger("0");
    BigInteger length = new BigInteger("0");
    while (n.compareTo(zero) > 0) {
      length = length.add(new BigInteger("1"));
      if (length.mod(base.pow(1)).intValue() == 0)
        System.out.println(sum);
      BigInteger digit = n.remainder(base);
      sum = sum.add(digit);
      n = n.divide(base);
    }
    return sum;
  }
  
  public static void main(String[] args) {
    try (PrintWriter w = new PrintWriter("fibonacci_out.txt", "UTF-8")) {
      int N = Integer.parseInt(args[0]);
      w_vals[0] = new BigInteger("0");
      w_vals[1] = new BigInteger("1");
      BigInteger f = getF(N);
      w.println(sum(f));
    } catch (Exception e) {
      System.out.println("File not found");
    }
  }
}
