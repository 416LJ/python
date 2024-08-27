def format_name(f_name,l_name):
    """Concatenates the first and last name into a single string"""
    return f_name+" "+l_name

def func(text):
    return text.title()

output = format_name(func("Laxsan","jEyas"))
print(output)
