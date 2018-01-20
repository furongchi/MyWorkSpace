package data;
import java.util.Date; 


import java.text.SimpleDateFormat; 

public class ResultData {
	private String caseName;
	private String caseResult;
	private String deviceID;
	private String startTime;
	private String executeTime;
	private Date startNow;
	private Date endNow;
	private String endTime;


	public ResultData() {
		// TODO Auto-generated constructor stub
	}
	
	
	public void setCaseName(String nameTmp) {
		// TODO Auto-generated method stub
		this.caseName=nameTmp;
		//System.out.print(this.caseName);
	}
	public String getcaseName(){
		return caseName;
	}


	public void setcaseResult(String nameTmp) {
		// TODO Auto-generated method stub
		this.caseResult=nameTmp;
		//System.out.print(this.caseResult);
	}
	public String getcaseResult(){
		
		return caseResult;
	}
	public void setStartTime() {
		// TODO Auto-generated method stub
		this.startNow = new Date(); 
		SimpleDateFormat startTimeFormat = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
		this.startTime=startTimeFormat.format( startNow ); 
		//System.out.print(this.startTime);
	}
	public String getStartTime(){
		return startTime;
	}
	public void setExecuteTime() {
		// TODO Auto-generated method stub
		this.endNow = new Date(); 
		long eTime=this.endNow.getTime()-this.startNow.getTime();
		this.executeTime=0+"'"+0+"\""+eTime;
		//System.out.print(this.executeTime);
	}
	public String getExecuteTime(){
		return executeTime;
	}

	public void setdeviceID(String deviceID) {
		// TODO Auto-generated method stub
		this.deviceID=deviceID;
		//System.out.print(this.deviceID);
	}
	public String getdeviceID(){
		return deviceID;
	}
	public void setEndTime() {
		// TODO Auto-generated method stub
		Date now = new Date();
		SimpleDateFormat endTimeFormat = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
		this.endTime=endTimeFormat.format(now);
		//System.out.print(this.endTime);
	}

	public String getEndTime() {
		// TODO Auto-generated method stub
		
		return endTime;
	}
}
