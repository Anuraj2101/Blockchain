from gui import VotingSystemUI as GUI
import tkinter as tk

def pull_entity(entity_type):
    entity_dict={}
    file_path = ""
    match entity_type:
        case "Voter":
            file_path = "utils/verified_voters.txt"
        case "Candidate":
            file_path = "utils/verified_candidates.txt"
    with open(file_path, "r") as f:
        lines = f.read().splitlines()
        for line in lines:
            entity_dict[line.split(":")[0]] = line.split(":")[1]
    
    return entity_dict


if __name__ == "__main__":

    cand_dict = pull_entity("Candidate")
    voter_dict = pull_entity("Voter")
    root = tk.Tk()
    app = GUI(root, cand_dict, voter_dict)
    root.mainloop()