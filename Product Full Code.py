import random

#Create a class by the name of "product" which also outlines the vairous variables that will be used in the program.
#Then it bascially initilizes product and its attributes.

class Product:
    def __init__(self, product_code, product_name, sale_price, manufacture_cost, stock, monthly_production):
        self.product_code = product_code
        self.product_name = product_name
        self.sale_price = sale_price
        self.manufacture_cost = manufacture_cost
        self.stock = stock
        self.monthly_production = monthly_production
        self.recurrent_sales = []     #This is the list to store monthly sales.

    def sales_monthly (self):

#Creates random monthly sales (range: monthly_production (variable name) +/- 10).

        lowest_sales = max(0, self.monthly_production - 10)
        highest_sales = self.monthly_production + 10
        recurrent_sales = random.randint(lowest_sales, highest_sales)
        self.recurrent_sales.append(recurrent_sales)     #Record monthly sales.
        self.stock += self.monthly_production - recurrent_sales     #Update stock level.

#"net_profit" is defined along with other variables and it returns the net profit by using the equation on line 31.

    def net_profit(self):
        total_units_sold = sum(self.recurrent_sales)
        total_units_manufactured = sum(self.monthly_production for _ in range(12))
        return (total_units_sold * self.sale_price) - (total_units_manufactured * self.manufacture_cost)

#Class is created for the "StockStatement".

class StockStatement:
    def __init__(self, product):
        self.product = product

#Here the product sale details are displayed for the user to view along with the info about the stock.

    def stock_questions(self):
        print("\n")
        print(f"Product code: {self.product.product_code}")
        print(f"Product Name: {self.product.product_name}\n")
        print(f"Sale Price: {self.product.sale_price:.2f} CAD")
        print(f"Manufacture Cost: {self.product.manufacture_cost:.2f} CAD")
        print(f"Monthly Production: {self.product.monthly_production} units (Approx.) \n")

#Here we generate and display the future stock for the next 12 months along with how many manufactured units made and how many we sold.

    def future_stock(self):
        for i in range(12):
            self.product.sales_monthly()
            print(f"Month {i + 1}: \n \t Manufactured: {self.product.monthly_production} units \n\t Sold: {self.product.recurrent_sales[i]} units \n\t Stock: {self.product.stock} units \n")

        net_profit = self.product.net_profit()
        print(f"Net Profit: {net_profit:.2f} CAD")

#We make an application class for the users interaction and ask question aboout the product.

class Application:
    def product_questions(self):

        product_code = int(input("Please enter the Product code: "))
        name = input("Please enter Product Name: ")
        stock = int(input("Please enter the current Stock: "))
        sale_price = float(input("Please enter the Product Sale Price: "))
        manufacture_cost = float(input("Please enter the Product Manufacture Cost: "))
        monthly_production = int(input("Please enter estimated monthly production: ")) 
        
#We gather the users input to develop a product instance.

        product = Product(product_code, name, sale_price, manufacture_cost, stock, monthly_production)
        stock_statement = StockStatement(product)
        return stock_statement

if __name__ == "__main__":
    app = Application()
    stock_statement = app.product_questions()
    stock_statement.stock_questions()
    stock_statement.future_stock()
