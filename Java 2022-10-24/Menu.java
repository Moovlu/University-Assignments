// Import required modules
import java.util.Scanner;

public class Menu {

    // Test if string input is numerical
    private static boolean testIfNumerical(String input) {
        try {
            Integer.parseInt(input);
            return true;
        } catch(NumberFormatException e) {
            return false;
        }
    }

    // Show menu (no objects need to be created so static is used)
    public static void showMenu() {

        Scanner scnr = new Scanner(System.in); // Create new scanner object
        System.out.println("\n######################################################################\n");

        // Get user input on loop
        boolean quit = false;
        try {
            // Create new timetable object and strings to save inputs
            WeeklyTimeTable week2 = new WeeklyTimeTable(2);
            String dayInput;
            String timeInput;

            // Selectable movies
            Movie[] movieList = new Movie[6];
            movieList[1] = new Movie("Snowpiercer", 126, "MA", 400);
            movieList[2] = new Movie("Top Gun: Maverick", 130, "M", 600);
            movieList[3] = new Movie("Monsters, Inc.", 92, "G", 90);
            movieList[4] = new Movie("Coraline", 100, "PG", 40);
            movieList[5] = new Movie("Goodbye", 140, "PG", 60);

            do {
                System.out.println("""
                1.Show the timetable of the week
                2.Show available tickets of the week
                3.Show sales report of the week
                4.Add a session by day and time
                5.Sale tickets by day and time
                6.Quit""");
                String mainInput = scnr.nextLine();
                // Runs code through switch based on user input
                switch(mainInput) {
                    case "1":
                        // Show session
                        week2.showSessions();
                        System.out.println();
                        break;

                    case "2":
                        // Show available tickets for the week
                        week2.showTickets();
                        System.out.println();
                        break;

                    case "3":
                        // Show sales report for the week
                        week2.showSales();
                        System.out.println();
                        break;

                    case "4":
                    // Add a session by day and time
                        // Define input saving variables
                        String sessionTypeInput;
                        String movieInput;
                        week2.showSessions();

                        System.out.println("Which day would you like to place the new session?");
                        // While day input is invalid keep asking for input
                        do {
                            dayInput = scnr.nextLine();
                        } while (!testIfNumerical(dayInput));
                        System.out.println("Which time would you like to place the new session?");
                        // While time input is invalid keep asking for input
                        do {
                            timeInput = scnr.nextLine();
                        } while (!testIfNumerical(timeInput));
                        System.out.println("What type of session would you like to make?\n1 - Normal\n2 - Kids\n3 - Sparse");
                        // While session type input is invalid keep asking for input
                        do {
                            sessionTypeInput = scnr.nextLine();
                        } while (!(testIfNumerical(sessionTypeInput)&&(Integer.parseInt(sessionTypeInput)>0)&&(Integer.parseInt(sessionTypeInput)<4)));
                        System.out.println("""
                            Which movie would you like to add to the new session?
                            1.Snowpiercer           126min  MA  $400
                            2.Top Gun: Maverick     130min  M   $600
                            3.Monsters Inc.         92min   G   $90
                            4.Coraline              100min  PG  $40
                            5.Goodbye               140min  PG  $60
                            """);
                        // While movies input is invalid keep asking for input
                        do {
                            movieInput = scnr.nextLine();
                        } while (!testIfNumerical(timeInput));

                        // Write movie to session and session to timetable
                        if (sessionTypeInput.equals("1")) {
                            // Create a regular session
                            Session tempSession = new Session(movieList[Integer.parseInt(movieInput)]);
                            week2.addSession(tempSession, Integer.parseInt(dayInput), Integer.parseInt(timeInput));
                        } else if (sessionTypeInput.equals("2")) {
                            // Create a sparse session
                            KidsSession tempSession = new KidsSession(movieList[Integer.parseInt(movieInput)]);
                            week2.addSession(tempSession, Integer.parseInt(dayInput), Integer.parseInt(timeInput));
                        } else if (sessionTypeInput.equals("3")) {
                            // Create a kids session
                            SparseSession tempSession = new SparseSession(movieList[Integer.parseInt(movieInput)]);
                            week2.addSession(tempSession, Integer.parseInt(dayInput), Integer.parseInt(timeInput));
                        }
                        break;


                    case "5":
                        String ticketInput;
                        // Sale tickets by day and time
                        week2.showSessions();

                        System.out.println("Which day would you like to buy from?");
                        // While day input is invalid keep asking for input
                        do {
                            dayInput = scnr.nextLine();
                        } while (!testIfNumerical(dayInput));
                        System.out.println("Which time would you like to buy from?");
                        // While time input is invalid keep asking for input
                        do {
                            timeInput = scnr.nextLine();
                        } while (!testIfNumerical(timeInput));

                        Session currentSession = week2.getSession(Integer.parseInt(dayInput), Integer.parseInt(timeInput));
                        if (currentSession == null) {
                            // Movie wasn't found
                            System.out.println("There is no session here!");
                        } else {
                            // Prompt user for how many tickets
                            System.out.println("Selected "+currentSession.getSessionTitle()+". How many tickets would you like to buy?");
                            do {
                                ticketInput = scnr.nextLine();
                            } while (!testIfNumerical(ticketInput));
                            currentSession.sellTickets(Integer.parseInt(ticketInput));
                        }

                        break;

                    case "6":
                        // Quit program
                        quit = true;
                        break;

                    default:
                        // Invalid input
                        System.out.println("Invalid input, please try again...");
                }
            } while (!quit);
            // Closes program
            System.exit(0 );

        } catch(Exception e) {
            System.err.println(e.getMessage());
        }
    }
}
