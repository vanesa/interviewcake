"""

Flatten a Dictionary

A dictionary is a type of data structure that is supported natively in all major interpreted languages such as JavaScript, Python, Ruby and PHP, where it’s known as an Object, Dictionary, Hash and Array, respectively. In simple terms, a dictionary is a collection of unique keys and their values. The values can typically be of any primitive type (i.e an integer, boolean, double, string etc) or other dictionaries (dictionaries can be nested). However, for this exercise assume that values are either a string or another dictionary.

Given a dictionary dict, write a function flattenDictionary that returns a flattened version of it .

If you’re using a compiled language such Java, C++, C#, Swift and Go, you may want to use a Map/Dictionary/Hash Table that maps strings (keys) to a generic type (e.g. Object in Java, AnyObject in Swift etc.) to allow nested dictionaries.

Example:

input:  dict = {
            "Key1" : "1",
            "Key2" : {
                "a" : "2",
                "b" : "3",
                "c" : {
                    "d" : "3",
                    "e" : "1"
                }
            }
        }

output: {
            "Key1" : "1",
            "Key2.a" : "2",
            "Key2.b" : "3",
            "Key2.c.d" : "3",
            "Key2.c.e" : "1"
        }
Important: when you concatenate keys, make sure to add the dot character between them. For instance concatenating Key2, c and d the result key would be Key2.c.d.

Constraints:

[time limit] 5000ms
[input] Dictionary dict
[output] Dictionary
"""

"""
1) grab key and value
2) add to new dict
3) if value == dict
4) add this to the Keyname and get into the new dict
5) repeat until all key, value have been retrieved

"""

def flatten_dictionary(dict_):
  
  new_dict = {}
  
  for k, v in dict_.items():
    if isinstance(v, str):
      new_dict[k] = v
    else:
      new_dict = go_in_dict(k, v, new_dict)
  
  return new_dict

# value = dict()
def go_in_dict(keyname, value, new_dict):

  if isinstance(value, str):
    keyname = keyname.rstrip('.')
    print keyname
    new_dict[keyname] = value
    return new_dict
  
  v2 = value.keys()
  for key in v2:
    if keyname != "":
      keyname2 = keyname + "." + key
    else:
      keyname2 = keyname + key
    new_dict = go_in_dict(keyname2, value[key], new_dict)
  
  return new_dict



test_dict = {
            "Key1" : "1",
            "Key2" : {
                "a" : "2",
                "b" : "3",
                "c" : {
                    "d" : "3"
                }
            }
}
print(flatten_dictionary(test_dict))