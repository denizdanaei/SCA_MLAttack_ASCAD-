# SCA_MLAttack_ASCAD

The assignment is to conduct a side-channel analysis of the ASCAD dataset.
Power measurements obtained from ATMEGA Boolean masked AES with a fixed key was considered. The dataset is available at [here](https://github.com/ANSSI-FR/ASCAD/tree/master/ATMEGA_AES_v1/ATM_AES_v1_fixed_key]).

When instruction followed in the `ReadMe.md` of the repository above, after downloading and extracting the project, there are four files available in folder `ASCAD_databases`, namely `ATMega8515_raw_traces.h5, ASCAD.h5, ASCAD_desync50.h5`, and `ASCAD_desync100.h5`.

The raw traces from `ATMega8515_raw_traces.h5`, was selected, which is an array of shape (60000,100000). The first 1000 points of interests was selected to observe the first round.

## How to run the program

``` python MLattack.py ```

or

``` python3 MLattack.py ```

Will run the profiling and attacking phases and prints a graph of different test sizes and their avr_GE

### needed libraries

`numpy`, `sklearn` `sympy` , `matplotlib.pyplot`

## Run from scratch

To start with different trace set or different points of interests, you should first execute `python extract.py`. Note that for this you will need to download the hash files from [here](https://github.com/ANSSI-FR/ASCAD/tree/master/ATMEGA_AES_v1/ATM_AES_v1_fixed_key]).

You can then use pearson correlation to decrease dimentionaliity as I did. You can execute `python featureSelection.py`, which will create another `npy` array from the trace set you give. There you can set which points of intrests you would like to take as well as how many features to keep after filtering.

Then run given command [above](#how-to-run-the-program)
