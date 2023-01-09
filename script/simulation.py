# Created at 08 Jun 2022 by Zihao Wang, zwang@mpi-magdeburg.mpg.de

import itertools
from aspen_utils import *


def run_Simulation(combine_loop, txt_file):
    """
    run process simulations under different configurations
    :param combine_loop: the matrix of operating variables with a shape of [n_conf, n_var]
        n_conf is the number of operating configurations to be simulated
        n_var is the operating variables (to be varied) in consideration
    :param txt_file: the file for data storage
    """
    with open(txt_file, "w") as f:
        f.write(" ".join(["Index",
                          "NStage", "RR", "StoF",
                          "DIST_C4H8", "RebDuty", "hasERROR",
                          "TimeCost",
                          "\n"]))

    # load Aspen Plus file
    Aspen_Plus = Aspen_Plus_Interface()
    Aspen_Plus.load_bkp(r"../simulation/ExtractiveDistillation.bkp", 0, 1)
    time.sleep(2)

    FeedRate = 500

    print("Start simulation ...")
    TotalTimeStart = time.time()
    Output_array = []
    for run_Index, Input in enumerate(combine_loop):
        TimeStart = time.time()
        Aspen_Plus.re_initialization()

        # assign values to each operating variable
        Input = list(Input)
        NStage, RR, StoF = Input
        NStage = int(NStage)
        Input = [NStage, RR, StoF]
        print("#", run_Index, "-", Input)
        Aspen_Plus.Application.Tree.FindNode(r"\Data\Blocks\ED\Input\NSTAGE").Value = NStage
        Aspen_Plus.Application.Tree.FindNode(r"\Data\Blocks\ED\Input\BASIS_RR").Value = RR
        Aspen_Plus.Application.Tree.FindNode(r"\Data\Streams\SOLVENT\Input\TOTFLOW\MIXED").Value = StoF * FeedRate
        Aspen_Plus.Application.Tree.FindNode(r"\Data\Blocks\ED\Input\FEED_STAGE\FEED").Value = np.ceil(0.5 * NStage)
        # the mixture is fed in the middle of the column

        # run the process simulation
        Aspen_Plus.run_simulation()
        Aspen_Plus.check_run_completion()

        # collect results
        DIST_C4H8 = Aspen_Plus.Application.Tree.FindNode(r"\Data\Streams\DIST1\Output\MOLEFRAC\MIXED\C4H8").Value
        RebDuty = Aspen_Plus.Application.Tree.FindNode(r"\Data\Blocks\ED\Output\REB_DUTY").Value
        hasERROR = Aspen_Plus.check_convergency()
        Output = [DIST_C4H8, RebDuty, hasERROR]
        print(Output)
        Output_array.append(Output)

        TimeEnd = time.time()
        TimeCost = TimeEnd - TimeStart

        with open(txt_file, "a") as f:
            f.write(" ".join(ListValue2Str([run_Index]) +
                             ListValue2Str(Input) +
                             ListValue2Str(Output) +
                             ListValue2Str([TimeCost]) +
                             ["\n"]))

    print("\nTerminate simulation ...")
    TotalTimeEnd = time.time()
    print(f"Simulation time:{TotalTimeEnd - TotalTimeStart: .2f} s")
    Aspen_Plus.close_bkp()


def main():
    # generate a set of operating configurations
    NStage_list = SequenceWithEndPoint(50, 50, 5)  # the number of stage of the column
    RR_list = SequenceWithEndPoint(1, 10, 1)  # the reflux ratio of the column
    StoF_list = SequenceWithEndPoint(1, 8, 1)  # the ratio of solvent flow rate to feed flow rate
    combine_loop = list(itertools.product(NStage_list, RR_list, StoF_list))

    total_run = len(combine_loop)
    print(f"Number of operating configurations: {total_run}")

    txt_file = "../DistillColumn.txt"  # the file for data storage

    run_Simulation(combine_loop, txt_file)

    KillAspen()


if __name__ == "__main__":
    main()
