class getproduct{
  int pcode;
  String pname;
  double price;
 }
class product{
  public static void main(String args[]){
    getproduct p1=new getproduct();
    getproduct p2=new getproduct();
    getproduct p3=new getproduct();
    p1.price=3000;
    p1.pcode=101;
    p1.pname="Airpod";
    p2.price=40;
    p2.pcode=102;
    p2.pname="Book";
    p3.price=1000;
    p3.pcode=103;
    p3.pname="Shampoo";
    if(p1.price<p2.price && p1.price<p3.price){
      System.out.println("Product name:"+p1.pname);
      System.out.println("Product code:"+p1.pcode);
      System.out.println("Product Price:"+p1.price);
      }
    else if(p2.price<p1.price && p2.price<p3.price){
      System.out.println("Product name:"+p2.pname);
      System.out.println("Product code:"+p2.pcode);
      System.out.println("Product Price:"+p2.price);
      }
    else{
      System.out.println("Product name:"+p3.pname);
      System.out.println("Product code:"+p3.pcode);
      System.out.println("Product Price:"+p3.price);
      }
      }
      }
      
