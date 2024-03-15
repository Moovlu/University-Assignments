// Import required Java modules
import java.util.Scanner;

/*
    Stage 2 - A basic shopping cart
    Another basic shopping cart
*/
public class ShoppingCart {

    // Create variables
    protected String customerName;
    protected String currentDate;
    protected ItemToPurchase[] cartItems;
    protected static final int CAPACITY = 10;
    protected int itemCount;

    // No-argument constructor
    public ShoppingCart() {
        this.customerName = "Unknown";
        this.currentDate = "1 September 2022";
        this.cartItems = new ItemToPurchase[CAPACITY];
        this.itemCount = 0;
    }

    // Argument constructor
    public ShoppingCart(String name, String date) {
        this.customerName = name;
        this.currentDate = date;
        this.cartItems = new ItemToPurchase[CAPACITY];
        this.itemCount = 0;
    }

    // Customer name accessor and mutator
    public String getCustomerName() { return this.customerName; } 
    public void setCustomerName(String name) { this.customerName = name; }

    // Date accessor and mutator
    public String getDate() { return this.currentDate; }
    public void setDate(String date) { this.currentDate = date; }

    // Check if item input is valid and if true, add item
    public boolean addItem(ItemToPurchase item) {
        // Check if shopping cart is full
        if (this.itemCount == CAPACITY) {
            System.out.println("SHOPPING CART IS FULL");
            return false;
        }
        // Check if item is already in shopping cart
        for (int i = 0; i < this.itemCount; i++) {
            if (item.getName().equals(this.cartItems[i].getName())) {
                System.out.println("ITEM ALREADY EXISTS");
                return false;
            }
        }

        // Add item to shopping cart
        this.cartItems[itemCount] = item;
        this.itemCount += 1;
        return true;
    }

    // Get quantity of all items in cart
    public int getNumItems() {
        int totalItemCount = 0;
        // Go through every item in cart and add to total
        for (int i = 0; i < this.itemCount; i++) {
            totalItemCount += this.cartItems[i].getQuantity();
        }
        return totalItemCount;
    }

    // Get total cost of all items in cart
    public int getCostOfCart() {
        int totalCost = 0;
        // Go through every item in cart and add to total
        for (int i = 0; i < this.itemCount; i++) {
            totalCost += this.cartItems[i].getTotalPrice();
        }
        return totalCost;
    }

    // Print total information on shopping cart
    public void printTotal() {
        // Print customer name and date
        System.out.println(this.customerName + " - " + this.currentDate);
        // Check if cart is empty
        if (this.itemCount == 0)
            System.out.println("SHOPPING CART IS EMPTY");
        else {
            // Print number of total items in cart
            System.out.println("Number of items: " + this.getNumItems());
            // Print information of each item in cart
            for (int i = 0; i < this.itemCount; i++) {
                System.out.println(String.format("%s %d @ $%d = $%d", cartItems[i].getName(), cartItems[i].getQuantity(), cartItems[i].getPrice(), cartItems[i].getTotalPrice()));
            }
            // Print total cost of shopping cart
            System.out.println("Total: $"+this.getCostOfCart());
        }
    }

    /*
        Part 3 - Updating the shopping cart
        Allow the user to update the items already added to the shopping cart
     */

    // Remove specified item from the shopping cart
    public void removeItem(String itemName) {
        // Check existance of item
        boolean itemFound = false;
        for (int existanceIndex = 0; existanceIndex < this.itemCount; existanceIndex++) {
            if (itemName.equals(this.cartItems[existanceIndex].getName())) {
                // Remove array item by writing null into it's position
                this.cartItems[existanceIndex] = null;
                // Change item count to new value
                this.itemCount -= 1;
                // Shift elements down the array so they won't be overridden by new elements
                for (int shiftingIndex = existanceIndex; shiftingIndex < this.itemCount; shiftingIndex++)
                    this.cartItems[shiftingIndex] = this.cartItems[shiftingIndex+1];
                System.out.println("["+itemName+"] is removed from your shopping cart.");
                itemFound = true;
                break;
            }
        }
        // If item doesn't exist
        if (!itemFound)
            System.out.println("["+itemName+"] not found in cart.");
    }

    // Modify an item's quantity
    public void modifyItem(String itemName) {
        // Check existance of item
        boolean itemFound = false;
        for (int existanceIndex = 0; existanceIndex < this.itemCount; existanceIndex++) {
            if (itemName.equals(this.cartItems[existanceIndex].getName())) {
                // Prompt user for new quantity and set
                Scanner scnr = new Scanner(System.in);
                System.out.println("Please enter the new quantity");
                cartItems[existanceIndex].setQuantity(scnr.nextInt());
                itemFound = true;
                break;
            }
        }
        // If item could not be found
        if (!itemFound)
            System.out.println("["+itemName+"] not found in cart. Nothing modified");
    }

    // Generate summary of shopping cart
    public void checkout() {
        // Check if shopping cart is empty
        if (itemCount == 0) {
            // If shopping cart is empty
            System.out.println("SHOPPING CART IS EMPTY");
        }
        else {
            // Generate summary of cart using printTotal()
            this.printTotal();
            // Remove all items from cart
            this.cartItems = new ItemToPurchase[CAPACITY];
            System.out.println("Thank you for shopping.");
        }
    }
}