import java.util.Scanner;
 
class Username_Exception extends Exception {
	public Username_Exception(String string) {
		super(string);
	}
}

class Password_Exception extends Exception {
	public Password_Exception(String string) {
		super(string);
	}
}

public class UserAuthentication{
	public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String username, password;
  
  System.out.print("Enter username:");
  username = sc.nextLine();
  
  System.out.print("Enter password:");
  password = sc.nextLine();
  
  int length = username.length();
 
  try {
	 if(length>8)
		 throw new Username_Exception("username must be atmost 8 characters!");
	 if(!password.equals("java"))
    	 throw new Password_Exception("Incorrect password\nEnter the correct password??");
     else
    	 System.out.println("**Successfully login**");
      }
  catch (Username_Exception U) {
	  U.printStackTrace();
  }
  catch (Password_Exception P) {
      P.printStackTrace();
  }
  
  }
}
