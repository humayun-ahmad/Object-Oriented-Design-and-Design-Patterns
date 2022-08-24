public class SingletonPatternDemo{
	public static void main(String[] args){
		// get the only object avaiable
		SingleObject object = SingleObject.getInstance();
		
		object.showMessage();
		
		callAgain();
		
	}
	
	public static void callAgain(){
		// Here I'm going to create a new object 
		// If new object is created then it will print hi
		// That's mean I will see two time hi message
		// I don't see two time hi message then second time 
		// object has not been created
		
		SingleObject object = SingleObject.getInstance();
		
		object.showMessage();
	}
	
	
}