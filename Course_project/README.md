# Virtual Environment

In this project, I will try to create my own virtual environment to be used specifically for my project. The aim of it is to contain the Python version I'm using and all libraries and dependencies that are needed for the project. 

A seperate virtual environment for a project allows you to manage dependencies, versions and packages without conflicts across different projects. 

The steps taken for creating this virtual environment are listed below: 
1/On command prompt, navigate to the project folder
-PS C:\Users\hedal246> cd Desktop/COSC_project

2/Create the virtual environment
-PS C:\Users\hedal246\Desktop\COSC_project> python -m venv COSC_env

3/Activate the virtual environment
-PS C:\Users\hedal246\Desktop\COSC_project> COSC_env/Scripts/activate

4/Install dependencies
-(COSC_env) PS C:\Users\hedal246\Desktop\COSC_project> pip install numpy pandas seaborn matplotlib

5/Install Jupyter notebook inside the virtual environment
-pip install jupyter
-pip install ipykernel

6/Add virtual environment to Jupyter as a kernel
-PS C:\Users\hedal246\Desktop\COSC_project> python -m ipykernel install --user --name=COSC_env --display-name "Python (COSC_env)"

7/Start Jupyter notebook
-jupyter notebook

8/Select the virtual environment in Jupyter
-Click on switch kernel in the top right corner and select
 Python (COSC_env) 

/Deactivate the virtual environment
-deactivate




