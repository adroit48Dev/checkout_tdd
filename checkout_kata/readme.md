## Checkout Kata

In a normal supermarket, things are identified using Stock Keeping Units, or SKUs. In
our store, we’ll use individual letters of the alphabet (A, B, C, and so on). Our goods are
priced individually. In addition, some items are multi-priced: buy n of them, and they’ll
cost you y pence. For example, item ‘A’ might cost 50 pence individually, but this week
we have a special offer: buy three ‘A’s and they’ll cost you 130. In fact this week’s prices
are:

| Item | Unit Price | Special Price |
| A    | 50         | 3 for 130     |
| B    | 30         | 2 for 45      |
| C    | 10         |               |

Your challenge is to build a checkout application that correctly calculates each of the
items in the customers basket and calculates any discounts

## Example test output:
* 1A = 50
* 1A + 1A = 100
* 1A + 1B = 80
* 1A + 1B + 1C = 90
* 1A + 1A + 1A + 1B = 160

## Understandings
1) Need Product data to get items and price 
2) Need Checkout class to calculate
3) Prior create testcases for checkout, calculating special prices.

## Usage Instructions
clone this repository from github
