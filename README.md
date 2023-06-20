# Spike-Cache-Analysis
Efficiancy analysis counting miss rate on data cache using a high memory access rate application

## Spike Installation Guide

## Prerequisites

Before you begin, ensure that you have the following prerequisites:

- Ubuntu or a compatible Linux distribution, for this project was used Ubuntu 20.04 in wsl2
- Git (for cloning the Spike repository)

## Step 1: Clone the Spike Repository

1. Open a terminal window.

2. Navigate to the directory where you want to clone the Spike repository.

3. Install the device-tree-compiler
    ```sh
    $ apt-get install device-tree-compiler
  
4. Run the following command to clone the repository and enter the newly created repository:
   ```sh
   $ git clone https://github.com/riscv/riscv-isa-sim.git
   $ cd riscv-isa-sim

5. Set your variable $RISCV to the PATH where you want the installation, for example:
   ```sh
   $ export $RISCV="/path/to/desired/location"
   
6. Run the following commands:
   ```sh
    $ mkdir build
    $ cd build
    $ ../configure --prefix=$RISCV
    $ make
    $ [sudo] make install

## Step 2: Clone the RISC-V GNU Toolchain Repository

1. Open a terminal window.

2. Navigate to the directory where you want to clone the RISC-V GNU toolchain repository.

3. Install the basic packages necessary to the GNU toolchain execution (following command is for Ubuntu, refer to https://github.com/riscv-collab/riscv-gnu-toolchain for correct packges for your linux distribution
    ```sh
    $ sudo apt-get install autoconf automake autotools-dev curl python3 python3-pip libmpc-dev libmpfr-dev libgmp-dev gawk build-essential bison flex texinfo gperf libtool patchutils bc zlib1g-dev libexpat-dev ninja-build git cmake libglib2.0-dev
  
4. Run the following command to clone the repository and enter the newly created repository:
   ```sh
   $ git clone https://github.com/riscv/riscv-gnu-toolchain
   $ cd riscv-gnu-toolchain
   
5. Set your variable $RISCV to the PATH where you want the installation, for example (use the same as your spike installation):
   ```sh
   $ export $RISCV="/path/to/desired/location"
   
6. Run the following commands:
   ```sh
    $ ./configure --prefix=$RISCV
    $ make

## Step 3: Clone RISC-V PK Repository

1. Open a terminal window.

2. Navigate to the directory where you want to clone the RISC-V pk repository.
  
3. Run the following command to clone the repository and enter the newly created repository:
   ```sh
   $ git clone https://github.com/riscv-software-src/riscv-pk
   $ cd riscv-pk
   
4. Set your variable $RISCV to the PATH where you want the installation, for example (use the same as your spike installation):
   ```sh
   $ export $RISCV="/path/to/desired/location"
   
5. Run the following commands:
   ```sh
    $ mkdir build
    $ cd build
    $ ../configure --prefix=$RISCV --host=riscv64-unknown-elf
    $ make
    $ make install

## Generating data using this repository
## Analysis using Spike and some auxiliar files

1. Once the spike setup is done, run the following command to allow us run Spike from wherever folder
   ```sh
   $ export PATH="/path/to/desired/location/bin/:$PATH"

2. Run the following command to clone the repository and enter the newly created repository:
   ```sh
   $ git clone https://github.com/hugo-navarro/Spike-Cache-Analysis
   $ cd Spike-Cache-Analysis

3. Compile the matrix_multiply.c file with the following command:
   ```sh
   $ /path/to/desired/location/bin/riscv64-unknown-elf-gcc -o matrix_multiply matrix_multiply.c

4. Run the bash file (any changes in cache configs must be saved to the bash file prior to this step):
   ```sh
   $ ./automate_cache_configs.sh
