
import java.io.*;


public class FileReadWrite {
	public static void main(String[] args) {
		try {
		File f = new File("D:\\MCA 2020\\SEM-II\\OOP_Lab\\CO6\\newfile.txt");
		FileWriter fw = new FileWriter(f);
		fw.write("HELLOO! THIS IS OBJECT ORIENTED PROGRAMMING LAB!!!!!");
		System.out.println("Data written into the file. .!\n");
		fw.close();
		
		BufferedReader br = new BufferedReader(new FileReader(f));
		String s;
		System.out.println("Data read from the file. .! Displayed below:\n");
		while((s = br.readLine()) != null) {
			System.out.println(s);
		 }
		br.close();
	 }
   
		catch(IOException e) {
			System.out.println("An error occurred. . ."+e);
		}
  }
}
