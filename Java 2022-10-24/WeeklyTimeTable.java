public class WeeklyTimeTable{
    // Initialise variables
    private int weekNum;
    private boolean[] weeksInUse = new boolean[52];
    private Session[][] movieDayTime = new Session[8][8];
    
    // Constructor
    public WeeklyTimeTable(int weekNum) throws WeekAlreadyExistException {
        // Check if week is already written
        if (weeksInUse[weekNum]) {
            throw new WeekAlreadyExistException(weekNum+" already exists!");
        } else {
            this.weekNum = weekNum;
            weeksInUse[weekNum] = true;
        }
    }
    
    // Convert string day input to int
    private int dayToInt(String day) {
        // Find day
        int numDay = 0;
        if (day.toLowerCase().contains("mon")) {
            numDay = 1;
        } else if (day.toLowerCase().contains("tue")) {
            numDay = 2;
        } else if (day.toLowerCase().contains("wed")) {
            numDay = 3;
        } else if (day.toLowerCase().contains("thu")) {
            numDay = 4;
        } else if (day.toLowerCase().contains("fri")) {
            numDay = 5;
        } else if (day.toLowerCase().contains("sat")) {
            numDay = 6;
        } else if (day.toLowerCase().contains("sun")) {
            numDay = 7;
        }
        return numDay;
    }
    //Convert string time input to int
    private int timeToInt(String time) {
        // Find time
        int numTime = 0;
        if (time.equals("08:00")) {
            numTime = 1;
        } else if (time.equals("10:00")) {
            numTime = 2;
        } else if (time.equals("12:00")) {
            numTime = 3;
        } else if (time.equals("14:00")) {
            numTime = 4;
        } else if (time.equals("16:00")) {
            numTime = 5;
        } else if (time.equals("18:00")) {
            numTime = 6;
        } else if (time.equals("20:00")) {
            numTime = 7;
        }
        return numTime;
    }


    // Check if selected day/time is empty
    public boolean checkAvailability(int day, int time) {
        // Check if array item is null
        if (this.movieDayTime[day][time] == null) {
            return true;
        // Check if its not the first movie of the day and if previous element cuts into selected
        } else if (time > 1 && this.movieDayTime[day][time-1].getSessonLength() > 120) {
            return true;
        } else {
            return false;
        }
    }  
    // Convert to usable format and check if empty
    public boolean checkAvailability(String day, String time) {
        // Create variables for numerical representations of input
        return checkAvailability(dayToInt(day), timeToInt(time));
    }
    
    // Add session to timetable
    public boolean addSession(Session s, int day, int time) throws InvalidDayException, InvalidTimeException {
        // Check if day/time is within bounds
        if ((day > 0) && (day < 8)) {
            if ((time > 0) && (time < 8)) {
                // Check if spot is available
                if (checkAvailability(day, time)) {
                    // Check if it's a kids session it cannot go past 18:00
                    if (s instanceof KidsSession && time > 5) { return false; }
                    // Write to array item
                    this.movieDayTime[day][time] = s;
                    return true;
                } else { return false; }
            } else { throw new InvalidTimeException("Invalid time input");}
        } else { throw new InvalidDayException("Invalid day input"); }
    }
    // Convert to usable format and add to timetable
    public boolean addSession(Session s, String day, String time) throws InvalidDayException, InvalidTimeException {
        return addSession(s, dayToInt(day), timeToInt(time));
    }    


    // Display all sessions
    public void showSessions() {
        System.out.print("""
                      Mon      Tue      Wed      Thu      Fri      Sat      Sun
        -------------------------------------------------------------------------
        """);
        for (int time=1;time<8;time++) { // row
            // Find current time
            switch(time) {
                case 1:
                    System.out.print("08:00     ");
                    break;
                case 2:
                    System.out.print("10:00     ");
                    break;
                case 3:
                    System.out.print("12:00     ");
                    break;
                case 4:
                    System.out.print("14:00     ");
                    break;
                case 5:
                    System.out.print("16:00     ");
                    break;
                case 6:
                    System.out.print("18:00     ");
                    break;
                case 7:
                    System.out.print("20:00     ");
                    break;
            }

            for (int day=1;day<8;day++) { // column
                // Print '---' if no session
                if (movieDayTime[day][time] == null) {
                    System.out.print("    ---  ");
                } else {
                    // Print movie name if session
                    System.out.print("  "+movieDayTime[day][time].getSessionTitle());
                }
            }
            System.out.println(); // Go to next line
        }
    }  
    
    // Display all sessions with available tickets
    public void showTickets() {
        System.out.print("""
                      Mon      Tue      Wed      Thu      Fri      Sat      Sun
        -------------------------------------------------------------------------
        """);
        for (int time=1;time<8;time++) { // row
            // Find current time
            switch(time) {
                case 1:
                    System.out.print("08:00     ");
                    break;
                case 2:
                    System.out.print("10:00     ");
                    break;
                case 3:
                    System.out.print("12:00     ");
                    break;
                case 4:
                    System.out.print("14:00     ");
                    break;
                case 5:
                    System.out.print("16:00     ");
                    break;
                case 6:
                    System.out.print("18:00     ");
                    break;
                case 7:
                    System.out.print("20:00     ");
                    break;
            }

            for (int day=1;day<8;day++) { // column
                // Print '---' if no session
                if (movieDayTime[day][time] == null) {
                    System.out.print("    ---  ");
                } else {
                    // Print movie name if session
                    System.out.print("  "+movieDayTime[day][time].getSessionTitle());
                }
                // When the end of row is reached
                if (day == 7) {
                    System.out.println();
                    System.out.print("            ");
                    // Print all available ticket numbers
                    for (int dayTick=1;dayTick<8;dayTick++) {
                        if (movieDayTime[dayTick][time] == null) {
                            // If no session is found, print blank
                            System.out.print("         ");
                        } else {
                            System.out.print("   "+movieDayTime[dayTick][time].getAvailableSeats()+"    ");
                        }
                    }
                }
            }
            System.out.println(); // Go to next line
        }
    }
    
    // Display all sessions with sales and tickets sold
    public void showSales() {
        // Initialise total profit for final print
        int totalProfit= 0;
        System.out.print("""
                      Mon      Tue      Wed      Thu      Fri      Sat      Sun
        -------------------------------------------------------------------------
        """);
        for (int time=1;time<8;time++) { // row
            // Find current time
            switch(time) {
                case 1:
                    System.out.print("08:00     ");
                    break;
                case 2:
                    System.out.print("10:00     ");
                    break;
                case 3:
                    System.out.print("12:00     ");
                    break;
                case 4:
                    System.out.print("14:00     ");
                    break;
                case 5:
                    System.out.print("16:00     ");
                    break;
                case 6:
                    System.out.print("18:00     ");
                    break;
                case 7:
                    System.out.print("20:00     ");
                    break;
            }

            for (int day=1;day<8;day++) { // column
                // Print '---' if no session
                if (movieDayTime[day][time] == null) {
                    System.out.print("    ---  ");
                } else {
                    // Print movie name if session
                    System.out.print("  "+movieDayTime[day][time].getSessionTitle());
                }

                // When the end of row is reached
                if (day == 7) {
                    System.out.println();
                    System.out.print("            ");
                    // Print all available ticket numbers
                    for (int dayTick=1;dayTick<8;dayTick++) {
                        if (movieDayTime[dayTick][time] == null) {
                            // If no session is found, print blank
                            System.out.print("         ");
                        } else {
                            System.out.print("  x"+movieDayTime[dayTick][time].getTicketsSold()+"    ");
                        }
                    }

                    System.out.println();
                    System.out.print("            ");
                    // Print session profit
                    for (int dayProf=1;dayProf<8;dayProf++) {
                        if (movieDayTime[dayProf][time] == null) {
                            // If no session is found, print blank
                            System.out.print("         ");
                        } else {
                            // Calculate net profit
                            int profit = movieDayTime[dayProf][time].profit() - movieDayTime[dayProf][time].getMovieFee();
                            totalProfit += profit;
                            System.out.print("  $"+profit+"    ");
                        }
                    }

                }
            }
            System.out.println(); // Go to next line
        }
        System.out.println("The total of this week is $"+totalProfit);
    }

    // Accessor for sessions in movieDayTime
    public Session getSession(int day, int time) {
        return this.movieDayTime[day][time];
    }
}