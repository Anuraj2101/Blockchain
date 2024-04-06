import tkinter as tk
import hashlib
from tkinter import messagebox
from voter import Voter
from candidate import Candidate
from block import Blockchain

def hash_data(data):
        hashed_data = hashlib.sha256(data.encode()).hexdigest()
        return hashed_data

def verify_voter(name, id):
    with open("utils/verified_voters.txt", "r") as f:
        lines = f.read().splitlines()
        for line in lines:
            filed_name, hashed_id = line.split(":")[0], line.split(":")[1]
            if name == filed_name and hash_data(id) == hashed_id:
                print("Found match, voter is verified...")
                return True
        else:
                print("Name and ID combination not found amongst verified voters list...")
                return False
        
def create_obj_array(entity_dict, entity_type):
    obj_lst = []
    for key in entity_dict:
        match entity_type:
            case "Voter":
                temp_voter = Voter(key)
                obj_lst.append(temp_voter)
            case "Candidate":
                temp_cand = Candidate(key, entity_dict[key])
                obj_lst.append(temp_cand)
    return obj_lst
     
class VotingSystemUI:
    def __init__(self, master, candidates, voters):
        self.master = master
        self.master.title("Voting System")
        self.master.geometry("400x400")
        self.candidates = create_obj_array(candidates, "Candidate")
        self.voters = create_obj_array(voters, "Voter")
        self.bc1 = Blockchain(self.voters, self.candidates)

        self.label = tk.Label(master, text="Welcome to Voting System", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.name_label = tk.Label(master, text="Enter your name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(master)
        self.name_entry.pack()

        self.id_label = tk.Label(master, text="Enter your Unique ID:")
        self.id_label.pack()
        self.id_entry = tk.Entry(master)
        self.id_entry.pack()

        self.vote_label = tk.Label(master, text="Select candidate to vote:")
        self.vote_label.pack()
        self.candidate_var = tk.StringVar(master)
        self.candidate_var.set("Select")
        self.candidate_menu = tk.OptionMenu(master, self.candidate_var, *list(candidates))
        self.candidate_menu.pack()

        self.vote_button = tk.Button(master, text="Vote", command=self.cast_vote)
        self.vote_button.pack(pady=10)

    def cast_vote(self):
        name = self.name_entry.get()
        id = self.id_entry.get()
        candidate_name = self.candidate_var.get()
        if not name:
            messagebox.showerror("Error", "Please enter your name.")
            return
        if not id:
            messagebox.showerror("Error", "Please enter your id.")
            return
        if candidate_name == "Select":
            messagebox.showerror("Error", "Please select a candidate.")
            return
        if not verify_voter(name, id):
            messagebox.showerror("Error", "Name and ID combination not among verified voters.")
            return
        voter = [vot for vot in self.voters if vot.get_voter_info()["Name"] == name][0]
        candidate = [cand for cand in self.candidates if cand.get_info()["Candidate Name"] == candidate_name][0]
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
