🧠 Recursive Course-of-Action Planner

A file-based, recursive planning system designed to replace traditional to-do lists with structured decision trees.

Instead of managing flat tasks, this app lets you build branching courses of action, where every step can expand into its own detailed plan—stored as independent files.

---

🚀 Core Idea

This project treats planning like a recursive tree:

Goal → Strategy → Action → Sub-action → ...

Each node represents a course of action, not just a task.

- Every node is stored as its own file
- Nodes can branch infinitely
- You can navigate decisions like a filesystem

---

📦 Features

- 📁 One file per node (modular + versionable)
- 🌳 Infinite recursion depth
- 🧭 CLI navigation system
- 🔗 Parent-child relationships
- 🧠 Designed for strategy, not checklists

---

📂 Project Structure

action_tree/
│
├── root.json
├── node_a1b2c3d4.json
├── node_e5f6g7h8.json

Each file represents a single node in the decision tree.

---

🧾 Node Format

Each node is stored as JSON:

{
  "id": "node_a1b2c3d4",
  "title": "Build Prototype",
  "description": "Initial working version",
  "children": [
    "node_e5f6g7h8"
  ]
}

---

⚙️ Installation

1. Clone or Copy

git clone <your-repo>
cd <your-repo>

2. Run the App

python app.py

No external dependencies required.

---

🧭 Usage

When you start the app, you’ll be placed at the root node.

Menu Options

1. List children
2. Add child
3. Go to child
4. Back (not implemented)
5. Exit

---

➕ Add a Course of Action

Creates a new node and links it as a child of the current node.

---

🔍 Navigate

Move deeper into your plan by selecting child nodes.

Each node represents a refinement of intent.

---

🧠 Design Philosophy

❌ Traditional To-Do Lists

- Flat
- Linear
- No structure for reasoning

✅ Recursive Planning

- Hierarchical
- Expandable
- Reflects real decision-making

This system is closer to:

- Strategy trees
- AI planning graphs
- Quest systems in games

---

🔥 Use Cases

- 🎮 Game design (quest trees, branching narratives)
- 🧠 Strategic thinking / planning
- 🏗 Complex project breakdowns
- 🤖 AI decision modeling
- 🕵️ Investigation workflows

---

🧩 Future Enhancements

🔁 Navigation Stack

Track history to allow "back" functionality

---

📊 Node Scoring

Add attributes like:

"risk": 0.3,
"cost": 5,
"reward": 10

Then compute optimal paths.

---

🤖 AI Integration

- Suggest next steps
- Auto-expand plans
- Evaluate strategies

---

🌐 Visualization

- Graph view (nodes + edges)
- Tools:
  - React + D3
  - PyQt
  - Godot editor plugin

---

💾 Sync & Versioning

Because each node is a file:

- Git-friendly
- Easy merges
- Distributed planning systems possible

---

⚠️ Limitations

- No back navigation yet
- CLI only (no GUI)
- No validation of node integrity
- No concurrency handling

---

🛠 Development Notes

- Designed to be minimal and extensible
- Easy to port into:
  - Web apps
  - Game engines
  - Embedded systems (ESP32)

---

🧭 Philosophy Summary

«A plan is not a list.
It is a tree of decisions under uncertainty.»

---

📄 License

MIT (or your preferred license)

---

✍️ Author

Built as a foundation for recursive decision systems and strategic modeling.

---
