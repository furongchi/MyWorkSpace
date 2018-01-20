package listener;

import java.awt.event.FocusEvent;
import java.awt.event.FocusListener;
import javax.swing.JTextField;

import data.CreateParam;


public class DeviceIDTextListener
  implements FocusListener
{
  private JTextField deviceID;
  private CreateParam createParam;
 
  
  public DeviceIDTextListener(JTextField deviceIDText, CreateParam createParam) {
	  deviceID = deviceIDText;
	  this.createParam = createParam;
  }
  

public void focusGained(FocusEvent e) {}

  public void focusLost(FocusEvent e)
  {
	  String nameTmp = deviceID.getText();
	  //System.out.print(nameTmp);
	  createParam.setdeviceID(nameTmp);
  }
}