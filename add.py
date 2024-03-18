import ast


def main():
    with open("func.py", "r") as f:
        source = f.read()
        return source


def rewrite():
    with open("func.py", "w") as f:
        f.write(ast.unparse(tree))


def check_func(tree, func_name):
    func_exists = False
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == func_name:
            func_exists = True
            to_remove = node
            break

    if func_exists and to_remove:
        return to_remove, func_exists
    else:
        return None, func_exists


def remove_func(tree, func_to_remove):
    to_remove, func_exists = check_func(tree, func_to_remove)
    if func_exists:
        parent_node = get_parent_node(tree)
        if parent_node and to_remove:
            parent_node.body.remove(to_remove)
            print(f"Function {func_to_remove}  is removed ")
    else:
        print(f"Function {func_to_remove} does not exist")


def get_parent_node(tree):
    for node in ast.walk(tree):
        if isinstance(node, ast.Module):
            return node


def create_func(tree, func_name, func_body):
    new_func = ast.parse(f"def {func_name}():\n{func_body}")
    if check_func(tree, func_name)[1]:
        remove_func(tree, func_name)
    tree.body.append(new_func)
    rewrite()


def converter():
    with open("func.py") as f:
        asm = []
        for line in f:
            if line.strip().startswith("movl") or line.strip().startwsith("addl"):
                asm.append(line.strip())
    print("\n".join(asm))


if __name__ == "__main__":
    tree = ast.parse(main())
    converter()
