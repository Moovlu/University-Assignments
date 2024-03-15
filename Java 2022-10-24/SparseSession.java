public class SparseSession extends Session {
    
    // Constructors
    public SparseSession(Movie movie, int price) throws InvalidMovieException {
        super(movie, price);
        this.capacity = 20;
        this.availableSeats = 20;
    }

    public SparseSession(Movie movie) throws InvalidMovieException {
        super(movie);
        this.capacity = 20;
        this.availableSeats = 20;
    }

    // Overidden accessor
    @Override
    public int getAvailableSeats() { return this.availableSeats; }

    // Overidden profit
    @Override
    public int profit() {
        // Adding on the extra 1000 to profit
        double num = (this.capacity - this.availableSeats)*this.price*0.6+1000;
        return (int) num;
    }
}