1. Explain what a list is in Python.
        - Explain how a list is different from a string.
        - Explain why a list is called a mutable data type.
        - Give an example of creating a list.
<h2>What is a List in Python?</h2>

<p>
A list is a collection data type in Python used to store multiple
items in a single variable. Lists can contain elements of different
data types such as integers, strings, and floating-point numbers.
Lists are created using square brackets [ ].
</p>

<br>

<h2>How is a List Different from a String?</h2>

<ul>
    <li>A string is a sequence of characters enclosed in quotes.</li>
    <li>A list is a collection of elements enclosed in square brackets.</li>
    <li>Strings are immutable, meaning their contents cannot be changed.</li>
    <li>Lists are mutable, meaning elements can be added, removed, or modified.</li>
</ul>

<br>

<h2>Why is a List Called a Mutable Data Type?</h2>

<p>
A list is called mutable because its contents can be changed after
the list is created. We can add new elements, remove existing
elements, or update values without creating a new list.
</p>

<br>

<h2>Example of Creating a List</h2>

<p>
Example:
</p>

<ul>
    <li>numbers = [10, 20, 30, 40]</li>
    <li>names = ["Alice", "Bob", "Charlie"]</li>
    <li>mixed = [1, "Python", 3.14]</li>
</ul>

2. Explain commonly used list methods in Python.
    Explain the purpose of:
        - append()
        - extend()
        - pop()
        - len()
<p>
Python lists provide several built-in methods that make it easy to add,
remove, and manage elements efficiently.
</p>

<br>

<h3>1. append()</h3>

<p>
The <b>append()</b> method is used to add a single element at the end of a list.
It increases the size of the list by one.
</p>

<ul>
    <li>Adds one element at the end of the list.</li>
    <li>Modifies the original list.</li>
</ul>

<br>

<h3>2. extend()</h3>

<p>
The <b>extend()</b> method is used to add multiple elements from another
iterable (such as a list, tuple, or string) to the end of a list.
</p>

<ul>
    <li>Adds multiple elements at once.</li>
    <li>Each element is added separately to the list.</li>
</ul>

<br>

<h3>3. pop()</h3>

<p>
The <b>pop()</b> method removes and returns an element from the list.
By default, it removes the last element, but an index can also be specified.
</p>

<ul>
    <li>Removes an element from the list.</li>
    <li>Returns the removed element.</li>
    <li>Can remove a specific indexed element.</li>
</ul>

<br>

<h3>4. len()</h3>

<p>
The <b>len()</b> function is used to determine the total number of elements
present in a list.
</p>

<ul>
    <li>Returns the length of the list.</li>
    <li>Useful for loops and counting elements.</li>
</ul>

<br>

<h3>Conclusion</h3>

<p>
The methods <b>append()</b>, <b>extend()</b>, and <b>pop()</b> help in adding
and removing elements from a list, while <b>len()</b> is used to find the
number of elements present in the list.
</p>

3. Explain list indexing and list slicing in Python.
        - Explain positive and negative indexing.
        - Explain the syntax- list[start:stop:step]
        - Explain how slicing creates a new list.
<h2>List Indexing</h2>

<p>
List indexing is used to access individual elements of a list using their position.
Each element in a list has an index number.
</p>

<h3>Positive Indexing</h3>

<p>
Positive indexing starts from the beginning of the list.
The first element has index 0, the second element has index 1, and so on.
</p>

<br>

<h3>Negative Indexing</h3>

<p>
Negative indexing starts from the end of the list.
The last element has index -1, the second last element has index -2, and so on.
</p>

<br>

<h2>List Slicing</h2>

<p>
List slicing is used to extract a portion of a list.
It returns a new list containing the selected elements.
</p>

<h3>Syntax</h3>

<p>
list[start:stop:step]
</p>

<ul>
    <li><b>start</b> – Index from where slicing begins.</li>
    <li><b>stop</b> – Index where slicing ends (not included).</li>
    <li><b>step</b> – Number of positions to move during slicing.</li>
</ul>

<br>

<h3>How Slicing Works</h3>

<ul>
    <li>If start is omitted, slicing begins from the first element.</li>
    <li>If stop is omitted, slicing continues to the last element.</li>
    <li>If step is omitted, the default value is 1.</li>
    <li>A negative step can be used to traverse the list in reverse order.</li>
</ul>

<br>

<h2>New List Creation</h2>

<p>
Slicing does not modify the original list. Instead, it creates and returns a new list
containing the selected elements. Any changes made to the sliced list do not affect
the original list.
</p>

4. Explain the difference between append() and extend()
in Python lists.
        - Show what happens when you append a list
          versus when you extend a list.
<p>
Both <b>append()</b> and <b>extend()</b> are used to add elements to a list,
but they work differently.
</p>

<br>

<h3>append()</h3>

<p>
The <b>append()</b> method adds the entire object as a single element at the end of the list.
If a list is appended, the whole list becomes one nested element.
</p>

<ul>
    <li>Adds one element at a time.</li>
    <li>Increases the list length by 1.</li>
    <li>A list remains a nested list when appended.</li>
</ul>

<p><b>Example:</b></p>

<p>
List: [1, 2, 3]<br>
append([4, 5])<br>
Result: [1, 2, 3, [4, 5]]
</p>

<br>

<h3>extend()</h3>

<p>
The <b>extend()</b> method adds each element of an iterable (such as a list,
tuple, or string) individually to the end of the list.
</p>

<ul>
    <li>Adds multiple elements at once.</li>
    <li>Increases the list length by the number of elements added.</li>
    <li>Does not create a nested list.</li>
</ul>

<p><b>Example:</b></p>

<p>
List: [1, 2, 3]<br>
extend([4, 5])<br>
Result: [1, 2, 3, 4, 5]
</p>

<br>

<h3>Comparison</h3>

<ul>
    <li><b>append([4, 5])</b> → [1, 2, 3, [4, 5]]</li>
    <li><b>extend([4, 5])</b> → [1, 2, 3, 4, 5]</li>
</ul>

<p>
In summary, <b>append()</b> adds the entire list as a single element,
whereas <b>extend()</b> adds each element of the list individually.
</p>
