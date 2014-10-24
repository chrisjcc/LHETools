# To compile this package with scram use
setup CMSSW7x
cd CMSSW/src
cmsenv
scram build -j8


# To compile a standalone executable use (alternative -stdlib=libc++)
clang++ `root-config --cflags --glibs` -std=c++11 -stdlib=libstdc++ bin/lheReader.cpp -o test/lheReader

# Usage with python run script
python runLHEreader.py output.root inputfolder

# Usage standalone (very important -i before EACH input file):
lheReader -i [input_1.lhe] -i [input_2.lhe] -o [output.root] -r [run] -e [event] -l [lumi] -d [debug mode]

