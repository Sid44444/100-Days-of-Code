#title case = Angela Yu
def format_name(first_name, last_name):
    print(first_name.title())
    print(last_name.title())

format_name("anGeLa", "SMITH")

def format_name_again(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name =(l_name.title())
    return f"{formatted_f_name} {formatted_l_name}"
print (format_name_again("anGEla", "YU"))
