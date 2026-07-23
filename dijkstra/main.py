from tkinter import ttk, messagebox

import tkinter as tk

import dijkestra
import bellmanford
import Graph



adj_list = {
    'A': [Graph.Edge(1.8, 'B'), Graph.Edge(1.5, 'C'), Graph.Edge(1.4, 'D')],
    'B': [Graph.Edge(1.8, 'A'), Graph.Edge(1.6, 'E')],
   'C': [Graph.Edge(1.5, 'A'), Graph.Edge(1.8, 'E'), Graph.Edge(2.1, 'F')],
    'D': [Graph.Edge(1.4, 'A'), Graph.Edge(2.7, 'F'), Graph.Edge(2.4, 'G')],
    'E': [Graph.Edge(1.6, 'B'), Graph.Edge(1.8, 'C'), Graph.Edge(1.4, 'F'), Graph.Edge(3.4, 'H')],
    'F': [Graph.Edge(2.1, 'C'), Graph.Edge(2.7, 'D'), Graph.Edge(1.4, 'E'), Graph.Edge(1.3, 'G'), Graph.Edge(2.9, 'H')],
    'G': [Graph.Edge(2.4, 'D'), Graph.Edge(1.3, 'F'), Graph.Edge(1.5, 'H')],
    'H': [Graph.Edge(3.4, 'E'), Graph.Edge(2.9, 'F'), Graph.Edge(1.5, 'G')],
}

g = Graph.Graph(adj_list)
root = tk.Tk()
root.title("Campus GPS Navigation")
root.geometry("600x500")
root.configure(bg="#F4F6F8")

title = tk.Label(
    root,
    text="Graph Navigation System",
    font=("Arial", 20, "bold"),
    bg="#F4F6F8",
    fg="#003366"
)
title.pack(pady=20)

# ----------------------------
# Frame
# ----------------------------

frame = tk.Frame(root, bg="#F4F6F8")
frame.pack()

locations = list(adj_list.keys())

tk.Label(frame, text="Starting Location",
         bg="#F4F6F8",
         font=("Arial",12)).grid(row=0,column=0,pady=10,padx=10)

start_box = ttk.Combobox(frame,width=25,values=locations,state="readonly")
start_box.grid(row=0,column=1)
start_box.current(0)

tk.Label(frame,
         text="Destination",
         bg="#F4F6F8",
         font=("Arial",12)).grid(row=1,column=0,pady=10)

end_box = ttk.Combobox(frame,width=25,values=locations,state="readonly")
end_box.grid(row=1,column=1)
end_box.current(1)

# ----------------------------
# Output
# ----------------------------

output = tk.Text(
    root,
    width=60,
    height=12,
    font=("Consolas",11)
)

output.pack(pady=20)

# ----------------------------
# Find Route
# ----------------------------

def find_route():

    start = start_box.get()
    end = end_box.get()

    if start == end:
        messagebox.showwarning("Warning",
                               "Please choose different locations.")
        return

    distance, path = dijkestra.dijkstra(g,start,end)

    output.delete(1.0,tk.END)

    if path:

        output.insert(tk.END,"Shortest Route\n")
        output.insert(tk.END,"========================\n\n")

        for i,node in enumerate(path):

            output.insert(tk.END,node)

            if i != len(path)-1:
                output.insert(tk.END,"\n   ↓\n")

        output.insert(tk.END,"\n\n")
        output.insert(tk.END,
                      f"Total Distance : {distance:.1f} km")

    else:

        output.insert(tk.END,"No route found.")

# ----------------------------
# Button
# ----------------------------

button = tk.Button(
    root,
    text="Find Shortest Route",
    command=find_route,
    bg="#0066CC",
    fg="white",
    font=("Arial",12,"bold"),
    width=22,
    height=2
)

button.pack()

root.mainloop()