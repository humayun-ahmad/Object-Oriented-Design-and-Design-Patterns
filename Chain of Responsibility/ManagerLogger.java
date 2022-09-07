public class ManagerLogger extends AbstractLogger{
	public ManagerLogger(){
		this.level = level;
	}

	protected void write(String message){
		System.out.println("Manager : " + message);
	}
}