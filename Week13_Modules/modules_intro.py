# Standard Module
# import random

# External Module --> Need to be installed first
# import pandas
# import find_index_module as fim
# import pandas as pd --> wherever possible stick to conventions
# Ex: pandas is always aliased as pd

# TO import only specific things
from find_index_module import find_index as fi
req_idx = fi(["apple", "oranges", "kiwi", "mango"], "mango")
print(req_idx)
# print(test_var)
print("Running modules intro: ", __name__)
