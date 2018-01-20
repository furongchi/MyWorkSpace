package listener;


import java.awt.event.FocusEvent;
import java.awt.event.FocusListener;
import javax.swing.JTextField;

import data.CreateParam;


public class MacTypeListener
  implements FocusListener
{
  private JTextField macType;
  private CreateParam createParam;
 
  
  public MacTypeListener(JTextField macTypeText, CreateParam createParam) {
	  macType = macTypeText;
	  this.createParam = createParam;
  }
  public void focusGained(FocusEvent e) {}

  public void focusLost(FocusEvent e)
  {
	  String nameTmp = macType.getText();
	  //System.out.print(nameTmp);
	  createParam.setmacType(nameTmp);
  }
}