# =====================================================
# CLEAN CODE BEST PRACTICES – PYTHON OPERATORS
# =====================================================

# 1. Use parentheses to clarify precedence
# ----------------------------------------
# BAD – hard to read, can cause bugs due to hidden precedence
result = a + b * c - d / e

# GOOD – explicitly group logic for clarity
result = (a + (b * c)) - (d / e)

# 2. Avoid chaining assignments unless necessary
# ----------------------------------------------
# BAD – hides intent and makes state changes unclear
x = y = z = 0

# GOOD – declare clearly and separately
x = 0
y = 0
z = 0

# 3. Never compare booleans to True/False
# ---------------------------------------
is_admin = True

# BAD
if is_admin == True:
    ...

# GOOD
if is_admin:
    ...

# 4. Use 'is' only for identity comparisons (like None)
# -----------------------------------------------------
# BAD – can behave incorrectly for value checks
if x is 5:
    ...

# GOOD – use '==' for value, 'is' for identity
if x == 5:
    ...
if x is None:
    ...

# 5. Name your operands meaningfully
# ----------------------------------
# BAD – unclear intent
if a + b > c:
    ...

# GOOD – self-explaining logic
if base_salary + bonus > total_cost:
    ...

# 6. Don’t abuse shorthand assignment (+=, -=, etc.)
# --------------------------------------------------
# BAD – careless mutation
cart_total += discount - tax * rate + 7

# GOOD – break into steps with intention
cart_total += discount
cart_total -= tax * rate
cart_total += 7

# 7. Avoid bitwise operators unless working with binary-level data
# ----------------------------------------------------------------
# BAD – confusing in high-level business logic
if user_flags & 0b1000:
    ...

# GOOD – encapsulate in function or use enums/constants
def has_permission(flag):
    return flag & 0b1000 != 0














