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
        self.root.geometry("815x710")
        self.root.title("Shietcode")

        self.frame = customtkinter.CTkFrame(master=self.root)
        self.frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.button1 = customtkinter.CTkButton(
            master=self.frame, text="Get Data", command=self.runProgramThreaded
        )
        self.button1.grid(row=0, column=0, padx=8, pady=8)

        self.entry1 = customtkinter.CTkEntry(
            master=self.frame, placeholder_text="Riot ID"
        )
        self.entry1.grid(row=0, column=1, padx=8, pady=8)

        self.entry2 = customtkinter.CTkEntry(master=self.frame, placeholder_text="Tag")
        self.entry2.grid(row=0, column=2, padx=8, pady=8)

        self.combobox = customtkinter.CTkComboBox(
            master=self.frame,
            values=[],
            width=220,
            state="readonly",
        )
        self.combobox.grid(row=0, column=3, padx=8, pady=8)

        self.button2 = customtkinter.CTkButton(
            master=self.frame, width=75, text="Show", command=self.setTextboxText
        )
        self.button2.grid(row=0, column=4, padx=8, pady=8)

        self.textbox = customtkinter.CTkTextbox(master=self.frame, height=605)
        self.textbox.grid(row=1, column=0, columnspan=5, padx=8, pady=5, sticky="ew")

        self.progressbar = customtkinter.CTkProgressBar(
            master=self.frame,
            orientation="horizontal",
            mode="indeterminate",
        )

    def run(self):
        load_dotenv()

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        # Ordner anlegen, um Fehler zu vermeiden
        if os.path.isdir("./Data"):
            shutil.rmtree("./Data")
        os.mkdir("./Data")

        self.root.mainloop()

    def readJsonFile(self, jsonFile):
        with open("./Data/" + jsonFile, "r") as jsonFile:
            output = jsonFile.read()
        return output

    def setTextboxText(self):
        state = self.combobox.get()
        self.textbox.delete("0.0", "end")
        self.textbox.insert("0.0", self.readJsonFile(state))

    def getJsonFiles(self):
        jsonFileList = []
        data = os.listdir("./Data")
        for x in data:
            jsonFileList.append(x)
        return jsonFileList

    def runProgram(self):
        self.progressbar.grid(
            row=2, column=0, columnspan=5, padx=8, pady=8, sticky="we"
        )
        self.progressbar.start()

        summoner1 = Summoner.Summoner(name=self.getRiotId(), tag=self.getRiotTag())
        games1 = Games.Games()

        summoner1.getPuuid()
        summoner1.getId()
        summoner1.getRankedData()

        games1.getMatchHistory(summoner1)
        games1.getMatchHistoryData()

        self.getJsonFiles()
        self.combobox.configure(values=self.getJsonFiles())

        self.progressbar.stop()
        self.progressbar.pack_forget()

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
