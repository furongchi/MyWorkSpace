package function;

import java.awt.Dimension;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextField;
import javax.swing.SwingUtilities;

import data.CreateParam;
import listener.CaseNameTextListener;
import listener.CaseNumberTextListener;
import listener.CaseResultTextListener;
import listener.CreateButtonListener;
import listener.DbtVersionListener;
import listener.DeviceIDTextListener;
import listener.MacTypeListener;
import listener.PathTextListener;

public class MainFrame extends JFrame
 {
	 public CreateParam createParam = new CreateParam();
	 public static void main(String[] args) {
	  
     SwingUtilities.invokeLater(new Runnable()
     {
       public void run() {
         MainFrame frame = new MainFrame();
         frame.setDefaultCloseOperation(3);
         frame.setVisible(true);
       }
     });
     }
   
   public MainFrame() {
	 setBounds(0, 0, 1000, 1000);
     JPanel contentPane = new JPanel();
     contentPane.setLayout(null);
     JScrollPane jsp = new JScrollPane(contentPane);
     jsp.setBounds(100, 100, 800, 900);
     contentPane.setPreferredSize(new Dimension(jsp.getWidth() - 50, jsp.getHeight()*2));
     add(jsp);
     contentPane.revalidate(); 
     setVisible(true);
     
 
     int startPointx = 20;
     int startPointy = 5;
     int yDelta = 45;
     int textRelevant = 130;
     int buttonRelevant = 300;
     int labelWidth = 110;
     int labelHight = 30;
     int PanelWith=900;
     int textFieldHight=25;
     int textWith=600;
     int count = 0;
     
     JPanel panel4Path = new JPanel();
     contentPane.add(panel4Path);
     panel4Path.setLayout(null);
     panel4Path.setBounds(startPointx, startPointy + count++ * yDelta, PanelWith,labelHight );
    
     
     JLabel lbPathLabel = new JLabel("Path");
     lbPathLabel.setHorizontalAlignment(2);
     lbPathLabel.setBounds(0, 0, labelWidth, labelHight);
     panel4Path.add(lbPathLabel);
     
     JTextField pathText = new JTextField();
     pathText.setBounds(textRelevant, 5, textWith, textFieldHight);
     pathText.setEditable(true);
     pathText.setText("./");
     pathText.addFocusListener(new PathTextListener(pathText, createParam));
     panel4Path.add(pathText);
     
     
  
    
     JPanel panel4CaseName = new JPanel();
     contentPane.add(panel4CaseName);
     panel4CaseName.setLayout(null);
     panel4CaseName.setBounds(startPointx, startPointy + count++ * yDelta, PanelWith,labelHight );
    
     
     JLabel lbCaseNameLabel = new JLabel("Case Name");
     lbCaseNameLabel.setHorizontalAlignment(2);
     lbCaseNameLabel.setBounds(0, 0, labelWidth, labelHight);
     panel4CaseName.add(lbCaseNameLabel);
     
     JTextField caseNameText = new JTextField();
     caseNameText.setBounds(textRelevant, 5, textWith, textFieldHight);
     caseNameText.setEditable(true);
     caseNameText.setText("testCase");
     caseNameText.addFocusListener(new CaseNameTextListener(caseNameText, createParam));
     panel4CaseName.add(caseNameText);
     
     JPanel panel4CaseNumber = new JPanel();
     contentPane.add(panel4CaseNumber);
     panel4CaseNumber.setLayout(null);
     panel4CaseNumber.setBounds(startPointx, startPointy + count++ * yDelta, PanelWith,labelHight );
     
     JLabel lbCaseNumberLabel = new JLabel("Case Number");
     lbCaseNumberLabel.setHorizontalAlignment(2);
     lbCaseNumberLabel.setBounds(0, 0, labelWidth, labelHight);
     panel4CaseNumber.add(lbCaseNumberLabel);
     
     JTextField caseNumberText = new JTextField();
     caseNumberText.setBounds(textRelevant, 5, textWith, textFieldHight);
     caseNumberText.setEditable(true);
     caseNumberText.setText("100");
     caseNumberText.addFocusListener(new CaseNumberTextListener(caseNumberText, createParam));
     panel4CaseNumber.add(caseNumberText);
     
     JPanel panel4CaseResult = new JPanel();
     contentPane.add(panel4CaseResult);
     panel4CaseResult.setLayout(null);
     panel4CaseResult.setBounds(startPointx, startPointy + count++ * yDelta, PanelWith,labelHight );
     
     JLabel lbCaseResultLabel = new JLabel("Case Result");
     lbCaseResultLabel.setHorizontalAlignment(2);
     lbCaseResultLabel.setBounds(0, 0, labelWidth, labelHight);
     panel4CaseResult.add(lbCaseResultLabel);
     
     JTextField CaseResultText = new JTextField();
     CaseResultText.setBounds(textRelevant, 5, textWith, textFieldHight);
     CaseResultText.setEditable(true);
     CaseResultText.setText("Success");
     CaseResultText.addFocusListener(new CaseResultTextListener(CaseResultText,createParam));
     panel4CaseResult.add(CaseResultText);
     
     JPanel panel4DeviceID = new JPanel();
     contentPane.add(panel4DeviceID);
     panel4DeviceID.setLayout(null);
     panel4DeviceID.setBounds(startPointx, startPointy + count++ * yDelta, PanelWith,labelHight );
    
     
     JLabel lbDeviceIDLabel = new JLabel("DeviceID");
     lbDeviceIDLabel.setHorizontalAlignment(2);
     lbDeviceIDLabel.setBounds(0, 0, labelWidth, labelHight);
     panel4DeviceID.add(lbDeviceIDLabel);
     
     JTextField DeviceIDText = new JTextField();
     DeviceIDText.setBounds(textRelevant, 5, textWith, textFieldHight);
     DeviceIDText.setEditable(true);
     DeviceIDText.setText("4d00bc0e98215073");
     DeviceIDText.addFocusListener(new DeviceIDTextListener(DeviceIDText,createParam));
     panel4DeviceID.add(DeviceIDText);
     
     JPanel panel4dbtVersion = new JPanel();
     contentPane.add(panel4dbtVersion);
     panel4dbtVersion.setLayout(null);
     panel4dbtVersion.setBounds(startPointx, startPointy + count++ * yDelta, PanelWith,labelHight );
    
     
     JLabel lbdbtVersionLabel = new JLabel("DBT version");
     lbdbtVersionLabel.setHorizontalAlignment(2);
     lbdbtVersionLabel.setBounds(0, 0, labelWidth, labelHight);
     panel4dbtVersion.add(lbdbtVersionLabel);
     
     JTextField dbtVersionText = new JTextField();
     dbtVersionText.setBounds(textRelevant, 5, textWith, textFieldHight);
     dbtVersionText.setEditable(true);
     dbtVersionText.setText("6");
     dbtVersionText.addFocusListener(new DbtVersionListener(dbtVersionText,createParam));
     panel4dbtVersion.add(dbtVersionText);
     
     JPanel panel4macType = new JPanel();
     contentPane.add(panel4macType);
     panel4macType.setLayout(null);
     panel4macType.setBounds(startPointx, startPointy + count++ * yDelta, PanelWith,labelHight );
    
     
     JLabel lbmacTypeLabel = new JLabel("mac Type");
     lbmacTypeLabel.setHorizontalAlignment(2);
     lbmacTypeLabel.setBounds(0, 0, labelWidth, labelHight);
     panel4macType.add(lbmacTypeLabel);
     
     JTextField macTypeText = new JTextField();
     macTypeText.setBounds(textRelevant, 5, textWith, textFieldHight);
     macTypeText.setEditable(true);
     macTypeText.setText("f8-b1-56-a4-b0-b2");
     macTypeText.addFocusListener(new MacTypeListener(macTypeText,createParam));
     panel4macType.add(macTypeText);
     
     
     JPanel panel4PCfgButton = new JPanel();
     contentPane.add(panel4PCfgButton);
     panel4PCfgButton.setLayout(null);
     panel4PCfgButton.setBounds(startPointx, startPointy + count++ * yDelta, PanelWith,labelHight);
          
     JButton configButton = new JButton("Create");
     configButton.addActionListener(new CreateButtonListener(createParam));
          
     configButton.setBounds(buttonRelevant, 0, 100, 30);
     panel4PCfgButton.add(configButton);

   }
 }
