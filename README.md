# grocery_store_simulation
Event-driven simulation for a grocery store, which could help in making decisions like how many employees to hire to staff checkout lines with varying numbers of customers arriving throughout the day.

## Feautures:
- Event Driven Simulation: Processes events like customer arrivals, checkout start, and line closures to update the state of the store over time.
- Types of Checkout Lines: Regular, Express and Self-serve
- Events:
    - Customer Arrival: Adds a customer to a checkout line based on availability.
    - Checkout Started: A customer starts checking out in a line.
    - Checkout Completed: A customer finishes checking out and leaves the line.
    - Close Line: A checkout line closes, causing customers to join new lines.
- Statistics:
    - Total number of customers processed.
    - Final event timestamp.
    - Maximum wait time any customer experienced. 
