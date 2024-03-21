public class sort_str {
	public static void main(String []args){
        String temp;
        int i,j;
        String str[] = {"apple","orange","pineapple","kiwi","rambootan"};
         System.out.println("The strings before sorting:");
        for(i=0;i<str.length;i++)
         {
             System.out.println(str[i]);
         }
        
        for (i=0; i<str.length; i++)
          {
              for(j=i+1;j<str.length;j++)
                {
                    if((str[i].compareTo(str[j]))>0)
                      {
                          temp=str[i];
                          str[i]=str[j];
                          str[j]=temp;
                      }
                }
              
          }
        System.out.println("\nThe strings after sorting:");
        for(i=0;i<str.length;i++)
         {
             System.out.println(str[i]);
         }
	}
}
