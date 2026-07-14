1. Explain what a lambda function is in Python.
        - Explain the syntax of a lambda expression.
        - Explain how a lambda function is different
          from a regular function defined with def.
        - Give one example of a lambda function.
<h1>Lambda Function in Python</h1>

<p>
A lambda function is a small anonymous function in Python. It can have any number of arguments but only one expression.
</p>

<br>

<h2>Syntax</h2>

<p>
lambda arguments : expression
</p>

<br>

<h2>Difference Between lambda and def</h2>

<ul>
    <li><p><b>lambda</b> creates an anonymous function (no name).</p></li>
    <li><p><b>def</b> creates a named function.</p></li>
    <li><p><b>lambda</b> contains only one expression.</p></li>
    <li><p><b>def</b> can contain multiple statements.</p></li>
    <li><p><b>lambda</b> is generally used for short functions.</p></li>
</ul>

<br>

<h2>Example</h2>

<p>
square = lambda x: x * x
</p>

<p>
square(5) → 25
</p>

2. Explain the map() function in Python.
        - Explain the syntax of map().
        - Explain what map() returns and how to
          convert that result into a list.
        - Give one example of using map() with a
          lambda.
<h2>map() Function in Python</h2>

<p>
The <b>map()</b> function applies a function to every item in an iterable
(such as a list or tuple) and returns the results.
</p>

<br>

<h3>Syntax</h3>

<p>
map(function, iterable)
</p>

<br>

<h3>What Does map() Return?</h3>

<ul>
    <li>map() returns a map object (iterator).</li>
    <li>To see all results, convert it into a list using list().</li>
</ul>

<p>
Example: list(map(function, iterable))
</p>

<br>

<h3>Example Using Lambda</h3>

<p>
Multiply each number in a list by 2:
</p>

<ul>
    <li>numbers = [1, 2, 3, 4]</li>
    <li>result = list(map(lambda x: x * 2, numbers))</li>
    <li>Output: [2, 4, 6, 8]</li>
</ul>

3. Explain the filter() function in Python.
        - Explain the syntax of filter().
        - Explain how filter() decides which items
          to keep.
        - Give one example of using filter() with a
          lambda.
<h1>filter() Function in Python</h1>

<p>
The <b>filter()</b> function is used to select elements from an iterable
(list, tuple, etc.) based on a condition.
</p>

<br>

<h2>Syntax</h2>

<p>
filter(function, iterable)
</p>

<ul>
    <li><b>function</b> → Condition to test each item.</li>
    <li><b>iterable</b> → List, tuple, or other iterable.</li>
</ul>

<br>

<h2>How filter() Works</h2>

<p>
filter() applies the function to each item. If the function returns
<b>True</b>, the item is kept; if it returns <b>False</b>, the item is removed.
</p>

<br>

<h2>Example with Lambda</h2>

<p>
Keep only even numbers from a list:
</p>

<ul>
    <li>numbers = [1, 2, 3, 4, 5, 6]</li>
    <li>result = filter(lambda x: x % 2 == 0, numbers)</li>
</ul>

<p>
Output: 2, 4, 6
</p>

4. Explain the key differences between map() and
   filter().
        - Compare them in terms of:
            - what the function returns
            - the role of the callable passed to them
            - typical use cases
<h2>Difference Between map() and filter()</h2>

<p><b>map()</b> and <b>filter()</b> are built-in Python functions used to process iterable objects such as lists and tuples.</p>

<br>

<h3>1. Return Value</h3>
<ul>
    <li><b>map()</b> returns transformed elements based on a function.</li>
    <li><b>filter()</b> returns only those elements that satisfy a condition.</li>
</ul>

<br>

<h3>2. Role of the Callable Function</h3>
<ul>
    <li><b>map()</b>: The function modifies each element and returns a new value.</li>
    <li><b>filter()</b>: The function returns <b>True</b> or <b>False</b> to decide whether an element should be kept.</li>
</ul>

<br>

<h3>3. Typical Use Cases</h3>
<ul>
    <li><b>map()</b>: Squaring numbers, converting strings to uppercase, type conversion, etc.</li>
    <li><b>filter()</b>: Selecting even numbers, positive values, valid records, etc.</li>
</ul>

<br>

<h3>Example</h3>
<ul>
    <li><b>map()</b>: [1, 2, 3] → [1, 4, 9]</li>
    <li><b>filter()</b>: [1, 2, 3, 4] → [2, 4]</li>
</ul>

