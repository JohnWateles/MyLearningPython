import ast
import dis


with open("source_code.txt", "r") as file:
    source_code = file.read()

# Получение AST
parsed_code = ast.parse(source_code)
print(ast.dump(parsed_code, indent=4))

# Компиляция в байт-код и его вывод
compiled_code = compile(parsed_code, filename='<ast>', mode='exec')
dis.dis(compiled_code)
