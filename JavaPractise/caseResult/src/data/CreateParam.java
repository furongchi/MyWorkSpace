package data;
public class CreateParam {
	private String path;
	private String caseName;
	private int caseNumber;
	private String caseResult;
	private String dbtVersion;
	private String deviceID;
	private String macType;

	public CreateParam() {
		// TODO Auto-generated constructor stub
	}

	public void setPath(String nameTmp) {
		// TODO Auto-generated method stub
		this.path=nameTmp;
		//System.out.print(this.path);
		
	}
	public String getPath(){
		return path;
	}

	public void setCaseName(String nameTmp) {
		// TODO Auto-generated method stub
		this.caseName=nameTmp;
		//System.out.print(this.caseName);
	}
	public String getcaseName(){
		return caseName;
	}

	public void setCaseNumber(String nameTmp) {
		// TODO Auto-generated method stub
		this.caseNumber=Integer.valueOf(nameTmp);
		//System.out.print(this.caseNumber);
	}
	public int getcaseNumber(){
		return caseNumber;
	}

	public void setcaseResult(String nameTmp) {
		// TODO Auto-generated method stub
		this.caseResult=nameTmp;
		//System.out.print(this.caseResult);
	}
	public String getcaseResult(){
		return caseResult;
	}

	public void setdbtVersion(String nameTmp) {
		// TODO Auto-generated method stub
		this.dbtVersion=nameTmp;
		//System.out.print(this.dbtVersion);
	}
	public String getdbtVersion(){
		return dbtVersion;
	}

	public void setdeviceID(String nameTmp) {
		// TODO Auto-generated method stub
		this.deviceID=nameTmp;
		//System.out.print(this.deviceID);
	}
	public String getDeviceID(){
		return deviceID;
	}

	public void setmacType(String nameTmp) {
		// TODO Auto-generated method stub
		this.macType=nameTmp;
		//System.out.print(this.macType);
	}
	public String getMacType(){
		return macType;
	}



}
