# To compile this package with scram use
setup CMSSW7x
cd CMSSW/src
cmsenv
scram build -j8


# To compile a standalone executable use (alternative -stdlib=libc++)
clang++ `root-config --cflags --glibs` -std=c++11 -stdlib=libstdc++ bin/lheReader.cpp -o test/lheReader

# Usage with python run script
python runLHEreader.py output.root inputfolder

# Usage
lheReader -i [input_1.lhe] [input_2.lhe] -o [output.root] -r [run] -e [event] -l [lumi] -d [debug mode]

# To printout out input file names included in the output file execute on the ROOT commmand prompt
lheFileNames->Print()
