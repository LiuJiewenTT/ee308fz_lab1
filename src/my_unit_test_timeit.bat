@rem python -m timeit -n 10 -r 3 -s "import my_unit_test"
python -m timeit -n 10 -r 3 -s "import mainM" "mainM.mainfunc('../test/testfile.c')"