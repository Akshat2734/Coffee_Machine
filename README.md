# Coffee_Machine
This is a Python script for a simple coffee machine. The script uses a dictionary MENU to store the ingredients and cost of each type of coffee. The machine has a certain amount of water, milk, and coffee, and it keeps track of how much of each is used.

The script defines several functions:

**report():** This function updates the amount of water, milk, and coffee left in the machine.
**make_latte(), make_espresso(), and make_cappuccino():** These functions update the amount of water, milk, and coffee used based on the ingredients required for each type of coffee.

The main part of the script is a while loop that runs as long as the coffee machine is on. Inside the loop, the user is asked to choose a type of coffee, and then they are asked to insert money. The script checks if the machine has enough ingredients and if the user has inserted enough money. If both conditions are met, the script makes the coffee, updates the amounts of ingredients, and gives the user change if necessary. If the user chooses to see a report, the script prints the current amounts of water, milk, and coffee. If the user does not have enough money or if the machine does not have enough ingredients, the script prints an appropriate message.

The script also includes a delay of 5 seconds and clears the console after each iteration of the loop.
