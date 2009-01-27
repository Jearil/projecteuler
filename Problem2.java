public class Problem2 {
    int sum;

    public Problem2() {
	sum = 0;
    }

    public void fib() {
	int old = 1;
	int second = 1;
	int nextNum = 0;

	while(nextNum < 4000000) {
	    nextNum = old + second;
	    old = second;
	    second = nextNum;
	    if (nextNum % 2 == 0) {
		sum += nextNum;
	    }
	}
    }

    public int getSum() {
	return this.sum;
    }

    public static void main(String[] args) {
	Problem2 p = new Problem2();
	p.fib();
	System.out.println("Sum is: " + p.getSum());
    }
}
