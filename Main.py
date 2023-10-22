import os
import shutil
import customtkinter
import threading
from dotenv import load_dotenv
import Summoner
import Games


class MyGUI:
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.geometry("225x175")
        self.root.title("Shietcode")

        self.frame = customtkinter.CTkFrame(master=self.root)
        self.frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.button1 = customtkinter.CTkButton(
            master=self.frame, text="Get Data", command=self.runProgramThreaded
        )
        self.button1.pack(padx=10, pady=10)

        self.entry1 = customtkinter.CTkEntry(
            master=self.frame, placeholder_text="Riot ID"
        )
        self.entry1.pack(padx=10, pady=5)

        self.entry2 = customtkinter.CTkEntry(master=self.frame, placeholder_text="Tag")
        self.entry2.pack(padx=10, pady=5)

        self.prorgessbar = customtkinter.CTkProgressBar(
            master=self.frame,
            orientation="horizontal",
            mode="indeterminate",
            height=8,
            width=160,
        )

    def run(self):
        load_dotenv()

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        # Ordner anlegen, um Fehler zu vermeiden
        if os.path.isdir("./Matches"):
            shutil.rmtree("./Matches")
        os.mkdir("./Matches")

        self.root.mainloop()

    def runProgram(self):
        self.prorgessbar.pack(padx=10, pady=10)
        self.prorgessbar.start()
        summoner1 = Summoner.Summoner(name=self.getRiotId(), tag=self.getRiotTag())
        games1 = Games.Games()

        summoner1.getPuuid()
        summoner1.getId()
        summoner1.getRankedData()

        games1.getMatchHistory(summoner1)
        games1.getMatchHistoryData()
        self.prorgessbar.stop()
        self.prorgessbar.pack_forget()

    def runProgramThreaded(self):
        threading.Thread(target=self.runProgram).start()

    def getRiotId(self):
        riotId = self.entry1.get()
        return riotId

    def getRiotTag(self):
        riotTag = self.entry2.get()
        return riotTag


if __name__ == "__main__":
    gui = MyGUI()
    gui.run()
