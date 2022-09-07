public class CashierLogger extends AbstractLogger{
	public CashierLogger(){
		this.level = level;
	}

	protected void write(String message){
		System.out.println("CashierLogger : " + message);
	}
}