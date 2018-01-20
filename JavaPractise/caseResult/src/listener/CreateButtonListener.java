package listener;

import java.awt.event.ActionEvent;
import javax.xml.parsers.ParserConfigurationException;

import data.CreateParam;
import function.CreateResultXML;

public class CreateButtonListener implements java.awt.event.ActionListener {
	private CreateParam createParam;

	public CreateButtonListener(CreateParam createParam) {
		// TODO Auto-generated constructor stub
		this.createParam=createParam;
	}


	@Override
	public void actionPerformed(ActionEvent paramActionEvent) {
		// TODO Auto-generated method stub
		CreateResultXML task= new CreateResultXML();
		System.out.print("time");
		System.out.print(System.currentTimeMillis() + "");
		String temp = String.valueOf(System.currentTimeMillis());
		try {
			task.createXml(createParam);
		} catch (ParserConfigurationException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		}

	}
