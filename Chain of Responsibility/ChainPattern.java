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
		loggerChain.logMessage(AbstractLogger.cashier, 5000 );
		loggerChain.logMessage(AbstractLogger.seniorOfficer, 70000);
		loggerChain.logMessage(AbstractLogger.manager, 100000);
	}	


}