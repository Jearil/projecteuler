import java.util.List;
import java.util.ArrayList;
import java.lang.StringBuffer;
import java.io.*;

public class Problem13 {
	public static void main(String[] args) throws Exception {
		ArrayInt sum = new ArrayInt();
		BufferedReader reader = new BufferedReader(new FileReader("13input"));

		for(String line = reader.readLine(); line != null; line = reader.readLine()) {
			ArrayInt item = new ArrayInt(line);
			sum = sum.add(item);
			System.out.println("Partial sum: " + sum);
		}
		System.out.println("The total is: " + sum);
	}
}

class ArrayInt {
	private List<Integer> number;
	
	public ArrayInt() {
		number = new ArrayList<Integer>(50);
	}
	
	public ArrayInt(String digits) {
		this();
		for(int i = digits.length() - 1; i >= 0; i--) {
			this.addDigit(Integer.parseInt(digits.charAt(i) + ""));
		}
		this.reduce();
	}
	
	public ArrayInt add(ArrayInt a) {
		return add(a, this);
	}
	
	public ArrayInt add(ArrayInt a, ArrayInt b) {
		ArrayInt result = new ArrayInt();
		
		for(int i = 0; i < a.size() || i < b.size(); i++) {
			result.addDigit(a.getDigit(i) + b.getDigit(i));
			//result.reduce();
			//System.out.print(".");
		}
		result.reduce();
		return result;
	}
	
	public int size() {
		return this.number.size();
	}
	
	public void addDigit(Integer i) {
		this.number.add(i);
	}
	
	public Integer getDigit(int index) {
		if (index >= number.size()) {
			return 0;
		} else {
			return number.get(index);
		}
	}
	
	private void reduce() {
		for(int i = 0; i < this.size(); i ++) {
			Integer num = this.getDigit(i);
			if(num >= 10) {
				Integer lastNum = getLastNum(num);
				//System.out.println("Last number of " + num + " is " + lastNum);
				this.setDigit(lastNum, i);
				Integer remainder = num / 10;
				//System.out.println("Remainter of " + num + " is " + remainder);
				if (this.size() > i + 1) {
				  //System.out.println("Adding " + remainder + " to digit " + getDigit(i + 1));
					this.setDigit(remainder + getDigit(i + 1), i + 1);
				}
				else {
				  //System.out.println("Adding new digit");
					this.addDigit(remainder + getDigit(i + 1));
				}
			}
		}
	}
	
	private Integer getLastNum(Integer num) {
		int n = num;
		while(n >= 10) {
			n -= 10;
		}
		return n;
	}
	
	private void setDigit(Integer digit, int index) {
		number.set(index, digit);
	}
	
	public String toString() {
		StringBuffer sb = new StringBuffer();
		//this.reduce();
		for(Integer i: number) {
			sb.append(i);
		}
		sb.reverse();
		return sb.toString();
	}
}