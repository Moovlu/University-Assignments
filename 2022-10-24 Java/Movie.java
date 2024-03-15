class Movie{
    // Initialise variables
    private String title;
    private int duration;
    private String rating;
    private int fee;

    // Constructor
    public Movie(String title, int duration, String rating, int fee) throws InvalidMovieException {
        // Assign instance variables
        this.title = title;
        this.duration = duration;
        this.rating = rating;
        this.fee = fee;

        // Check if inputs are valid, if not throw exception
        if (!rating.equals("M") && !rating.equals("MA") && !rating.equals("G") && !rating.equals("PG"))
            throw new InvalidMovieException("Invalid Rating");
        else if (duration > 220)
            throw new InvalidMovieException("Invalid duration");
        
        // Cut down move name for display
        this.title = this.title.substring(0, 7);
    }

    // Accessors
    public String getTitle() { return this.title; }
    public int getDuration() { return this.duration; }
    public String getRating() { return this.rating; }
    public int getFee() { return this.fee; }
}