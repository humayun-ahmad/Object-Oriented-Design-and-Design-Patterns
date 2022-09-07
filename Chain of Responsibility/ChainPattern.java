public class ChainPattern{
	private static AbstractLogger getChainOfLoggers(){
		AbstractLogger cashierLogger = new CashierLogger(AbstractLogger.cashier);
		AbstractLogger seniorLogger = new SeniorOfficerLogger(AbstractLogger.seniorOfficer);
		AbstractLogger managerLogger = new ManagerLogger(AbstractLogger.manager);
	

		cashierLogger.setNextLogger(seniorLogger);
		seniorLogger.setNextLogger(managerLogger);


		return cashierLogger;
	}


	public static void main(String[] args){
		AbstractLogger loggerChain = getChainOfLoggers();
		loggerChain.logMessage(AbstractLogger.cashier, "cashier.");
		loggerChain.logMessage(AbstractLogger.seniorOfficer, "senior officer");
		loggerChain.logMessage(AbstractLogger.manager, "manager");
	}	


}