"""
## 2. Build a Person Profile with **kwargs  *(Medium)*

=================================================
BUILD A PROFILE DICTIONARY USING **KWARGS
=================================================

Problem Statement:
Write a Python FUNCTION called `build_profile`
that accepts a required argument `name` and
ANY number of additional keyword arguments
using **kwargs.

The function must return a DICTIONARY in the
following form:
   {
     "name":   <name>,
     "details": { ...all kwargs... },
     "fields": ( ...tuple of kwarg keys... )
   }

-------------------------------------------------
Input Example:
build_profile(
    "Alice",
    age=25,
    city="Delhi",
    role="Engineer"
)

Output Example:
{
  'name': 'Alice',
  'details': {'age': 25, 'city': 'Delhi', 'role': 'Engineer'},
  'fields': ('age', 'city', 'role')
}

-------------------------------------------------
Explanation:
**kwargs collects all extra keyword arguments
into a dictionary. The function copies them
into "details" and stores their keys in a
tuple called "fields".
=================================================

"""
def build_profile(name, **kwargs):
    profile = {
        "name": name,
        "details": kwargs,
        "fields": tuple(kwargs.keys())
    }
    return profile
name = input("Enter name: ")
n = int(input("Enter number of details: "))
details = {}
for i in range(n):
    key = input("Enter field name: ")
    value = input("Enter field value: ")
    details[key] = value
res = build_profile(name, **details)
print(res)