/*
    Stage 1 - An item to purchase
    A basic online shopping cart
*/
public class ItemToPurchase {

    // Create variables
    private String itemName;
    private int itemPrice;
    private int itemQuantity;

    // No-argument constructor
    public ItemToPurchase() {
        this.itemName = "none";
        this.itemPrice = 0;
        this.itemQuantity = 0;
    }

    // Argument constructor
    public ItemToPurchase(String name, int price, int quantity) {
        // Check if all inputs are valid, if true assign to variables, if false throw error
        if (name != null)
            this.itemName = name;
        else
            throw new IllegalArgumentException("Name cannot be null");

        if (price >= 0)
            this.itemPrice = price;
        else
            throw new IllegalArgumentException("Price must be greater than 0");

        if (quantity >= 0)
            this.itemQuantity = quantity;
        else
            throw new IllegalArgumentException("Quantity must be greater than 0");
    }


    // Name mutator
    public void setName(String name) {
        // Check if input is valid
        if (name != null)
            this.itemName = name;
        else
            throw new IllegalArgumentException("Name cannot be null");
    }

    // Price mutator
    public void setPrice(int price) {
        // Check if input is valid
        if (price >= 0)
            this.itemPrice = price;
        else
            throw new IllegalArgumentException("Price must be greater than 0");
    }

    // Quantity Mutator
    public void setQuantity(int quantity) {
        // Check if input is valid
        if (quantity >= 0)
            this.itemQuantity = quantity;
        else
            throw new IllegalArgumentException("Quantity must be greater than 0");
    }

    // Name Accessor
    public String getName() { return this.itemName; }
    // Price Accessor
    public int getPrice() { return this.itemPrice; }
    // Quantity Accessor
    public int getQuantity() { return this.itemQuantity; }

    // Returns total price which is price * quantity
    public int getTotalPrice() {
        return this.itemPrice * this.itemQuantity;
    }

    @Override
    public String toString() {
        return String.format("%s %d @ $%d = $%d", this.itemName, this.itemQuantity, this.itemPrice, this.getTotalPrice());
    }
}
