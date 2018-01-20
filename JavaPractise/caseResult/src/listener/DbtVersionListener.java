package listener;
import java.awt.event.FocusEvent;
import java.awt.event.FocusListener;
import javax.swing.JTextField;

import data.CreateParam;


public class DbtVersionListener
  implements FocusListener
{
  private JTextField dbtVersion;
  private CreateParam createParam;
 
  
  public DbtVersionListener(JTextField dbtVersionText, CreateParam createParam) {
	  dbtVersion = dbtVersionText;
	  this.createParam = createParam;
  }
  public void focusGained(FocusEvent e) {}

  public void focusLost(FocusEvent e)
  {
	  String nameTmp = dbtVersion.getText();
	  //System.out.print(nameTmp);
	  createParam.setdbtVersion(nameTmp);
  }
}