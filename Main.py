import os
import json
import uuid

DATA_DIR = "action_tree"

def ensure_data_dir():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def node_path(node_id):
    return os.path.join(DATA_DIR, f"{node_id}.json")

def create_node(title, description=""):
    node_id = f"node_{uuid.uuid4().hex[:8]}"
    node = {
        "id": node_id,
        "title": title,
        "description": description,
        "children": []
    }
    with open(node_path(node_id), "w") as f:
        json.dump(node, f, indent=2)
    return node_id

def load_node(node_id):
    with open(node_path(node_id), "r") as f:
        return json.load(f)

def save_node(node):
    with open(node_path(node["id"]), "w") as f:
        json.dump(node, f, indent=2)

def init_root():
    root_path = node_path("root")
    if not os.path.exists(root_path):
        root = {
            "id": "root",
            "title": "Root Goal",
            "description": "Top level objective",
            "children": []
        }
        save_node(root)

def add_child(parent_id, title, description=""):
    parent = load_node(parent_id)
    child_id = create_node(title, description)
    parent["children"].append(child_id)
    save_node(parent)
    print(f"Added child {child_id} to {parent_id}")

def list_children(node_id):
    node = load_node(node_id)
    print(f"\n[{node['title']}]")
    for i, child_id in enumerate(node["children"]):
        child = load_node(child_id)
        print(f"{i+1}. {child['title']} ({child_id})")

def navigate():
    current = "root"

    while True:
        node = load_node(current)
        print(f"\n=== {node['title']} ===")
        print(node["description"])
        print("\nOptions:")
        print("1. List children")
        print("2. Add child")
        print("3. Go to child")
        print("4. Back (not implemented stack)")
        print("5. Exit")

        choice = input("> ")

        if choice == "1":
            list_children(current)

        elif choice == "2":
            title = input("Title: ")
            desc = input("Description: ")
            add_child(current, title, desc)

        elif choice == "3":
            list_children(current)
            idx = int(input("Enter number: ")) - 1
            children = load_node(current)["children"]
            if 0 <= idx < len(children):
                current = children[idx]
            else:
                print("Invalid selection")

        elif choice == "5":
            break

def main():
    ensure_data_dir()
    init_root()
    navigate()

if __name__ == "__main__":
    main()
