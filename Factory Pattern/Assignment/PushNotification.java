public class PushNotification implements Notification {
 
    @Override
    public void notifyUser(String msg)
    {
        System.out.println("It's calling from PushNotification! & it's sending a push notification");
        System.out.println(msg);
    }
}