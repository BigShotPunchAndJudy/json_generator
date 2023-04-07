import tkinter as tk
import json

class JSONGenerator:
    def __init__(self):
        self.data = []

        self.root = tk.Tk()
        self.root.title("JSON Generator")

        # Create input fields and labels
        instruction_label = tk.Label(self.root, text="Instruction")
        instruction_label.grid(row=0, column=0)

        input_label = tk.Label(self.root, text="Input")
        input_label.grid(row=0, column=1)

        output_label = tk.Label(self.root, text="Output")
        output_label.grid(row=0, column=2)

        self.instruction_entry = tk.Text(self.root, height=4)
        self.instruction_entry.grid(row=1, column=0)

        self.input_entry = tk.Text(self.root, height=4)
        self.input_entry.grid(row=1, column=1)

        self.output_entry = tk.Text(self.root, height=4)
        self.output_entry.grid(row=1, column=2)

        # Create filename input field and label
        filename_label = tk.Label(self.root, text="Filename")
        filename_label.grid(row=2, column=0)

        self.filename_entry = tk.Entry(self.root)
        self.filename_entry.grid(row=3, column=0)

        # Create buttons
        add_button = tk.Button(self.root, text="Add", command=self.add_data)
        add_button.grid(row=2, column=1)

        generate_button = tk.Button(self.root, text="Generate", command=self.generate_json)
        generate_button.grid(row=3, column=1, columnspan=2)

    def add_data(self):
        data = {
            "instruction": self.instruction_entry.get("1.0", tk.END).strip(),
            "input": self.input_entry.get("1.0", tk.END).strip(),
            "output": self.output_entry.get("1.0", tk.END).strip()
        }
        self.data.append(data)

        # Clear input fields
        self.instruction_entry.delete("1.0", tk.END)
        self.input_entry.delete("1.0", tk.END)
        self.output_entry.delete("1.0", tk.END)

    def generate_json(self):
        filename = self.filename_entry.get()
        if not filename:
            filename = "data.json"

        with open(filename, "w") as f:
            json.dump(self.data, f, indent=4)

        self.root.destroy()

if __name__ == "__main__":
    app = JSONGenerator()
    app.root.mainloop()

