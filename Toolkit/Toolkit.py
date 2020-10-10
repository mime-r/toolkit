#!/usr/bin/python
import glob, os, sys, time
from importlib import reload

class Toolkit:

    
    def __init__(self):
        print("[TOOLKIT] Alpha v1.0\nSimple Modular Code Framework for Python\nSamuel Cheng 2020\n----")

        #Preliminary: Scanning Directory
        self.u = utils()
        self.u.process("Scanning current directory...")
        self.pyfiles= [f for f in glob.glob("*.py")]
        if len(self.pyfiles) <= 1:
            self.u.warning("No other .py files in same dir.")
            self.u.tip("For this code to be helpful, please add more python files into the same directory as this file.")

            
    def start(self):
        self.u.process("Starting up envrionment...")

        print("\n"*100) #cls for idle
        os.system("cls")
        
        self.shell = "toolkit"
        self.ran = []
        
        self.mainloop()


    def mainloop(self):
        self.line = 1
        while True:
            self.shellconstructor = "[{0} {1}]\: ".format(self.shell,self.line)
            self.parse(input(self.shellconstructor))
            self.line += 1


    def parse(self, raw):
        lowered = raw.lower()
        self.exitcmd = ["#exit", "#e"]
        self.helpcmd = ["#help", "#h"]
        self.listfilescmd = ["#listfiles"]
        
        if lowered in self.exitcmd:
            self.u.process("exiting...")
            sys.exit(0)
        elif lowered in self.helpcmd:
            self.help()
        elif lowered in self.listfilescmd:
            self.listfiles()
        else:
            if not raw.endswith(".py"):
                raw += ".py"
            if raw in self.pyfiles:

                
                self.u.process("Running [{0}] ({1}).\n----[output starts on next line]----".format(raw, os.path.dirname(os.path.realpath(__file__)) + '\\' + raw))

                print("\n"*100) #cls for idle
                os.system("cls")
        
                if raw in self.ran:
                    starttime = time.time()
                    reload(self.runinstance)
                    self.u.info("Time elapsed: {} seconds.".format(time.time() - starttime))
                else:
                    self.ran.append(raw)
                    starttime = time.time()
                    self.runinstance = __import__(str(raw[:-3]))
                    self.u.info("Time elapsed: {} seconds.".format(time.time() - starttime))
            else:
                self.u.warning("File not found, entering search mode.")

                self.correctedpyfiles = []
                if not lowered.endswith(".py"):
                    lowered += ".py"
                for filename in self.pyfiles:
                    self.correctedpyfiles.append([filename.lower(), filename])

                self.found = False
                for element in self.correctedpyfiles:
                    
                    if element[0] == lowered:
                        self.u.tip("Did you mean \"{filename}\"?".format(filename = element[1]))
                        self.found = True
                if not self.found:
                    self.u.critical("Search did not return any matches.", 0)
                    self.u.tip("Type in \"#help\" for help, or \"#listfiles\" to list files in this file's directory.")


    def listfiles(self):
        self.listfilesline = 1
        for element in self.pyfiles:
            print("{0}: {1}".format(self.listfilesline, element))


    def help(self, *args):
        self.u.help("Type in {0} to exit.".format(self.exitcmd))
        self.u.help("Type in {0} for help.".format(self.helpcmd))
        self.u.help("Type in {0} to list all files in this directory.".format(self.listfilescmd))

            
            


class utils:

    
    def warning(self, msg):
        print("[Warning] {}".format(msg))

        
    def help(self, msg):
        print("[Help] {}".format(msg))

        
    def process(self, msg):
        print("[Process] {}".format(msg))

        
    def tip(self, msg):
        print("[Tip] {}".format(msg))

        
    def info(self, msg):
        print("[Info] {}".format(msg))

        
    def critical(self, msg, state):
        print("[Critical] {}".format(msg))
        if state == 1:
            sys.exit(-1)

if __name__ == "__main__":
    t = Toolkit()
    t.start()
else:
    print("\nThis code \"Toolkit.py\" is not to be called from this code or from another code. Please run this code separately.\n")
