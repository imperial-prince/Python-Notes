#RULES FOR NAMING VARIABLES 
 
 
# ✅ Valid names (Start with letter, use lowercase, underscores, readable)
user_name = "prinss"         #  lowercase, descriptive, uses underscore
age = 18                     #  short but meaningful
is_logged_in = True          #  boolean prefixed with 'is_' – clean code convention
total_price_usd = 199.99     #  multi-word, descriptive
user2 = "admin"              #  can include numbers after letters
_name = "hidden"             #  valid – starts with underscore (used for internal/private use)
MAX_RETRIES = 5              #  constant – all uppercase (PEP8 convention for constants)

#---------------------------------------------------------------------------------------------------------

# ❌ INVALID or BAD PRACTICES (for clarity and safety)

# Starts with a number        #  SyntaxError
# 6user = "not allowed"       #  invalid: cannot start with a digit
# user-name = "dash"          #  invalid: dashes are not allowed
# full$name = "illegal"       #  invalid: symbols like $ not allowed
# class = "math"              #  invalid: 'class' is a reserved keyword in Python
# @fruit = "apple"            #  invalid: cannot start with @

list = [1, 2, 3]             #  bad: overwrites built-in 'list' – avoid shadowing built-ins
str = "text"                 #  bad: shadows 'str' – kills core functions like str()
x = 5                        #  bad: single-letter, unclear
data = [1, 2]                #  bad: too generic – what kind of data?

#---------------------------------------------------------------------------------------------------------

# ✅ Clean refactors of the above
product_list = ["phone", "laptop"]  #  better than 'list'
user_input_str = "yes"              #  descriptive type hint in name
items_count = 5                     #  replaces 'x'
customer_ids = [1, 2]               #  replaces generic 'data'





