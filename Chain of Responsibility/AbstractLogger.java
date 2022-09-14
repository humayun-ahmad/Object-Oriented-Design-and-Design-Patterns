public abstract class AbstractLogger{
	public static int cashier = 1;
	public static int seniorOfficer = 2;
	public static int manager = 3;

	protected int level;

	protected AbstractLogger nextLogger;

	public void setNextLogger(AbstractLogger nextLogger){
		/*this.levelLogger = nextLogger;*/
		this.nextLogger = nextLogger;
	}

	public void logMessage(int level, String message){
		if(this.level <= level){
			write(message);
		}
		if(nextLogger != null){
			nextLogger.logMessage(level, message);
		}
	}

	abstract protected void write(String message);

}


