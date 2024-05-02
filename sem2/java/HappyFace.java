import java.awt.*;
import java.awt.event.*;
import java.applet.*;
public class HappyFace extends Applet implements ActionListener{
    TextField text1,text2,text3,text4,text5;
    Button btn;
    int average = 0;
    public void init(){
        Label label1 = new Label("Subject 1 : ");
        Label label2 = new Label("Subject 2 : ");
        Label label3 = new Label("Subject 3 : ");
        Label label4 = new Label("Subject 4 : ");
        Label label5 = new Label("Subject 5 : ");
        text1 = new TextField(10);
        text2 = new TextField(10);
        text3 = new TextField(10);
        text4 = new TextField(10);
        text5 = new TextField(10);
        btn = new Button("Find");
        add(label1);
        add(text1);
        add(label2);
        add(text2);
        add(label3);
        add(text3);
        add(label4);
        add(text4);
        add(label5);
        add(text5);
        add(btn);
        btn.addActionListener(this);
    }
    public void actionPerformed(ActionEvent e){
        int sub1 = Integer.parseInt(text1.getText());
        int sub2 = Integer.parseInt(text2.getText());
        int sub3 = Integer.parseInt(text3.getText());
        int sub4 = Integer.parseInt(text4.getText());
        int sub5 = Integer.parseInt(text5.getText());
        average = (sub1+sub2+sub3+sub4+sub5)*100/500;
        repaint();
    }
    public void paint(Graphics g){
        g.drawString("Average Mark is : "+average+"%",20,100);
        if(average <= 0){
            g.drawString("", 20, 100);
        }else if(average < 50){
            g.drawOval(100, 200, 150, 150);
            g.fillOval(140, 250, 10, 10);
            g.fillOval(200, 250, 10, 10);
            g.drawArc(140, 290, 70, 50, 0, 180);
        }else{
            g.drawOval(100, 200, 150, 150);
            g.fillOval(140, 250, 10, 10);
            g.fillOval(200, 250, 10, 10);
            g.drawArc(140, 270, 70, 50, 180, 180);
        }
    }
}
