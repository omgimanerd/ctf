import java.math.*;

public class Algo1 {
    public BigInteger g1 = new BigInteger("0");
    public BigInteger g2 = new BigInteger("1");
    public BigInteger w1 = new BigInteger("0");
    public BigInteger w2 = new BigInteger("1");
    public BigInteger total = new BigInteger("0");
    
    public BigInteger getG() {
	return g1;
    }
    public BigInteger getW() {
	return w1;
    }
    public BigInteger getTotal() {
	return total;
    }

    public long setTotal() {
	total = g1.subtract(w1); // g(30) - w(30);
	return sumDigits(total);
    }
    
    public static long sumDigits(BigInteger x) {
	BigInteger ten = new BigInteger("10");
	BigInteger zero = new BigInteger("0");
	long total = 0;
	while (x.compareTo(zero) > 0) {
	    BigInteger[] values = x.divideAndRemainder(ten); // [new x, rem]
	    x = values[0];
	    total += values[1].intValue();
	}
	return total;
    }
    
    public void g() {
	BigInteger g3 = new BigInteger("0");
	g3 = (g1.add(g2)).pow(2);
	g1 = g2;
	g2 = g3;
    }
    public void w() {
	BigInteger w3 = new BigInteger("0");
	w3 = (w1.pow(2)).add(w2.pow(2));
	w1 = w2;
	w2 = w3;
    }

    public static void main(String[] args) {
	/*
	for (int i = 0; i < 6; i++) {
	    System.out.println("g(" + i + "): " + g(i));
	    System.out.println("w(" + i + "): " + w(i));
	}
	System.out.println(sumDigits(1324567890L));
	System.out.println(new BigInteger("10"));
	*/
	Algo1 cha = new Algo1();
	for (int i = 0; i < 30; i++) { // g1 = g(30)
	    System.out.println("Calculating g(" + i + ")...");
	    cha.g();
	    // System.out.println(cha.getG());
	}
	for (int i = 0; i < 30; i++) { // g1 = g(30)
	    System.out.println("Calculating w(" + i + ")...");
	    cha.w();
	    // System.out.println(cha.getW());
	}
	System.out.println(cha.setTotal());
    }
}
