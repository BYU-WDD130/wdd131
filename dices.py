import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry
import random

def main():
    root = tk.Tk()
    root.option_add("*Font", "Helvetica 16")
    frm_main = Frame(root)
    frm_main.master.title("Dice Roller")
    frm_main.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    setup_main(frm_main)
    root.mainloop()  # should call root.mainloop(), not frm_main.mainloop()

def setup_main(frm):
    # --- Input fields ---
    lbl_sides = Label(frm, text="Enter the number of sides on the dice (2–20):")
    lbl_sides.grid(row=0, column=0, sticky="e", padx=5, pady=5)
    ent_sides = IntEntry(frm, width=3, lower_bound=2, upper_bound=20)
    ent_sides.grid(row=0, column=1, padx=5, pady=5)

    lbl_count = Label(frm, text="Enter the number of dice to roll (1–10):")
    lbl_count.grid(row=1, column=0, sticky="e", padx=5, pady=5)
    ent_count = IntEntry(frm, width=3, lower_bound=1, upper_bound=10)
    ent_count.grid(row=1, column=1, padx=5, pady=5)

    # --- Output label ---
    lbl_result = Label(frm, text="", wraplength=300, justify="left")
    lbl_result.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

    # --- Dice roll function ---
    def roll_dice(sides, count):
        total = 0
        rolls = []
        for _ in range(count):
            roll = random.randint(1, sides)
            total += roll
            rolls.append(str(roll))
        return f"Rolls: {', '.join(rolls)}\nTotal: {total}"

    # --- Button event handler ---
    def roll_action():
        try:
            sides = ent_sides.get()
        except ValueError:
            lbl_result.config(text="❌ You must enter a valid number of sides.")
            return

        try:
            count = ent_count.get()
        except ValueError:
            lbl_result.config(text="❌ You must enter a valid number of dice.")
            return

        # Only roll if both inputs are valid
        result_text = roll_dice(sides, count)
        lbl_result.config(text=result_text)

    # --- Roll Button ---
    btn_roll = Button(frm, text="🎲 Roll it!", command=roll_action)
    btn_roll.grid(row=2, column=0, columnspan=2, pady=10)

if __name__ == "__main__":
    main()