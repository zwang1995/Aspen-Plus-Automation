# Created on 12 May 2022 by Zihao Wang, zwang@mpi-magdeburg.mpg.de


import os
import time
from win32com.client import GetObject, Dispatch
import numpy as np


class Aspen_Plus_Interface():
    def __init__(self):
        self.Application = Dispatch("Apwn.Document.38.0")
        # {"V10.0": "36.0", V11.0": "37.0", V12.0": "38.0"}
        print(self.Application)

    def load_bkp(self, bkp_file, visible_state=0, dialog_state=0):
        """
        Load a process via bkp file
        :param bkp_file: location of the Aspen Plus file
        :param visible_state: Aspen Plus user interface, 0 is invisible and 1 is visible
        :param dialog_state: Aspen Plus dialogs, 0 is not to suppress and 1 is to suppress
        """
        self.Application.InitFromArchive2(os.path.abspath(bkp_file))
        self.Application.Visible = visible_state
        self.Application.SuppressDialogs = dialog_state

    def re_initialization(self):
        # initial the chemical process in Aspen Plus
        self.Application.Reinit()

    def run_simulation(self):
        # run the process simulation
        self.Application.Engine.Run()

    def check_run_completion(self, time_limit=60):
        # check whether the simulation completed
        times = 0
        while self.Application.Engine.IsRunning == 1:
            time.sleep(1)
            times += 1
            if times >= time_limit:
                print("Violate time limitation")
                self.Application.Engine.Stop
                break

    def check_convergency(self):
        # check the simulation convergency by detecting errors in the history file
        runID = self.Application.Tree.FindNode("\Data\Results Summary\Run-Status\Output\RUNID").Value
        his_file = "../simulation/" + runID + ".his"
        with open(his_file, "r") as f:
            hasERROR = np.any(np.array([line.find("ERROR") for line in f.readlines()]) >= 0)
        return hasERROR

    def close_bkp(self):
        # close the Aspen Plus file
        self.Application.Quit()

    def collect_stream(self):
        # colloct all streams involved in the process
        streams = []
        node = self.Application.Tree.FindNode(r"\Data\Streams")
        for item in node.Elements:
            streams.append(item.Name)
        return tuple(streams)

    def collect_block(self):
        # colloct all blocks involved in the process
        blocks = []
        node = self.Application.Tree.FindNode(r"\Data\Blocks")
        for item in node.Elements:
            blocks.append(item.Name)
        return tuple(blocks)


def KillAspen():
    # kill the Aspen Plus
    WMI = GetObject("winmgmts:")
    for p in WMI.ExecQuery("select * from Win32_Process where Name='AspenPlus.exe'"):
        os.system("taskkill /pid " + str(p.ProcessId))


def SequenceWithEndPoint(start, stop, step):
    # generate evenly spaced values containing the end point
    return np.arange(start, stop + step, step)


def ListValue2Str(alist):
    # convert a list of mixed variables into string formats
    return list(map(str, alist))
