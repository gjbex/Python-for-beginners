# Troubleshooting

This guide is aimed at beginners using Python in a terminal, in JupyterLab, or
in Google Colab.

## If you are completely stuck

Start with these checks:

1. Are you in the repository directory?
1. Is the correct Conda environment activated?
1. Are you running notebook cells from top to bottom?
1. Does a data file live in the path used by the notebook or script?

## Local setup problems

### `conda: command not found`

Conda or Mamba is not installed or not on your shell `PATH`.

Use one of these approaches:

* install Miniforge, Mambaforge, or Anaconda;
* open a terminal where Conda is already configured;
* use Google Colab instead.

### `EnvironmentNameNotFound` or activation fails

Create the environment first:

```bash
conda env create -f environment.yml
conda activate python_for_beginners
```

### `jupyter: command not found`

JupyterLab is installed in the course environment, so activate that environment
first:

```bash
conda activate python_for_beginners
jupyter lab
```

### Wrong Python version

Check which Python is being used:

```bash
python --version
which python
```

On Windows with WSL, use:

```bash
python --version
command -v python
```

If the path is not inside your Conda environment, activate the environment
again.

## Jupyter notebook problems

### A notebook cell fails with `NameError`

This usually means a variable or function has not been defined yet because an
earlier cell was not run.

Fix:

1. restart the kernel;
1. run the notebook again from the top.

### A notebook shows stale or strange results

The kernel may still contain variables from older experiments.

Fix:

1. restart the kernel;
1. run all cells again in order.

### A notebook cannot find a file

Most file paths in the notebooks are relative to the notebook location.

Check:

* that you opened JupyterLab in the repository root;
* that the data file exists;
* that the path uses the correct capitalization.

## Python errors beginners see often

### `SyntaxError`

Python could not parse the code. Common causes:

* missing `:`;
* missing quote;
* unmatched parentheses;
* incorrect indentation.

Read the line number in the error message first. The actual mistake is often on
that line or the line just before it.

### `IndentationError`

Python uses indentation to define blocks.

Check:

* that indented lines under `if`, `for`, `while`, `def`, and `with` line up;
* that you are not mixing tabs and spaces.

### `NameError`

You are using a name that Python does not know yet.

Typical causes:

* misspelling a variable name;
* calling a function before defining it;
* forgetting to run an earlier cell.

### `ModuleNotFoundError`

A required package is not available in the current Python environment.

Fix:

1. activate the course environment;
1. start JupyterLab from that environment;
1. if needed, recreate the environment from `environment.yml`.

## Running scripts from the terminal

If you want to run a script directly:

```bash
python path/to/script.py
```

If the script reads input files, make sure you run it from the expected working
directory or provide the correct relative path.

## Google Colab issues

### Colab cannot find local files

Colab runs on a remote machine, not on your laptop.

You must upload:

* the notebook file;
* any data files used by that notebook.

### Work disappears after closing the session

Download your notebook or save a copy to Google Drive.

### Package differences

Colab may have slightly different package or Python versions than your local
machine. If a notebook behaves differently, prefer the local Conda environment
for reproducibility.

## When to switch from Colab to local

Colab is fine for a first pass. Local JupyterLab is usually better when:

* you need to open many notebooks and local data files;
* you want to run scripts from the terminal;
* you want a stable environment across sessions.
