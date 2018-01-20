package listener;

import java.awt.event.FocusEvent;
import java.awt.event.FocusListener;
import javax.swing.JTextField;

import data.CreateParam;


public class PathTextListener
  implements FocusListener
{
  private JTextField path;
  private CreateParam createParam;
 
  
  public PathTextListener(JTextField pathText, CreateParam createParam) {
	  path = pathText;
	  this.createParam = createParam;
  }
  
  public void focusGained(FocusEvent e) {}

  public void focusLost(FocusEvent e)
  {
	  String nameTmp = path.getText();
	  //System.out.print(nameTmp);
	  createParam.setPath(nameTmp);
  }
}
