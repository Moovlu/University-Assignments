public class KidsSession extends Session {
    // Constructors
    public KidsSession(Movie movie, int price) throws InvalidMovieException {
        super(movie, price);
        // Check if selected movie is not rated M or MA
        if (movie.getRating().equals("M") || movie.getRating().equals("MA"))
            throw new InvalidMovieException("Selected movie inappropriate");
    }
    public KidsSession(Movie movie) throws InvalidMovieException {
        super(movie);
        // Check if selected movie is not rated M or MA
        if (movie.getRating().equals("M") || movie.getRating().equals("MA"))
            throw new InvalidMovieException("Selected movie inappropriate");
    }

    @Override
    public int profit() {
        double num = (this.capacity - this.availableSeats)*this.price*0.6;
        return (int) num;
    }
}