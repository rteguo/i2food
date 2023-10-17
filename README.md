# <img src="https://github.com/rteguo/i2food/blob/main/static/img/i2food.png">
# i2food : improve the impact of food

## Summary
**i2food** project is a contribution to help people select healthy foods to stay in good health. It is an e-commerce application for selling fresh food products that offers ratings for products based on their nutrient composition. In the customer journey, it is possible to consult and print information about the composition of each product which can be printed. Information about the composition of the products is provided by the [Ninja API](https://api-ninjas.com/api/nutrition). When the product selection is complete, the customer can review the cart and proceed to validate the order. The web site also integrates a content management system that allows the administrator to view validated orders and perform product management operations as well as manage user accounts.


## About the Softfware Engineer

i2food plateforme was designed and implemented  by **Romaric Cyrille TEGUO**. Learn more about the developer on [LinkedIn](https://www.linkedin.com/in/romaric-teguo/).


## Architecture and Technologies

My application is built on a 3-layers architecture:
- Data layer : Postgres
- Back End layer : Flask, SQLAlchemy, Python
- Front End layer : HTML/CSS/Js, Bootstrap, Jinja, AJAX, JQuery
- API: [Ninja API](https://api-ninjas.com/api/nutrition)

![Architecture of my app](https://github.com/rteguo/i2food/blob/main/static/img/architecture-i2food-m.png)

## Features

**Front End features:**
- User registration
- User login
- Display the products with rating relating their nutrient composition
- Add product in the cart
- Remove product in the cart
- Display the details of product which include nutritional information 
- Print the information about the nutrient composition of product 
- Display recently sold products
- Submit the order
- Send the message with contact form

**Back End features (for administrator profile):**
- Consult the List of orders 
- Cosult the details of each order
- Consult the list of products
- Update the information about product
- Add new product in the database
- Consult the list of user accounts
- Add new user
- Get the last sale products

## Screenshots

![Home page i2food](https://github.com/rteguo/i2food/blob/main/static/img/home-page.png)