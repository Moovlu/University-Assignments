// Import required java modules
import java.util.Scanner;

// Main class
public class ShoppingCartManager {
    public static void main(String [] args) {

    }

    public static void stage1(ItemToPurchase item) {
        // Create new scanner object
        Scanner scnr = new Scanner(System.in);

        // Read name input and change item name
        System.out.println("******** Stage 1 ********\nEnter name of the item:");
        item.setName(scnr.nextLine());

        // Read price input and change item price
        System.out.println("Enter price of "+item.getName()+":");
        item.setPrice(scnr.nextInt());

        // Read quantity input and change item quantity
        System.out.println("Enter quantity:");
        item.setQuantity(scnr.nextInt()); 

        // Print total cost calculation
        System.out.println("Total: " + item.toString());

    }

    public static void stage2(ShoppingCart cart) {
        // Create new scanner object
        Scanner scnr = new Scanner(System.in);

        // Read customer name input and change customer name
        System.out.println("******** Stage 2 ********\nEnter name of the customer:");
        cart.setCustomerName(scnr.nextLine());

        // Read date input and change date
        System.out.println("Enter the current date:");
        cart.setDate(scnr.nextLine());

        // Print totals
        cart.printTotal();

        do {
            // Create new item object
            ItemToPurchase item = new ItemToPurchase();

            // Read name input and change item name
            System.out.println("Enter name of the item:");
            item.setName(scnr.nextLine());

            // Add item to cart to check if it exists
            if (cart.addItem(item)) {

                // Read price input and change item price
                System.out.println("Enter price of "+item.getName()+":");
                item.setPrice(scnr.nextInt());

                // Read quantity input and change item quantity
                System.out.println("Enter quantity:");
                item.setQuantity(scnr.nextInt()); 
                
                // Using the leftover newline (why is this even a limitaton? 😠)
                scnr.nextLine();
            }

            // Ask if user wants to add more items
            System.out.println("Add more? (Y/N)");
            if (scnr.nextLine().equals("N"))
                break;
        }
        while (true);

        // Print totals
        cart.printTotal();
    }

    public static void stage3(ShoppingCart cart) {
        // Create new scanner object
        Scanner scnr = new Scanner(System.in);

        // Prompt if user wants to remove item
        System.out.println("******** Stage 3 ********\nDo you want to remove an item? Y/N");
        if (scnr.nextLine().equals("Y")) {
            // Ask user for item name
            System.out.println("Enter name of the item:");
            // Remove item from cart
            cart.removeItem(scnr.nextLine());
            // Print totals
            cart.printTotal();
        }
        else
            System.exit(0);
        
        // Prompt if user wants to modify item
        System.out.println("Do you want to modify an item from the cart? Y/N");
        if (scnr.nextLine().equals("Y")) {
            // Ask user for item name
            System.out.println("Enter name of the item:");
            // Modify item from cart
            cart.modifyItem(scnr.nextLine());
            // Print totals
            cart.printTotal();
        }
        else
            System.exit(0);

        // Prompt if user wants to checkout
        System.out.println("Do you want to checkout? Y/N");
        if (scnr.nextLine().equals("Y")) {
            cart.checkout();
        }
        else
            System.exit(0);
        
    }

    public static void stage4() {
        // Create new scanner object
        Scanner scnr = new Scanner(System.in);

        // Create new VIP shopping cart object
        VIPShoppingCart cart = new VIPShoppingCart();

        // Prompt user for customer details
        System.out.println("******** Stage 4 ********\nEnter name of the customer:");
        cart.setCustomerName(scnr.nextLine());
        System.out.println("Enter the current date:");
        cart.setDate(scnr.nextLine());
        System.out.println("Enter the available points:");
        cart.setcustomerPoints(scnr.nextInt());

        // Once again use the leftover newline
        scnr.nextLine();

        do {
            // Create new item object
            ItemToPurchase item = new ItemToPurchase();

            // Read name input and change item name
            System.out.println("Enter name of the item:");
            item.setName(scnr.nextLine());

            // Add item to cart to check if it exists
            if (cart.addItem(item)) {

                // Read price input and change item price
                System.out.println("Enter price of "+item.getName()+":");
                item.setPrice(scnr.nextInt());

                // Read quantity input and change item quantity
                System.out.println("Enter quantity:");
                item.setQuantity(scnr.nextInt()); 
                
                // Using the leftover newline (why is this even a limitaton? 😠)
                scnr.nextLine();
            }

            // Ask if user wants to add more items
            System.out.println("Add more? (Y/N)");
            if (scnr.nextLine().equals("N"))
                break;
        }
        while (true);

        // Print totals and ask to redeem points
        cart.checkout();
    }
}