# Week 7 Review

## Assessing your Problem Solutions

Again, the content of this week's module is less about new expressions and algorithmic structures, and more about _how_ you design and build your programs. Although correctly meeting problem requirements remains part of how you will be graded, we will now also focus on how you designed the program that meets those requirements. Specifically, we will look for:

* appropriate separation of concerns (including classes)
* appropriate use of function interfaces (i.e., using parameters and return values, not using variables declared as part of a script to make them accessible in all function scopes)
* comments explaining the why behind more difficult areas of code
* documentation of classes/modules for explaining their purpose and usage
* good function, parameter, and variable names that communicate the purpose and make the program more readable

Please keep in mind there is no single correct answer for how you design the program: there are many good approaches that are worth full credit. If you find yourself in a spiral of trying to perfectly optimize function interfaces and writing a lot of functions with a single line of code in them, you are probably overthinking it.

## 1 [stock_seller.py]
You're working on software for a small financial firm to track clients' stock holdings. In particular, you're charged with modeling stock purchases. Clients will purchase shares of stock at some price per share. Often clients want to explore how much profit they could earn from selling some of their stock shares at the current market price, and, if they think it is the right moment, then actually sell some shares.

For example, assume we have a client that buys 100 shares of the MARY stock (MARY being the stock symbol) at $2.50 per share. The price of MARY stock rises to $10 per share. Now the client is thinking of selling 20 of those 100 shares. Those 20 shares originally cost the client $50 (20 * $2.50) and they are now worth $200 (20 * $10, the current market price), thus the client would profit $150 ($200 - $50) if they sold the 20 shares right now. The client decides to sell the 20 shares, leaving them with only 80 shares of MARY stock left.

You are to write a class named `StockHolding` which will represent a client's stock holding. In this context a `StockHolding` object should store the following data in instance variables (i.e., you will need to modify the provided `__init__` constructor):

* a symbol for the stock (e.g., "MARY")
* the number of shares purchased
* the initial price the client paid per share

The StockHolding class should then have the following methods:

* accessor methods for the number the stock symbol (`getSymbol`), the number of shares (`getNumOfShares`)
* an accessor method for the total cost (`getTotalCost`) of the shares being currently held, for example if the client purchased 50 shares of the stock at $3 a share, then while they're still holding 50 shares this method would return $150 (50 shares times the $3). If they later sold 20 shares and now only have 30 shares left, then this method should return $90 (the 30 shares left times the $3)
* a method named `estimateProfit` that should have two parameters: (1) a number of shares that could be sold and (2) a current price for those shares if they were sold right now. The `estimateProfit` method should return how much profit the client would earn if they sold that number of shares at the current price (i.e., the difference between the money they would earn selling at the current price and how much those shares cost them originally). Note that this value can be negative: shares are sold at losses too.
* a mutator method named `sellShares` with one parameter: a number of shares to sell, that modify the value of shares being held by subtracting the number of shares to be sold from the number of shares being held. It also should raise a ValueError if the client attempts to sell more shares than they own (e.g., if we attempt to sell 90 shares of MARY when we only have 80, this should raise an Error, not just print out a message)

In the same python file as your `StockHolding` class, you will also find a `main` function. The purpose of this `main` function will be to test your `StockHolding` class and show that it works as required above. In that main function, you should:

* Create an instance of your `StockHolding` class
* Output the result of calling the accessor methods to show the `StockHolding object is properly initialized
* Call the `estimateProfit` method and, using a conditional statement, output a message only if the returned estimated profit is the value you expect
* Call the `sellShares` method and, using a conditional statement with the shares accessor, output a message only if the number of shares after selling is the value you expect
* Call the `sellShares` method attempting to sell more shares than you have to show the ValueError is raised


## 2 [die_sum_counter/die_sum_counter.py, die_sum_counter/double_die_roller.py]
You are to write a new UI Widget called a `SumCounterView` for displaying the number of times a sum of two die is rolled in our Double Die Roller program.

The `SumCounterView` UIWidget should be displayed as a rectangle with text in the middle. The text should display two pieces of data:

* The sum the `SumCounterView` is counting (e.g., if it is counting how many times the sum of the two die is 9 then it could have text 'Total of 9 counted')
* The total number of times that sum has been rolled (e.g., if it is counting how many times the sum of the two die is 9, and a total of 9 has been rolled 3 times, then it should have the text "3 times")

For example, if we have a `SumCounterView` widget counting how many times 9 is rolled, and it has been rolled 3 times, it could look like this:

![9_counted_3_times](/images/9_counted_3_times.png)

Then if we rolled two dice again and their total was 9, the `SumCounterView` could increment how many times it had counted 9 be rolled to 4 times, and update its view to this:

![9_counted_4_times](/images/9_counted_4_times.png)

All files necessary for this problem should be found in the `die_sum_counter` folder from the repository. You should write your `SumCounterView` UI Widget class in the `sum_counter_view.py` file. The `SumCounterView` UI Widget class should:

* store what sum it is counting
* store how many times it has counted the value
* draw itself and its text in a given window at a given location

Additionally, the `SumCounterView` class should contain a method named `handleRoll` that takes a single parameter: the sum of the roll of two die. Note this one parameter is not a die, or two die values, it is the sum of two die values. Within the `handleRoll` method, if the sum argument matches the sum a `SumCounterView` object is counting, then it should increment the count and update the view to show the count has changed. There should be no die rolling in the `SumCounterView` class.

You will be integrating instances of the `SumCounterView` class into our `double_die_roller` program such that the `double_die_roller` window will now include multiple `SumCounterView` objects that display how many times a sum has been rolled, like this:

![pre_roll_counts](/images/pre_roll_counts.png)

If we click the roll button and roll a 9, as shown below, note how the total number of times 9 is counted is increment by 1 to be 5 times the sum 9 has been counted:

![post_roll_counts](/images/post_roll_counts.png)

Within in the `double_die_roller` program you should create at least four `SumCounterView` object, each counting a different sum, and then after each time a user presses the roll button, have each `SumCounterView` object handle the roll by passing the sum of the roll to the `handleRoll` method for each instance. Each instance should only increment its count and update its view if the total sum of the rolled die is the same as the sum the `SumCounterView` object is counting.
