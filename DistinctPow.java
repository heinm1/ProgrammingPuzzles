
// calculate the distinc number of powers in a 2-100, 2-100 matrix

//spent 2 days trying to careat a formula
//just brute forced in the end;

import java.util.ArrayList;
import java.util.HashSet;
import java.math.BigInteger;

public class DistinctPow {

  public static void main(String[] args) {

    System.out.println(solution(100));

  }

  public static int solution(int w){
    ArrayList l = new ArrayList<>();

    //generates 9801 powers
    for(int a = 2; a <= w; ++a){
      for(int b = 2; b <= w; ++b){
        l.add(pow(a,b));
      }
    }
/*
    for(int a = 0; a < l.size(); ++a){
      System.out.println(l.get(a));
    }
*/

    //set filters out duplicets
    HashSet<String> hs = new HashSet<>();
    hs.addAll(l);

    //length of the set is the number of distinct powers
    return hs.size();
  }

  //helper method to calculate large powers
  public static BigInteger pow(int a, int b){
    BigInteger temp = new BigInteger(""+a);
    for(int i = 0; i < b-1; ++i){
      temp = temp.multiply(new BigInteger(a+""));
    }
    return temp;
  }

}
