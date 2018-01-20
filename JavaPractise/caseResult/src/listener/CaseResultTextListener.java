package listener;


import java.awt.event.FocusEvent;
import java.awt.event.FocusListener;
import javax.swing.JTextField;

import data.CreateParam;


public class CaseResultTextListener
  implements FocusListener
{
  private JTextField caseResult;
  private CreateParam createParam;
 
  
  public CaseResultTextListener(JTextField caseResultText, CreateParam createParam) {
	  caseResult = caseResultText;
	  this.createParam = createParam;
  }
  public void focusGained(FocusEvent e) {}

  public void focusLost(FocusEvent e)
  {
	  String nameTmp = caseResult.getText();
	  //System.out.print(nameTmp);
	  createParam.setcaseResult(nameTmp);
  }
}