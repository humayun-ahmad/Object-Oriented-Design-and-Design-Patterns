public class CashierLogger extends AbstractLogger{
	public CashierLogger(int level){
		this.level = level;
	}

	protected void write(String message){
		System.out.println("CashierLogger : " + message);
	}
}