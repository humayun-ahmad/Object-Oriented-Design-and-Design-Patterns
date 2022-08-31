public class EmailNotification implements Notification {
 
    @Override
    public void notifyUser()
    {
    
        System.out.println("It's calling from EmailNotification! & it's sending an e-mail notification");
    }
}