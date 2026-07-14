1. Explain what *args is in Python.
        - Explain why *args is useful when a function
          must accept a variable number of positional
          arguments.
        - Explain what type of object *args becomes
          inside the function.
        - Give an example of a function that uses *args.
<h2>What is *args in Python?</h2>

<p>
*args allows a function to accept any number of positional arguments.
</p>

<br>

<h2>Why is *args Useful?</h2>

<p>
It is useful when you do not know in advance how many arguments will be passed to a function.
</p>

<ul>
    <li>Accepts zero or more arguments.</li>
    <li>Makes functions more flexible.</li>
    <li>Avoids writing multiple parameters manually.</li>
</ul>

<br>

<h2>What Type Does *args Become?</h2>

<p>
Inside the function, *args becomes a tuple.
</p>

<p>
Example: args = (1, 2, 3, 4)
</p>

<br>

<h2>Example</h2>

<p>
Function:
</p>

<p>
def total_sum(*args):<br>
return sum(args)
</p>

<p>
Call:
</p>

<p>
total_sum(10, 20, 30)
</p>

<p>
Output: 60
</p>

2. Explain what **kwargs is in Python.
        - Explain how **kwargs is different from *args.
        - Explain what type of object **kwargs becomes
          inside the function.
        - Give an example of a function that uses
          **kwargs.
<h1>**kwargs in Python</h1>

<p>
**kwargs allows a function to accept any number of keyword arguments.
</p>

<br>

<h2>Difference Between *args and **kwargs</h2>

<ul>
    <li>*args collects extra positional arguments.</li>
    <li>**kwargs collects extra keyword arguments.</li>
</ul>

<p>Example:</p>

<ul>
    <li>*args → (10, 20, 30)</li>
    <li>**kwargs → {"name": "Alice", "age": 25}</li>
</ul>

<br>

<h2>Type of Object</h2>

<p>
Inside the function, **kwargs becomes a dictionary.
</p>

<p>
Example:
{"city": "Delhi", "role": "Engineer"}
</p>

<br>

<h2>Example</h2>

<p>
def profile(**kwargs):<br>
print(kwargs)
</p>

<p>
profile(name="Alice", age=25)
</p>

<p>
Output:<br>
{"name": "Alice", "age": 25}
</p>

3. Explain the correct order of parameters in a Python
   function definition when using positional arguments,
   default arguments, *args, and **kwargs together.
        - Give an example signature using all four.
<h2>Order of Parameters in Python Functions</h2>

<p>The correct order is:</p>

<ul>
    <li>Positional Arguments</li>
    <li>Default Arguments</li>
    <li>*args</li>
    <li>**kwargs</li>
</ul>

<br>

<h3>Syntax</h3>

<p>
def function_name(positional, default=value, *args, **kwargs):
</p>

<br>

<h3>Example</h3>

<p>
def display(name, age=18, *marks, **details):
</p>

<ul>
    <li><b>name</b> → Positional argument</li>
    <li><b>age=18</b> → Default argument</li>
    <li><b>*marks</b> → Variable positional arguments</li>
    <li><b>**details</b> → Variable keyword arguments</li>
</ul>

<br>

<h3>Example Call</h3>

<p>
display("Tushar", 20, 85, 90, city="Bhubaneswar", course="Python")
</p>

5. Explain when you would prefer **kwargs over a
   regular dictionary parameter.
        - Give one real-world example (e.g. building
          a configuration object or a database record).
<h2>When to Use **kwargs</h2>

<p>
Use <b>**kwargs</b> when the number or names of keyword arguments are not known in advance.
It makes a function more flexible.
</p>

<br>

<h2>Why Prefer **kwargs?</h2>

<ul>
    <li>No need to create a dictionary before calling the function.</li>
    <li>Allows passing any number of named arguments.</li>
    <li>Makes functions flexible and reusable.</li>
</ul>

<br>

<h2>Real-World Example</h2>

<p>
While building a user profile or configuration object, different users may provide different details.
Using <b>**kwargs</b> allows accepting fields like age, city, email, role, etc., without defining them beforehand.
</p>

<ul>
    <li>build_profile("Alice", age=25, city="Delhi")</li>
    <li>build_profile("Bob", role="Manager", salary=50000)</li>
</ul>
