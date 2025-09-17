
#! SECURITY RISK: User input is not sanitized            -   Alert 
#? Should we move this block into a separate function?   -   Doubt
#// Deprecated logic — kept for legacy compatibility     -   Dead code
# TODO : Add exception handling for file errors          -   Task
#* Validate input before processing further              -   Highlight 
# NOTE : .....................                           -   Some note



# ============================================
# RULE 1: COMMENTS ARE A LAST RESORT
# Write code that is self-explanatory. Avoid comments when naming and structure can make intent clear.
# Reference: Clean Code in Python – Chapter 1
# ============================================

# BAD: Comment describes what code does (redundant)
# In this case, rename variable instead
counter = 0
# Increase counter by 1
counter += 1  # Unnecessary comment

# BETTER: Code tells the story without comment
user_attempts = 0
user_attempts += 1  # No comment needed, name explains intent


# ============================================
# RULE 2: PREFER DOCSTRINGS FOR DOCUMENTATION
# Use triple-quoted strings for documenting functions, classes, and modules — not comments
# Use one-liners or multi-line docstrings as needed
# ============================================

#  BAD: Using comment instead of docstring
# def add(a, b):
#     # This function adds two numbers
#     return a + b

#  GOOD: Using a docstring to document the intent
def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


# ============================================
# RULE 3: USE COMMENTS TO EXPLAIN WHY, NOT WHAT
# Use comments ONLY to explain intent, reasoning, or external context — not mechanics
# ============================================

# ❌ BAD: Comment explains the "what"
def square(x: int) -> int:
    # Return square of x
    return x * x  # ❌ This is obvious, don't comment

# ✅ GOOD: Comment explains "why" a non-obvious choice is made
def retry_connection():
    """
    Attempt to reconnect to the server.
    Includes delay due to rate-limiting constraints.
    """
    import time
    # WHY: Server enforces a 2-second delay between retries
    time.sleep(2)
    print("Reconnecting...")

retry_connection()


# ============================================
# RULE 4: USE TODO COMMENTS SPARINGLY & RESPONSIBLY
# Mark places for improvements, bugfixes, or temporary code using 'TODO', but never leave them unmanaged
# Include context: who/when/why
# ============================================

# ✅ GOOD: Actionable TODO with details
# TODO [prinss][2025-07-20]: Remove fallback when API v2 is deployed
def legacy_fallback():
    return "Using legacy auth"


# ============================================
# RULE 5: DO NOT COMMENT BAD CODE — REFACTOR IT
# If your code needs a comment, refactor it into a clearly named function
# ============================================

# ❌ BAD: Comment used to explain a cryptic block
# Calculate total after applying 10% tax
# t = p + (p * 0.1)

# ✅ GOOD: Encapsulate in a self-explanatory function
def calculate_total_with_tax(price: float) -> float:
    """Return total price after adding 10% tax."""
    return price + (price * 0.1)

# USAGE:
final_price = calculate_total_with_tax(100)
print(final_price)  # 110.0


# ============================================
# RULE 6: COMMENT BLOCKS SHOULD NOT SUBSTITUTE CLARITY
# Avoid comment-heavy procedural code. Use modular design instead.
# ============================================

# ❌ BAD: Procedural block with too many comments
# Step 1: Get input
# Step 2: Validate input
# Step 3: Print greeting
# name = input("Enter your name: ")
# if name:
#     print(f"Hello, {name}")

# ✅ GOOD: Break into named functions
def get_user_name() -> str:
    """Prompt user and return the name."""
    return input("Enter your name: ")

def greet(name: str) -> None:
    """Greet the user by name."""
    if name:
        print(f"Hello, {name.title()}")

greet(get_user_name())


# ============================================
# RULE 7: COMMENT ROT IS REAL — DELETE STALE COMMENTS
# Comments must be updated when code changes; otherwise, delete them
# ============================================

# ❌ BAD: Comment no longer matches code
# Calls old API endpoint
def fetch_data():
    # Fetch from /api/v1
    return "New endpoint response"  # But comment says /v1

# ✅ FIX: Remove or update incorrect comment immediately


# ============================================
# RULE 8: NEVER COMMENT OUT DEAD CODE — REMOVE IT
# If it’s unnecessary, delete it. Version control tracks everything.
# ============================================

# ❌ BAD:
# def old_login():
#     return "Legacy"

# ✅ Just delete it. Don’t pollute the codebase.


# ============================================
# RULE 9: USE INLINE COMMENTS ONLY IF ABSOLUTELY NECESSARY
# Place short comments at the end of the line, separated by two spaces
# Only when explaining rare logic
# ============================================

threshold = 0.85  # Minimum confidence score for model output




