import tkinter as tk
from tkinter import messagebox
from voter import Voter
from candidate import Candidate
from block import Blockchain

class VotingSystemUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Voting System")
        self.master.geometry("400x300")

        self.bc1 = Blockchain()

        self.label = tk.Label(master, text="Welcome to Voting System", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.name_label = tk.Label(master, text="Enter your name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(master)
        self.name_entry.pack()

        self.vote_label = tk.Label(master, text="Select candidate to vote:")
        self.vote_label.pack()
        self.candidate_var = tk.StringVar(master)
        self.candidate_var.set("Select")
        self.candidate_menu = tk.OptionMenu(master, self.candidate_var, "Alice", "Bob", "Charlie")
        self.candidate_menu.pack()

        self.vote_button = tk.Button(master, text="Vote", command=self.cast_vote)
        self.vote_button.pack(pady=10)

    def cast_vote(self):
        name = self.name_entry.get()
        candidate_name = self.candidate_var.get()
        if not name:
            messagebox.showerror("Error", "Please enter your name.")
            return
        if candidate_name == "Select":
            messagebox.showerror("Error", "Please select a candidate.")
            return

        voter = Voter(name)
        candidate = Candidate(candidate_name, "Democratic")

        vote = voter.cast_vote(candidate)
        if vote.startswith("1 vote token transferred"):
            self.bc1.add_block(vote)
            messagebox.showinfo("Success", "Your vote has been cast successfully.")
            print("Blockchain Updated")
            print("Current Chain:")
            self.bc1.get_chain()
            print("Voter Wallet Balance:", voter.wallet.balance)
        else:
            messagebox.showerror("Error", vote)

if __name__ == "__main__":
    root = tk.Tk()
    app = VotingSystemUI(root)
    root.mainloop()
