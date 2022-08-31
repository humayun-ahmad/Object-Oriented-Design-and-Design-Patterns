public class SMSNotification implements Notification {
 
    @Override
    public void notifyUser()
    {
        
        System.out.println("It's calling from SMSNotification! & it's sending an SMS notification!");
    }
}