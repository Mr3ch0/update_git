import os
import subprocess

def update_github_app(app_folder):
    # navigate to the app folder
    os.chdir(app_folder)
    
    # check if the folder contains a git repository
    if os.path.exists(".git"):
        # pull the latest changes from the remote repository
        subprocess.run(["git", "pull"])
    else:
        print(f"{app_folder} is not a git repository, skipping update.")

def main():
    apps_folder = "/opt/"
    
    # list all the subdirectories in the apps folder
    for app in os.listdir(apps_folder):
        app_path = os.path.join(apps_folder, app)
        
        # check if the subdirectory is a directory
        if os.path.isdir(app_path):
            update_github_app(app_path)

if __name__ == "__main__":
    main()
