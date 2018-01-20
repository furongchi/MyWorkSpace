package util;

import java.io.File;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.List;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.transform.OutputKeys;
import javax.xml.transform.Transformer;
import javax.xml.transform.TransformerFactory;
import javax.xml.transform.dom.DOMSource;
import javax.xml.transform.stream.StreamResult;
import org.w3c.dom.Document;
import org.w3c.dom.Element;

import data.CreateParam;
import data.ResultData;

public class ExportToXMLUtil {
	public static void createFakeResult(List<ResultData> resultDataList,CreateParam createParam) throws ParserConfigurationException {
		DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
		
		try {
			DocumentBuilder builder = factory.newDocumentBuilder();
			Document testResult = builder.newDocument();
			Element resultStore = testResult.createElement("Cases");
			for (ResultData resultData : resultDataList){
				Element caseresult = testResult.createElement("Case");
				caseresult.setAttribute("name", resultData.getcaseName());
				
				Element deviceID = testResult.createElement("deviceId");
	            deviceID.setTextContent(resultData.getdeviceID());
	            caseresult.appendChild(deviceID);
	            
	            Element result = testResult.createElement("result");
	            result.setTextContent(resultData.getcaseResult());
	            caseresult.appendChild(result);
	            
	            Element endTime = testResult.createElement("endTime");
	            endTime.setTextContent(resultData.getEndTime());
	            caseresult.appendChild(endTime);
	            
	            Element executeTime = testResult.createElement("time");
	            executeTime.setTextContent(resultData.getExecuteTime());
	            caseresult.appendChild(executeTime);
	            
	            resultStore.appendChild(caseresult);	
				}
			resultStore.setAttribute("xmlns","");
			resultStore.setAttribute("macType",createParam.getMacType());
			resultStore.setAttribute("dbtVersion",createParam.getdbtVersion());
			ResultData firstElement=resultDataList.get(0);
			SimpleDateFormat simpleDateFormat =new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
			Date startTime=simpleDateFormat.parse(firstElement.getStartTime());
			resultStore.setAttribute("startTime",startTime.getTime()+"");
			ResultData lastElement=resultDataList.get(resultDataList.size()-1);
			Date endTime=simpleDateFormat.parse(lastElement.getEndTime());
			resultStore.setAttribute("endTime",endTime.getTime()+"");
			testResult.appendChild(resultStore);
			TransformerFactory tff = TransformerFactory.newInstance();
			Transformer tf = tff.newTransformer();
			tf.setOutputProperty(OutputKeys.INDENT, "yes");
			File myFile = new File(createParam.getPath(),"result.xml");
			if (!myFile.exists())
				myFile.createNewFile();
			tf.transform(new DOMSource(testResult), new StreamResult(myFile));
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		// TODO Auto-generated method stub
		
	}
	
	
}

	

