"""
## 3. Products Within Budget Report  *(Medium)*

=================================================
PRODUCTS WITHIN BUDGET REPORT
=================================================

Problem Statement:
You are given a LIST of TUPLES, where each
tuple represents a product:
        (product_name, price)

Write a Python program that builds a REPORT
DICTIONARY in the following form:

   {
     "within_budget":  [list of (name, price) tuples],
     "over_budget":    [list of (name, price) tuples],
     "categories":     {
                         "cheap":    set of names with price <  50,
                         "moderate": set of names with 50 <= price <= 200,
                         "costly":   set of names with price >  200
                       },
     "cheapest":       (name, price),
     "costliest":      (name, price)
   }

-------------------------------------------------
Input Example:
products = [
   ("Pen",    10),
   ("Book",   150),
   ("Bag",    500),
   ("Pencil", 5),
   ("Lamp",   300),
   ("Mug",    80),
]
budget = 200

Output Example:
{
  'within_budget': [('Pen',10), ('Book',150),
                    ('Pencil',5), ('Mug',80)],
  'over_budget':   [('Bag',500), ('Lamp',300)],
  'categories': {
      'cheap':    {'Pen', 'Pencil'},
      'moderate': {'Book', 'Mug'},
      'costly':   {'Bag', 'Lamp'}
  },
  'cheapest':  ('Pencil', 5),
  'costliest': ('Bag', 500)
}

-------------------------------------------------
Explanation:
Iterate once through the product list and
classify every item:
   price <  50  -> cheap
   50..200      -> moderate
   price > 200  -> costly
Compare each price to the budget to split it
into within/over budget. While iterating, also
remember the smallest and largest prices seen
so far to find the cheapest and costliest
products.
=================================================

"""
n = int(input("Enter number of products: "))
list_0f_prdcts = []
for i in range(n):
    prdct_name = input("Enter the name of the product: ")
    prdct_price = int(input("Enter the price of this product: "))
    list_0f_prdcts.append((prdct_name, prdct_price))
budget = int(input("Enter your budget: "))
report = {
    'within budget' : list(filter(lambda x: x[1] <= budget, list_0f_prdcts)),
    'over budget' : list(filter(lambda x: x[1] > budget, list_0f_prdcts)),
    'categories' : {
        'cheap' : list(filter(lambda x: x[1] < 50, list_0f_prdcts)),
        'moderate' : list(filter(lambda x: x[1] <= 200 and x[1] <= 50, list_0f_prdcts)),
        'costly' : list(filter(lambda x: x[1] > 200, list_0f_prdcts))
    },
    'cheapest' : min(list(map(lambda x: x[1], list_0f_prdcts))),
    'costliest' : max(list(map(lambda x: x[1], list_0f_prdcts)))
}
print(f"Report: \n {report}")