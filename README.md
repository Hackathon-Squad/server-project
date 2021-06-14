# server-project

## Project Setup

1. Make sure that either [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Miniforge](https://github.com/conda-forge/miniforge) is installed
2. Make sure that [Yarn](https://yarnpkg.com/getting-started/install) is installed
3. Clone the repository 
4. Install frontend dependencies
```
cd frontend
yarn
```
4. Create Conda Environment
```
cd ../backend
conda env create -f environment.yml
conda activate server-project
```
5. IDE Setup
  * Restart VSCode
  * Open `backend/app.py`
  * Click the python interpreter in the bottom left
  * Select `Python 3.8.10 64-bit ('server-project': conda)`
6. Run Project
```
cd frontend
conda activate server-project
yarn run dev
```
Note: You do not need to run `conda activate server-project` if the terminal shows `(server-project)`
