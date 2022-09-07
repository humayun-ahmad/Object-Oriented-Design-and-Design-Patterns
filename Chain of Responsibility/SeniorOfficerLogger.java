public class SeniorOfficerLogger extends AbstractLogger{
	public SeniorOfficerLogger(int level){
		this.level = level;
	}

	protected void write(String message){
		System.out.println("SeniorOfficer : " + message);
	}
}