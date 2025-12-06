# import tkinter as tk
# from simulator import VirtualMemorySimulator

# class App:
#     def __init__(self, root):
#         self.sim = VirtualMemorySimulator()

#         root.title("Virtual Memory Simulator - Group C")

#         tk.Label(root, text="Enter Logical Address (0 - 8191):").pack(pady=5)

#         self.entry = tk.Entry(root, width=30)
#         self.entry.pack(pady=5)

#         tk.Button(root, text="Translate", command=self.translate).pack(pady=10)

#         self.output = tk.Text(root, height=15, width=60)
#         self.output.pack()

#     def translate(self):
#         try:
#             logical_address = int(self.entry.get())
#         except ValueError:
#             self.output.insert(tk.END, "Invalid Input: Enter a number\n\n")
#             return

#         physical, page, frame, status = self.sim.translate(logical_address)

#         text = f"Logical Address: {logical_address}\n"
#         text += f"Page Number: {page}\n"
#         text += f"Frame Number: {frame}\n"
#         text += f"Physical Address: {physical}\n"
#         text += f"Status: {status}\n"
#         text += "-" * 50 + "\n"

#         self.output.insert(tk.END, text)


# --------------------------------------------------------------------
# --------------------------------------------------------------------


import tkinter as tk
from tkinter import ttk
from simulator import VirtualMemorySimulator

class App:
    def __init__(self, root):
        self.sim = VirtualMemorySimulator()

        root.title("Virtual Memory Simulator - 721434768")

        # Main layout frames
        input_frame = tk.Frame(root)
        input_frame.pack(pady=10)

        table_frame = tk.Frame(root)
        table_frame.pack(pady=10)

        output_frame = tk.Frame(root)
        output_frame.pack(pady=10)

        # ---------------------------------
        # Input Section
        # ---------------------------------
        tk.Label(input_frame, text="Enter Logical Address (0 - 8191):").grid(row=0, column=0, padx=5)

        self.entry = tk.Entry(input_frame, width=25)
        self.entry.grid(row=0, column=1, padx=5)

        tk.Button(input_frame, text="Translate", width=15, command=self.translate).grid(row=0, column=2, padx=10)
        tk.Button(input_frame, text="Reset Simulation", width=15, command=self.reset).grid(row=0, column=3, padx=10)

        # ---------------------------------
        # Page Table
        # ---------------------------------
        tk.Label(table_frame, text="Page Table (Page to Frame)").grid(row=0, column=0)
        self.page_table_tree = ttk.Treeview(table_frame, columns=("page", "frame"), show='headings', height=8)
        self.page_table_tree.grid(row=1, column=0, padx=10)

        self.page_table_tree.heading("page", text="Page #")
        self.page_table_tree.heading("frame", text="Frame #")

        # ---------------------------------
        # Frame Table
        # ---------------------------------
        tk.Label(table_frame, text="Frame Table (Frame to Page)").grid(row=0, column=1)
        self.frame_table_tree = ttk.Treeview(table_frame, columns=("frame", "page"), show='headings', height=4)
        self.frame_table_tree.grid(row=1, column=1, padx=10)

        self.frame_table_tree.heading("frame", text="Frame #")
        self.frame_table_tree.heading("page", text="Page Loaded")

        # ---------------------------------
        # Output Window
        # ---------------------------------
        tk.Label(output_frame, text="Translation Output:").pack()

        self.output = tk.Text(output_frame, height=12, width=70)
        self.output.pack()

        # Highlight styles
        self.output.tag_config("fault", background="yellow")

        # Initially populate tables
        self.refresh_tables()

    # --------------------------------------------------------
    # Simulation Logic
    # --------------------------------------------------------
    def translate(self):
        try:
            logical_address = int(self.entry.get())
        except ValueError:
            self.output.insert(tk.END, "Invalid Input: Enter a number\n\n")
            return

        physical, page, frame, status = self.sim.translate(logical_address)

        text = f"Logical Address: {logical_address}\n"
        text += f"Page Number: {page}\n"
        text += f"Frame Number: {frame}\n"
        text += f"Physical Address: {physical}\n"
        text += f"Status: {status}\n"
        text += "-" * 50 + "\n"

        # Insert text
        if status is True:  # page fault
            self.output.insert(tk.END, text, "fault")
        else:
            self.output.insert(tk.END, text)

        # Refresh UI tables
        self.refresh_tables()

    # --------------------------------------------------------
    # Refresh UI tables
    # --------------------------------------------------------
    def refresh_tables(self):
        # clear old rows
        for row in self.page_table_tree.get_children():
            self.page_table_tree.delete(row)
        for row in self.frame_table_tree.get_children():
            self.frame_table_tree.delete(row)

        # Page Table with color coding
        for page_num, frame_num in enumerate(self.sim.page_table):
            row_id = self.page_table_tree.insert("", "end", values=(page_num, frame_num))

            if frame_num == -1:
                self.page_table_tree.item(row_id, tags=("notloaded",))
            else:
                self.page_table_tree.item(row_id, tags=("loaded",))

        self.page_table_tree.tag_configure("loaded", background="lightgreen")
        self.page_table_tree.tag_configure("notloaded", background="lightcoral")

        # Frame Table with colors
        for frame_num, page in enumerate(self.sim.frames):
            row_id = self.frame_table_tree.insert("", "end", values=(frame_num, page))

            if page is None:
                self.frame_table_tree.item(row_id, tags=("empty",))
            else:
                self.frame_table_tree.item(row_id, tags=("used",))

        self.frame_table_tree.tag_configure("used", background="lightskyblue")
        self.frame_table_tree.tag_configure("empty", background="lightgray")

    # --------------------------------------------------------
    # Reset Simulation
    # --------------------------------------------------------
    def reset(self):
        self.sim = VirtualMemorySimulator()
        self.output.delete(1.0, tk.END)
        self.refresh_tables()
        self.entry.delete(0, tk.END)

