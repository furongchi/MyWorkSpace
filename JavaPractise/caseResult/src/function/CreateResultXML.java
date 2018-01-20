package function;

import java.util.ArrayList;
import java.util.List;

import javax.xml.parsers.ParserConfigurationException;

import data.CreateParam;
import data.ResultData;
import data.ResultDataWrap;
import util.ExportToXMLUtil;

public class CreateResultXML {

	public void createXml(CreateParam createParam) throws ParserConfigurationException {
		// TODO Auto-generated method stub
		createFakeResultXML(createParam);
	}

	private void createFakeResultXML(CreateParam createParam) throws ParserConfigurationException {
		// TODO Auto-generated method stub
		List<ResultData> resultDataList = new ArrayList<ResultData>();
        for (int index = 0; index < createParam.getcaseNumber(); index++) {
            resultDataList.add(ResultDataWrap.wrapTestCase(index, createParam));
        }
        
        ExportToXMLUtil.createFakeResult(resultDataList,createParam);
	}
	

}
