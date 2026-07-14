1. Explain what a dictionary is in Python.
        - Explain the key-value pair structure.
        - Explain why dictionary keys must be immutable.
        - Give an example of creating and accessing
          a dictionary.
<h1>Dictionary in Python</h1>

<p>
A dictionary is a Python data structure that stores data as key-value pairs.
</p>

<br>

<h2>Key-Value Pair Structure</h2>

<ul>
    <li>Key → Identifier</li>
    <li>Value → Associated data</li>
</ul>

<br>

<h2>Why Keys Must Be Immutable</h2>

<p>
Keys must be immutable so Python can find values efficiently using hashing.
</p>

<ul>
    <li>Valid keys: strings, integers, tuples</li>
    <li>Invalid keys: lists, dictionaries</li>
</ul>

<br>

<h2>Example</h2>

<p>
student = {"name": "Tushar", "age": 19}
</p>

<p>
student["name"] → Tushar
</p>

2. Explain commonly used dictionary methods in Python.
    Explain the purpose of:
        - keys()
        - values()
        - items()
        - get()
<h1>Common Dictionary Methods in Python</h1>

<br>

<h2>1. keys()</h2>
<p>
Returns all keys present in the dictionary.
</p>

<ul>
    <li>Used to access dictionary keys.</li>
</ul>

<br>

<h2>2. values()</h2>
<p>
Returns all values present in the dictionary.
</p>

<ul>
    <li>Used to access dictionary values.</li>
</ul>

<br>

<h2>3. items()</h2>
<p>
Returns key-value pairs as tuples.
</p>

<ul>
    <li>Useful for looping through both keys and values.</li>
</ul>

<br>

<h2>4. get()</h2>
<p>
Returns the value of a specified key.
</p>

<ul>
    <li>Prevents errors if the key does not exist.</li>
</ul>

3. Explain what a tuple is in Python.
        - Explain how a tuple is different from a list.
        - Explain why a tuple is called an immutable
          data type.
        - Give an example of tuple packing and
          tuple unpacking.
<h1>Tuple in Python</h1>

<p>
A tuple is a collection of elements stored in a single variable.
Tuples are created using parentheses ().
</p>

<br>

<h2>Difference Between Tuple and List</h2>

<ul>
    <li>Tuple uses parentheses ()</li>
    <li>List uses square brackets []</li>
    <li>Tuple is immutable</li>
    <li>List is mutable</li>
</ul>

<br>

<h2>Why Tuple is Immutable</h2>

<p>
A tuple is called immutable because its elements cannot be changed,
added, or removed after the tuple is created.
</p>

<br>

<h2>Tuple Packing</h2>

<p>
Packing means storing multiple values into a tuple.
</p>

<p>
Example: t = (10, 20, 30)
</p>

<br>

<h2>Tuple Unpacking</h2>

<p>
Unpacking means assigning tuple elements to separate variables.
</p>

<p>
Example: a, b, c = (10, 20, 30)
</p>

4. Explain the difference between list, tuple, and
   dictionary in Python.
        - Compare them in terms of:
            - mutability
            - ordering
            - syntax used to create them
            - typical use cases
<h1>Difference Between List, Tuple, and Dictionary</h1>

<br>

<h2>List</h2>
<p>A list is an ordered and mutable collection of items.</p>
<ul>
    <li>Mutability: Mutable</li>
    <li>Ordering: Ordered</li>
    <li>Syntax: [1, 2, 3]</li>
    <li>Use Case: Storing and modifying collections of data.</li>
</ul>

<br>

<h2>Tuple</h2>
<p>A tuple is an ordered and immutable collection of items.</p>
<ul>
    <li>Mutability: Immutable</li>
    <li>Ordering: Ordered</li>
    <li>Syntax: (1, 2, 3)</li>
    <li>Use Case: Storing fixed data that should not change.</li>
</ul>

<br>

<h2>Dictionary</h2>
<p>A dictionary stores data as key-value pairs.</p>
<ul>
    <li>Mutability: Mutable</li>
    <li>Ordering: Ordered (Python 3.7+)</li>
    <li>Syntax: {"name": "Tushar", "age": 19}</li>
    <li>Use Case: Fast lookup and storing related data using keys.</li>
</ul>

5. Explain when to use a tuple instead of a list,
   and when to use a dictionary instead of a list.
        - Give one real-world example for each case.
<h2>Tuple vs List</h2>

<p>Use a tuple when the data should not change after creation. Tuples are immutable, while lists are mutable.</p>

<br>

<p><b>Example:</b> Storing a student's date of birth (day, month, year).</p>

<ul>
    <li>Tuple: (15, 8, 2006)</li>
</ul>

<br>

<h2>Dictionary vs List</h2>

<p>Use a dictionary when data is stored as key-value pairs and fast lookup is needed. Use a list for ordered collections of items.</p>

<br>

<p><b>Example:</b> Storing student information.</p>

<ul>
    <li>Dictionary: {"name": "Tushar", "roll": 101, "branch": "CSE"}</li>
</ul>
