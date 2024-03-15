// Import required java modules
import java.util.Scanner;

public class VIPShoppingCart extends ShoppingCart {

    // Create variables
    private int customerPoints;
    private int totalCost;

    // No argument constructor
    public VIPShoppingCart() {
        super();
        this.customerPoints = 0;
        this.totalCost = 0;
    }

    // Argument constructor
    public VIPShoppingCart(String name, String date) {
        super();
        this.customerPoints = 0;
        this.totalCost = 0;
    }

    // customerPoints accessor
    public int getcustomerPoints() { return this.customerPoints; }
    // customerPoints mutator
    public void setcustomerPoints(int points) { this.customerPoints = points; }

    // Print total information on shopping cart
    @Override
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
            // Check if discount should be applied
            if (this.getCostOfCart() < 100) {
                // Print total cost
                this.totalCost = this.getCostOfCart();
                System.out.println("Total: $"+this.totalCost);
                System.out.println("No discount for a total less than 100.");
            }
            else {
                // Round and print total cost with discount
                double discountDouble = this.getCostOfCart() * 0.95 + 0.5;
                this.totalCost = (int) discountDouble;
                System.out.println("Total: $"+this.totalCost+" (after 5% discount)");
            }
        }
    }

    // Generate summary of shopping cart
    @Override
    public void checkout() {
        // Check if shopping cart is empty
        if (itemCount == 0) {
            // If shopping cart is empty
            System.out.println("SHOPPING CART IS EMPTY");
        }
        else {
            // Generate summary of cart using printTotal()
            this.printTotal();
            // Ask if they want to redeem points
            redeemPoints();
            // Remove all items from cart
            this.cartItems = new ItemToPurchase[CAPACITY];
            // Apply new points and print thanks message
            this.customerPoints += this.totalCost;
            System.out.println("\nThank you for shopping with us. "+this.totalCost+" points added!");
        }
    }

    // Redeeming points at checkout
    private void redeemPoints() {
        // Create new scanner object
        Scanner scnr = new Scanner(System.in);
        // Ask if user wants to redeem points
        System.out.println("\nRedeem points? (Y/N)");
        if (scnr.nextLine().equals("Y")) {
            int pointsInput = 0;
            System.out.println("Enter points to be redeemed, -1 to quit:");
            do {
                pointsInput = scnr.nextInt();
                pointsInput = (pointsInput/50)*50;
                // Check if points inputted is valid and redeem if true
                if (pointsInput < 50)
                    System.out.println("Less than 50! Please retry. Enter -1 to quit:");
                else if (pointsInput > this.customerPoints)
                    System.out.println("Not enough points. Please retry. Enter -1 to quit:");
                else {
                    // Rounds down to the nearest 50 through int casting
                    this.totalCost -= pointsInput/50;
                    this.customerPoints -= pointsInput;
                    System.out.println("Redeeming "+pointsInput+" points.\nTotal to pay: $"+this.totalCost);
                    break;
                }
            }
            while (pointsInput != -1);
        }
    }
}