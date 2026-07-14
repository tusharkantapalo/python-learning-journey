1. Explain the difference between Arithmetic Operators and Comparison Operators in Python with examples.
<p>Arithmatic operators are the operators used for mathmatical operations like
addition, substraction, multiplication etc. and comparision operators are used to 
compare any two variables or objects, which returns true if the respective 
comparision is successful else returns false.</p>

2. What is the difference between = and == in Python?
Explain with suitable examples and mention a real-world situation where confusing these two can create errors.
<p>'=' is assignment operator, it is used to refere any object by any variable, 
whereas '==' is a comparision operator which is used to compare any two objects or 
any two variables refering their respective objects and it returns true if both the 
objects are equal or returns false if the objects are not equal</p>
<p>e.g:-        x=5 and (x==5)
int the first case, x is refering to 5 and will print 5 but in the second case, it 
will print 1 if x is 5 or it will print 0 if x is not 5</p>
<p>let a program if password = "admin123":, here it will throw an error as '=' is 
not an assignment operator</p>
3. What are Logical Operators in Python?
Explain how and, or, and not work using truth table examples.
<p>Logical Operators in Python are used to combine multiple conditions and return 
either True or False.They are and, or not</p>
<h2>and</h2>
<ol>
    <li>0  0 -> 0</li>
    <li>0  1 -> 0</li>
    <li>1  0 -> 0</li>
    <li>1  1 -> 1</li>
</ol>
<h2>or</h2>
<ol>
    <li>0  0 -> 0</li>
    <li>0  1 -> 1</li>
    <li>1  0 -> 1</li>
    <li>1  1 -> 1</li>
</ol>
<h2>not</h2>
<ol>
    <li> 0 -> 1 </li>
    <li> 1 -> 0 </li>
</ol>

4. A company gives bonuses based on the following conditions:

    Employees with experience greater than 5 years and rating above 8 get a 20% bonus.
    Employees with rating below 5 or attendance below 75% get no bonus.
    All others get a 10% bonus.

    Explain how conditional statements and logical operators help implement this system in Python.
    Also explain why multiple conditions are important in real-world applications.
<p>if experience > 5 and rating > 8:<br>
      bonus = salary * 0.20<br>
   elif rating < 5 or attendance < 75:<br>
      bonus = 0<br>
   else:<br>
      bonus = salary * 0.10</p>
<p>Conditional statements (`if`, `elif`, `else`) help the program make decisions 
based on employee details. Logical operators (`and`, `or`) combine multiple 
conditions to check bonus eligibility. Together they automate bonus calculation 
accurately by applying different rules for experience, performance rating and 
attendance, making the system efficient and reliable.</p>
<p>Multiple conditions are important in real-world applications because decisions 
often depend on several factors together. For example, employee bonuses, loan 
approvals and student grading systems require checking multiple conditions to ensure 
accurate, fair and reliable results.</p>