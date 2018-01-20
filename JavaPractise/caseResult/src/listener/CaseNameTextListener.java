package listener;

import java.awt.event.FocusEvent;
import java.awt.event.FocusListener;
import javax.swing.JTextField;

import data.CreateParam;


public class CaseNameTextListener
  implements FocusListener
{
  private JTextField caseName;
  private CreateParam createParam;
 
  
  public CaseNameTextListener(JTextField caseNameText, CreateParam createParam) {
	  caseName = caseNameText;
	  this.createParam = createParam;
  }
  
  public void focusGained(FocusEvent e) {}

  public void focusLost(FocusEvent e)
  {
	  String nameTmp = caseName.getText();
	  //System.out.print(nameTmp);
	  createParam.setCaseName(nameTmp);
  }
}
