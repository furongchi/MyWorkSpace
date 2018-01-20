package listener;


import java.awt.event.FocusEvent;
import java.awt.event.FocusListener;
import javax.swing.JTextField;

import data.CreateParam;


public class CaseNumberTextListener
  implements FocusListener
{
  private JTextField caseNumber;
  private CreateParam createParam;
 
  
  public CaseNumberTextListener(JTextField caseNumberText, CreateParam createParam) {
	  caseNumber = caseNumberText;
	  this.createParam = createParam;
  }
  

public void focusGained(FocusEvent e) {}

  public void focusLost(FocusEvent e)
  {
	  String nameTmp = caseNumber.getText();
	  //System.out.print(nameTmp);
	  createParam.setCaseNumber(nameTmp);
  }
}