#Agent Based Model Description

The aim of my PhD project is to develop cutting-edge marketing analysis applied to sales data and store location data. My plan is to develop a series of tools and models using "network analysis". Such methods will allow me to investigate the relationship between many "nodes" which could be particular retail outlets, products or individual consumers.

This model aims at recreating the buying behaviour of customers in an urban setting. To do so, I have created an agent based model (ABM) composed of 8 stores and 50 customers. The stores are given an initial revenue. The model, after a set number of iterations, will write a csv file showing the final revenue of the stores.

The stores and customers were created through their respective classes by generating, at random, a x-coordinate and a y-coordinate to be placed in a 100x100 plane. Each store is assigned a store number and a revenue which was retrieved from the csv file that was read into the model. The customers are instead given a money variable which is constant for all at 100.

After creating stores and customers, the customers are moved at random in the plane 100 times. To avoid customers wandering off the environment, the plane was modelled to resemble a torus so that customers exiting the plane at the top would appear at the bottom, and customers exiting on the right would reappear on the left.

As normal customers would do, the customers in this model move and shop in the stores they find themselves closest to. For this reason, the customers, while they move, calculate which shops they are closest to, and if they have enough money, they shop. Every time a customer shops the revenue of the store increases by the amount spent by the customer.

The next step in the model is to write a new csv file that shows the final revenue of the shops after 100 iterations. To do so, a new list of revenue is created and written to a csv file. Customers and Stores are finally plotted in a graph to show a visual image of the model. The stores are plotted in blue, while the customers are plotted in tan.
