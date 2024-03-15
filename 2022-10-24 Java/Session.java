public class Session{
    // Initialise variables
    protected int capacity = 60;
    protected int availableSeats = capacity;
    protected Movie movie;
    protected int price;
    protected int sessionLength;
    
    // Constructors
    public Session(Movie movie, int price) throws InvalidMovieException {
        // Check if movie is valid
        if ((movie == null) || (price < 0) || (price > 100)) {
            throw new InvalidMovieException("Invalid movie");
        } else {
            // Select movie
            this.movie = movie;
            this.price = price;
        }
    }
    public Session(Movie movie) throws InvalidMovieException {
        if (movie == null) {
            throw new InvalidMovieException("Invalid movie");
        } else {
            this.movie = movie;
            this.price = 15;
        }
    }

    // Accessors
    public int getSessonLength() { return this.movie.getDuration(); }
    public int getAvailableSeats() { return this.availableSeats; }
    public int getMovieFee() { return this.movie.getFee(); }
    public int getTicketsSold() { return this.capacity - this.availableSeats; }

    // Purchasing tickets
    public boolean sellTickets(int num) {
        if ((num < 1) || (num > this.availableSeats))
            return false;
        else {
            this.availableSeats -= num;
            return true;
        }
    }

    public String getSessionTitle() { return this.movie.getTitle(); }
    
    public int profit() {
        return (this.capacity - this.availableSeats)*this.price;
    }
}