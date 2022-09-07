public class SingleObject{
	private static SingleObject instance = new SingleObject();
	
	private SingleObject(){
		
		System.out.println("Hi");
	}
	
	// only object that is available for getting
	public static SingleObject getInstance(){
		return instance;
	}
	
	public void showMessage(){
		System.out.println("Hello World");
	}
	
	
	
}