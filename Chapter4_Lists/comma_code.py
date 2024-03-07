# Write your code here :-)
def comma_code(list):
    list_to_str = ""
    length = len(list)
    if length == 0:
        return list_to_str
    else:
        for i in range(length):
            if length == 2:
                list_to_str += list[i] + " and " + list[i+1]
                break
            elif i != length - 1:
                list_to_str += list[i] + ", "
            else:
                list_to_str +=  "and " + list[i]
    return list_to_str

print(comma_code(["pig", "fish"]))

print(comma_code(["Meg", "Brian", "Stewie", "Peter", "Louis", "Chris"]))

print(comma_code([]))
