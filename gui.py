# -*- coding: cp1251 -*-
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import random
import matplotlib.pyplot as plt
from PIL import ImageTk, Image


def delete():
    output_text1.delete("0.0", tk.END)
    plt.cla()

def create():
    k_entry.delete(0, tk.END)
    k_entry.insert(0,0)
    global mypop
    global mystat
    global k
    k = 0
    mypop = [generate_individual() for i in range(int(chromoval_entry.get()))]
    mystat = []


def fitness3(x):
    func = combo.get()

    return (4 * (x[0] - 5) ** 2 + (x[1] - 6) ** 2)


def fitness(x):
    return (x[1] - x[0] ** 2) ** 2 + (1 - x[0]) ** 2


def generate_individual():
    individual = []
    minn = int(minn_entry.get())
    maxx = int(maxx_entry.get())
    individual.append(random.uniform(minn, maxx))
    individual.append(random.uniform(minn, maxx))
    return individual


def crossover(parent1, parent2):
    individual = []
    individual.append((parent1[0] + parent2[0]) / 2)
    individual.append((parent1[1] + parent2[1]) / 2)
    return individual


def mutate(individual):
    individual[0] += random.uniform(-1, 1)
    individual[1] += random.uniform(-1, 1)
    return individual


def main():
    global k
    k += int(generations_var.get())
    print(k)
    k_entry.delete(0, tk.END)
    k_entry.insert(0,k)
    for generation in range(int(generations_var.get())):
        # Evaluate fitness function
        fitness_scores = [fitness(individual) for individual in mypop]

        # Select parents
        parents = random.choices(mypop, weights=fitness_scores, k=2)

        # Create offspring
        offspring = crossover(parents[0], parents[1])
        mutpercent = int(mutant_entry.get()) / 100
        res = random.choices([1, 0], weights=[mutpercent, 1 - mutpercent])
        if True:
            offspring = mutate(offspring)

        # Replace worst individual in population with offspring
        worst_index = fitness_scores.index(max(fitness_scores))
        mypop[worst_index] = offspring
        best_individual = min(mypop, key=fitness)
        best_val = round(fitness(best_individual), 2)
        if best_val<4:
         mystat.append(best_val)

    plt.plot(range(1, len(mystat) + 1), mystat)
    plt.title("������ ����������� �������� �� ���-�� ���������")
    plt.xlabel("���������� ���������")
    plt.ylabel("������� ������-�������")
    plt.savefig("graph.png")
    output_text2.delete(1.0, tk.END)
    output_text2.insert(tk.END, "�����, ���������, ���1, ���2 \n")
    for i in range(len(fitness_scores)):
        line = "{} , {}, {}, {}".format(i, round(fitness_scores[i], 2), round(mypop[i][0], 2),
                                        round(mypop[i][1], 2)) + "\n"
        output_text2.insert(tk.END, line)

    # Get best individual
    best_individual = min(mypop, key=fitness)
    resx = "Minimum found: {}, {}".format(round(best_individual[0], 2), round(best_individual[1], 2))
    resy = "Minimum value: {}".format(round(fitness(best_individual), 2))
    output_text1.insert("1.0", resx + "\n")
    output_text1.insert("1.0", resy + "\n")
    output_text1.insert("1.0", "************************\n")


# Create the main window
root = tk.Tk()
root.title("������������ ��������")

# Set the size of the window
root.geometry("900x600")

# Create the left and right frames
left_frame = ttk.Frame(root, padding=10)
right_frame = ttk.LabelFrame(root, padding=10, text="��������� ���������")

# Divide the main window into two equal parts
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# Pack the left and right frames into the main window
left_frame.grid(row=0, column=0, sticky="nsew")
right_frame.grid(row=0, column=1, sticky="nsew")

# Create the child frames in the left frame
frame1 = ttk.LabelFrame(left_frame, padding=10, text="���������")
frame11 = ttk.LabelFrame(left_frame, padding=10, text="���������� �����")
frame2 = ttk.LabelFrame(left_frame, padding=10, text="����������")
frame3 = ttk.LabelFrame(left_frame, padding=10, text="����������")

# Pack the child frames into the left frame
frame1.pack(side="top", fill="x", padx=5, pady=5)
frame11.pack(side="top", fill="x", padx=5, pady=5)
frame2.pack(side="top", fill="x", padx=5, pady=5)
frame3.pack(side="top", fill="both", expand=True, padx=5, pady=5)

# Create the input widgets with captions in frame1
combo_label = ttk.Label(frame1, text="�������")
combo = ttk.Combobox(frame1, width="40")
combo['value'] = ("(x[1] - x[0]**2)**2 + (1 - x[0])**2",)
combo.current(0)  # ���������� ������� �� ���������

mutant_label = ttk.Label(frame1, text="����������� �������")
mutant_entry = ttk.Spinbox(frame1, from_=0, to=100)
mutant_entry.insert(0, "10")
chromoval_label = ttk.Label(frame1, text="���-�� ��������")
chromoval_entry = ttk.Spinbox(frame1, from_=0, to=10000)
chromoval_entry.insert(0, "50")
minn_label = ttk.Label(frame1, text="����������� �������� ����")
minn_entry = ttk.Spinbox(frame1, from_=-10000, to=10000)
minn_entry.insert(0, "-50")
maxx_label = ttk.Label(frame1, text="������������ �������� ����")
maxx_entry = ttk.Spinbox(frame1, from_=-10000, to=10000)
maxx_entry.insert(0, "50")
# Pack the input widgets with captions into frame1
combo_label.grid(row=0, column=0)
combo.grid(row=1, column=0)
mutant_label.grid(row=2, column=0, padx=0, pady=5)
mutant_entry.grid(row=2, column=1, padx=5, pady=5)

chromoval_label.grid(row=3, column=0, padx=0, pady=5)
chromoval_entry.grid(row=3, column=1, padx=5, pady=5)

minn_label.grid(row=4, column=0, padx=0, pady=5)
minn_entry.grid(row=4, column=1, padx=5, pady=5)

maxx_label.grid(row=5, column=0, padx=0, pady=5)
maxx_entry.grid(row=5, column=1, padx=5, pady=5)

# Create the Radio buttons and the calculate button in frame11
generations_var = tk.IntVar()
spin = ttk.Spinbox(frame11, from_=10, to=1000, width=10, textvariable=generations_var)
radio_button0 = ttk.Radiobutton(frame11, text="1", variable=generations_var, value=1)
radio_button1 = ttk.Radiobutton(frame11, text="10", variable=generations_var, value=10)
radio_button2 = ttk.Radiobutton(frame11, text="100", variable=generations_var, value=100)
radio_button3 = ttk.Radiobutton(frame11, text="500", variable=generations_var, value=500)
# Pack the Radio buttons and the calculate button into frame11
radio_button0.grid(row=0, column=0, padx=1, pady=5)
radio_button1.grid(row=0, column=1, padx=1, pady=5)
radio_button2.grid(row=0, column=2, padx=1, pady=5)
radio_button3.grid(row=0, column=3, padx=1, pady=5)
spin.grid(row=0, column=4, padx=5, pady=5)

# frame2
k = 0
create_button = ttk.Button(frame2, text="��������� ��������� ���������� �������", command=create)
calculate_button = ttk.Button(frame2, text="��������� ��� ����", command=main)
k_label = ttk.Label(frame2,text="����� ������:")
k_entry = ttk.Entry(frame2)
create_button.grid(row=2, column=0, padx=5, pady=5)
calculate_button.grid(row=2, column=1, padx=5, pady=5)
k_label.grid(row=3,column=0,padx=5, pady=5)
k_entry.grid(row=3,column=1,padx=5, pady=5)
output_text1 = ScrolledText(frame3, width=20, height=8)
output_text1.pack(side="top", fill="both", expand=True)
delbutton = ttk.Button(frame3, text="��������", command=delete)
delbutton.pack(side="bottom", fill="x")
# Create the text output widget in frame3
output_text2 = ScrolledText(right_frame, width=50, height=35)
output_text2.pack(side="left", fill="both", expand=True)
#image = Image.open("graph.png")
#img = ImageTk.PhotoImage(image)
#label = tk.Label(right_frame, image=img)
#label.pack(side="left", fill="both", expand=True)
################
mypop = []
mystat = []
generations_var.set(1)
################


root.mainloop()
