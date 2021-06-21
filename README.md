# server-project

## Project Setup

1. Make sure that either [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Miniforge](https://github.com/conda-forge/miniforge) is installed
2. Make sure that [Yarn](https://yarnpkg.com/getting-started/install) is installed
3. Clone the repository 
4. Install front-end dependencies
```
cd frontend
yarn
```
5. Create Conda Environment
```
cd ../backend
conda env create -f environment.yml
conda activate server-project
```
6. IDE Setup
  * Restart VSCode
  * Open `backend/app.py`
  * Click the python interpreter in the bottom left
  * Select `Python 3.8.10 64-bit ('server-project': conda)`
7. Add Mongo URI
  * Create a file called `.env` in `backend`
  * Add `MONGO_URI=[Connection String]`
8. Add API URL
  * Create a file called `.env` in `frontend`
  * Add `REACT_APP_API_URL="http://localhost:5000/"` to the file
9. Run Project
```
cd frontend
conda activate server-project
yarn run dev
```
Note: You do not need to run `conda activate server-project` if the terminal shows `(server-project)`

## Installing New Backend Packages 

1. Deactivate the conda environment
```
conda deactivate
```
2. In `backend/environment.yml`, add the package to the `dependencies` list
3. In `backend/Dockerfile`, add the package to end of `RUN python -m pip install gunicorn flask [new package]`
4. Update the conda environment 
```
conda env update --file environment.yml
```
5. Restart VSCode
6. Activate the conda environment
```
conda activate server-project
```
## Installing new Front-end Packages
```
cd frontend
yarn add [new package]
```
