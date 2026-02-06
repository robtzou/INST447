# lab-01-onboarding

Setting up our environment for INST447. This assignment contains three files:

1. [README.md](./README.md) -- _This file_. The instructions you are reading.
2. [Otter-sample-assignment.ipynb](./Otter-sample-assignment.ipynb) -- This is a Jupyter notebook with a sample assignment.
3. [environment.yml](./environment.yml) -- Environment file for BYO coding environments. If you are using the recommended coding environment, you may ignore this file.

# What you need to do

First start with the Jupyter notebook. Follow the instructions in the notebook, complete the sample problem, and finally download the ZIP file. Then go on ELMS and upload the ZIP file there.

# For BYO python only: setting up the virtual environment

__NOTE:__ *You may ignore this section if you are using the recommended Python
environment*.

If you are using your own coding environment (BYO method), you may use the provided environment file to set up a virtual environment. 

To create the virtual environment, open a terminal and run:

```shell
conda env create -f environment.yml
```

To activate the it, run:

```shell
conda activate lab01
```

Then in the same terminal, you can run:

```
jupyter lab
```

And then open the notebook file.
