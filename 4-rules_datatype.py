# CLEAN CODE RULES: DATA TYPES IN PYTHON
# --------------------------------------------

# RULE 1: Always use type hints for clarity and safety.
# --------------------------------------------

# BAD: No type hints, unclear intent
# name = "prinss"

# GOOD: With type hint
user_name: str = "prinss"


# RULE 2: Use descriptive variable names based on type and meaning.
# --------------------------------------------

# BAD: Vague and short
# a = 18

# GOOD: Descriptive and typed
user_age: int = 18


# RULE 3: Prefer immutable types for safety when mutation is not needed.
# --------------------------------------------

# GOOD: Tuple is immutable and safe for fixed coordinates
coordinates: tuple[float, float] = (12.4, 78.2)

# BAD: Using list when mutation isn't required (may introduce bugs)
# coordinates = [12.4, 78.2]


# RULE 4: Use the right container for the right task.
# --------------------------------------------

# Use list for ordered, mutable sequences
shopping_cart: list[str] = ["apple", "banana"]

# Use set for unique, unordered values
unique_tags: set[str] = {"python", "linux", "security"}

# Use dict for structured key-value mappings
user_profile: dict[str, str | int] = {
    "name": "Prinss",
    "age": 18
}


# RULE 5: Never use mutable objects as default arguments in functions.
# --------------------------------------------

# BAD: Dangerous — shared state between function calls
# def add_item(item, cart=[]):
#     cart.append(item)
#     return cart

# GOOD: Safe pattern
def add_item(item: str, cart: list[str] | None = None) -> list[str]:
    """
    Add an item to a shopping cart. Initializes new cart if None.
    """
    if cart is None:
        cart = []
    cart.append(item)
    return cart


# RULE 6: Avoid shadowing built-in type names.
# --------------------------------------------

# BAD: Overwrites built-in type
# list = [1, 2, 3]

# GOOD: Use descriptive name
task_list: list[int] = [1, 2, 3]


# RULE 7: Always cast input data to correct type explicitly.
# --------------------------------------------

# BAD: Trusting input data blindly
# age = input("Enter your age: ")

# GOOD: Safe explicit casting
raw_age: str = input("Enter your age: ")
try:
    user_age: int = int(raw_age)
except ValueError:
    print("Invalid age input.")


# RULE 8: Avoid over-nesting complex dicts — use data models if needed.
# --------------------------------------------

# BAD: Deep nesting
# user = {"profile": {"details": {"name": "prinss"}}}

# GOOD: Flatten or model when depth increases
user_name: str = "prinss"
user_country: str = "India"


# RULE 9: Choose correct numeric type — int vs float
# --------------------------------------------

# Use int for counting
retry_count: int = 3

# Use float for measurements or prices
product_price: float = 129.99


# RULE 10: Use None and Optional carefully with type safety
# --------------------------------------------

# Example: a user may or may not have a middle name
from typing import Optional

middle_name: Optional[str] = None

# Safe conditional usage
if middle_name is not None:
    print(middle_name.upper())


# RULE 11: Don’t mix unrelated types in a single container unless needed.
# --------------------------------------------

# BAD: Ambiguous, hard to type-check
# mixed_data = ["hello", 123, True]

# GOOD: Keep it type-specific unless explicitly polymorphic
log_messages: list[str] = ["Started...", "Connecting..."]


# RULE 12: Declare constants with ALL_CAPS and correct types
# --------------------------------------------

MAX_CONNECTIONS: int = 10
PI: float = 3.14159


# RULE 13: Use isinstance() to validate type where needed
# --------------------------------------------

def is_valid_age(age: int | str) -> bool:
    """
    Validate if input can be accepted as an age.
    """
    if isinstance(age, int):
        return age > 0
    elif isinstance(age, str) and age.isdigit():
        return int(age) > 0
    return False


# RULE 14: Document container types with generics (Python 3.9+ syntax)
# --------------------------------------------

# BAD:
# items = []

# GOOD:
items: list[str] = ["python", "hacking"]


# RULE 15: Use data types that express intent and behavior
# --------------------------------------------

# GOOD:
from datetime import datetime

start_time: datetime = datetime.now()
