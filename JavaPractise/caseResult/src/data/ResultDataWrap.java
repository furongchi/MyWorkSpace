package data;

public class ResultDataWrap {

	public static ResultData wrapTestCase(Integer webId,CreateParam createParam) {
		ResultData resultData = new ResultData();
		resultData.setStartTime();
		try {
			Thread.sleep(30);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		resultData.setCaseName(webId+"_"+createParam.getcaseName()+"_"+webId);
		resultData.setdeviceID(createParam.getDeviceID());
		resultData.setcaseResult(createParam.getcaseResult());
		resultData.setEndTime();
		resultData.setExecuteTime();
		return resultData;
	}

}
