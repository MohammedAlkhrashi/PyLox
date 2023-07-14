import sys
from typing import List
def main():
    args = sys.argv
    if len(args) != 2:
        print("Usage: generate_ast <output_dir>")
        sys.exit(64)

    output_dir = args[1]
    write_path = f"{output_dir}/expr_generated.py"
    print(f"Writing to {write_path}")

    
    types = []
    types.append("Binary   : Expr left, Token operator, Expr right")
    types.append("Grouping : Expr expression")
    types.append("Literal  : Object value",)
    types.append("Unary    : Token operator, Expr right")
    define_ast(write_path, "Expr", types)
    


def define_ast(write_path, base_name, types: List[str]):

    with open(write_path, "w") as file:
        file.write("from abc import ABC\n")
        file.write("from PyLox.tokens import Token\n")
        file.write("\n")
        file.write(f"class {base_name}(ABC):"
                   "\n\t...\n")
        file.write("\n")

        file.write(f"class Visitor(ABC):\n")
        for type in types:
            type_name, fields_str = type.split(":")
            type_name = type_name.strip()
            file.write(f"\tdef visit_{type_name.lower()}(expr):"
                       "\n\t\t...\n")
            file.write("\n")
            


        for type in types:
            type_name, fields_str = type.split(":")
            type_name = type_name.strip()
            fields = fields_str.lstrip().split(",")
            formatted_fields = []
            for field in fields:
                type, name = field.lstrip().split(" ")
                formatted_fields.append(f"{name}: type")

            formatted_fields = ", ".join(formatted_fields)

            file.write("\n")
            file.write(f"class {type_name}({base_name}):\n")
            file.write(f"\tdef __init__(self, {formatted_fields}):\n")
            for field in fields:
                _, name = field.lstrip().split(" ")
                file.write(f"\t\tself.{name}  = {name}\n")

            file.write("\n")
            file.write(f"\tdef accept(self,visitor: Visitor):"
                       f"\n\t\treturn visitor.visit_{type_name.lower()}()")
            file.write("\n")


    
    
    
    
    
    


if __name__ == "__main__":
    main()