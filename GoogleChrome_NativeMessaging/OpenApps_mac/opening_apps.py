import os
import pathlib as pth


def launch_app(app: str):
    """
    Opens the app with name of parameter string: app.
    Can also bring app back into focus without restarting the window.
    """
    if app in "Google Chrome":
        os.system("open -a Google\\ Chrome")
    elif app in "zoom.us":
        os.system("open -a zoom.us")

    # Code below looks in the Applications folder and prints out the names of all the apps, just to see
    apps = list(pth.Path('/Applications').glob("*.app"))
    app_names = [str(i).split('/')[-1].replace('.app', '') for i in apps]
    print('Other apps: ')
    for ap in app_names: print(ap)

def close_app(app: str):
    if app in "Google Chrome":
        os.system("pkill Google\\ Chrome")
    elif app in "zoom.us":
        os.system("pkill zoom.us")
if __name__ == "__main__":
    # Launch apps
    launch_app('Google Chrome')
    launch_app('zoom')

    # Call launch_app again to bring apps into focus
    launch_app('Google Chrome')

    # Closing the apps
    close_app("zoom")
    close_app("Google")


