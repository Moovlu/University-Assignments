/*  Put Your Student ID, Name here 
    s3947523, William Dash
   You can make each class public and place them into individual .java files
*/

import java.util.*;

public class A3_P1_2022{ 
    public static void main(String[] args){

        try{
            Movie[] movieList = new Movie[5];
            
            movieList[0] = new Movie("Snowpiercer", 126, "MA", 400);
            movieList[1] = new Movie("Top Gun: Maverick", 130, "M", 600);
            movieList[2] = new Movie("Monsters, Inc.", 92, "G", 90);
            movieList[3] = new Movie("Coraline", 100, "PG", 40);
            movieList[4] = new Movie("Goodbye", 140, "PG", 60);
            
            WeeklyTimeTable week1 = new WeeklyTimeTable(1);
            // WeeklyTimeTable week2 = new WeeklyTimeTable(1);  // Exception!

            System.out.println(week1.checkAvailability(1,1));
            //System.out.println(week1.checkAvailability(1,9));  // Exception!

            System.out.println(week1.checkAvailability("Monday", "14:00"));
            // System.out.println(week1.checkAvailability("Monday", "8:00")); //Exception!

            Session s1 = new Session(movieList[0], 18);
            week1.addSession(s1, 2, 2);
            
            //Session s2 = new KidsSession(movieList[0]);  // Exception!
            Session s2 = new KidsSession(movieList[2]); 
            
            week1.addSession(s2, 4, 6);  // not successful!
            week1.addSession(s2, 4, 5);
            week1.showSessions();
            
            s1.sellTickets(90);          // not successful!
            s1.sellTickets(30);
            s2.sellTickets(25);
            
            week1.showSales();
        }
        catch(Exception e){
            System.err.println(e.getMessage());
        }

        // Display menu
        Menu.showMenu();
    }
}

class WeekAlreadyExistException extends Exception {
    public WeekAlreadyExistException(String message) {
        super(message);
    }
}
class InvalidDayException extends Exception {
    public InvalidDayException(String message) {
        super(message);
    }
}
class InvalidTimeException extends Exception {
    public InvalidTimeException(String message) {
        super(message);
    }
}
class InvalidMovieException extends Exception {
    public InvalidMovieException(String message) {
        super(message);
    }
}