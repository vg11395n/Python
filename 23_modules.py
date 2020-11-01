import converters
import utils
from ecommerce.shipping import calc_shipping, calc_tax

print(converters.kg_to_lbs(65))

print(converters.lbs_to_kg(143))

number = [120, 23, 45, 67, 89, 10]
print(utils.find_max(number))

print(calc_shipping())
print(calc_tax())
# Please note that when we use from syntax in import we don't need to be verbose to call out function in a module
# In above example we called calc_tax() directly instead shipping.calc_tax() syntax

# Another method of importing modules
# from converters import kg_to_lbs
# print(kg_to_lbs(143))









