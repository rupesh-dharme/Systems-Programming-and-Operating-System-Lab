import sys

sys.stdin = open('asm.txt', 'r')
sys.stdout = open('Pass_01_output.txt', 'w')


class MNT:
    def __init__(self, name, mdtc):
        self.name = name
        self.mdtc = mdtc


class MDT:
    def __init__(self, command):
        self.command = command


class ALA:
    def __init__(self, param, default=None):
        self.param = param
        self.default = default


class MacroPassOne:
    def __init__(self):
        self.mnt = []
        self.mdt = []
        self.ala = []

    def read_input(self):
        instruction = input()
        flag = False
        curr_params = dict()
        while instruction != "END":
            if flag:
                command = ""
                i = 0
                while i < len(instruction):
                    if instruction[i] == "&":
                        i += 1
                        command += curr_params[f"&{instruction[i]}"]
                    else:
                        command += instruction[i]
                    i += 1
                self.mdt.append(MDT(command))
            if instruction == "MACRO":
                flag = True
                instruction = input()
                if " " in instruction:
                    x = instruction.split()
                    name, params = x[0], " ".join(x[1:])
                else:
                    name, params = instruction, ""
                i = 0
                name += " "
                while i < len(params):
                    if params[i] == "&":
                        name += f"#{len(self.ala)} "
                        i += 1
                        p = params[i]
                        v = ""
                        i += 1
                        curr_params[f"&{p}"] = f"#{len(self.ala)}"
                        if i < len(params) and params[i] == "=":
                            i += 1
                            while i < len(params) and params[i] != " ":
                                v += params[i]
                                i += 1
                            self.ala.append(ALA(p, v))
                        else:
                            self.ala.append(ALA(p))
                    i += 1
                self.mnt.append(MNT(name, len(self.mdt)))
            if instruction == "MEND":
                flag = False
                curr_params = dict()
            instruction = input()

    def display(self):
        print("MNT")
        print("i\tmdtc\tname")
        for i in range(len(self.mnt)):
            x = self.mnt[i]
            print(f"{i}\t{x.mdtc}\t\t{x.name}")
        print("MDT")
        print("i\tcommand")
        for i in range(len(self.mdt)):
            x = self.mdt[i]
            print(f"{i}\t{x.command}")
        print("ALA")
        print("i\tparam\tdefault")
        for i in range(len(self.ala)):
            x = self.ala[i]
            print(f"{i}\t{x.param}\t\t{x.default}")


mpo = MacroPassOne()
mpo.read_input()
mpo.display()
