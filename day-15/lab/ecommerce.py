'''
1. Blueprint Structure (Class & Attributes)
• Class Attribute: platform_name = "ShopMart"
• Constructor (_init__): Must accept three parameters for each product: item_name, category (e.g., Electronics, Clothing), and price.
2. Actions (Methods)
• Method 1 (get_product_tag): This method should return a formatted string containing item details.
• Format: "Buy [item_name] from our [category] collection on [platform_name]."
• Method 2 (apply_discount): This method must accept a discount_amount, subtract it from the price to calculate final deal price, and print it to the screen.
• Formula: deal_price = price - discount amount
3. Execution (Object Creation & Testing)
• Create an object named my_product with the following data: "Wireless Headphones", "Electronics", 5000.
• Call and print the result of get product tag().
• Call apply_discount(700) to display final discounted price.
'''


class ShopMart:

    def __init__(self, name, category, price):

        self.prd_name = name
        self.prd_category = category
        self.prd_price = price

    def get_prdct_tag(self):

        return f"Buy {self.prd_name} from our {self.prd_category} collection on Shop Mart"
    
    def apply_dis(self, dis):

        deal_price = self.prd_price - dis

        print(f"The deal price of this product is {deal_price}/- rupees")


prd_name = input("Enter the product name: ")
prd_category = input("Enter the product category: ")
prd_price = int(input("Enter the price of the product in rupees: "))
prd_dis = int(input("Enter the discount amount in rupees: "))

my_product = ShopMart(prd_name, prd_category, prd_price)

res = my_product.get_prdct_tag()

print(res)

my_product.apply_dis(prd_dis)
