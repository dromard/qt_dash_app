# qt_dash_app
Make great dashbords in python QT using Dash and bundles it in an application using pyinstaller. 
This repo is an example of a QT application that embeds a Dash dashboard and that can be then bundled into a portable application.
It then integrates the power a python web dashbords into a the most known GUI python application python QT. Indeed making data visualization in QT can be tricky and mixing these two technologies can help a lot.
Furthermore,in order to share easely the work, the code shows how to integrate it into a portable application by using pyinstaller.

# How it works

To integrate Dash into the Qt application we create a thread for the Dash web application and then using the QWebEngineView a widget that allows to display web content, we integrate it into the QT application: The QWebEngineView pointing to the adress of the Dash web app.

In order to bundle everything in an excecutable, we created multiple hooks as pyinstaller (see hook directory and modifcation in the .spec file) is unable to find all the hidden imports. We also had to change some setting of pyinstaller: we increased in the .spec file the number of recursions limit and made some modifications in the config file of pyinstaller.

# How to run
The application has been desiged in (Ubuntu 5.4.0-6ubuntu1~16.04.12)

1. You first need to install all the required packages using conda : conda install --yes --file requirements.txt
2. You need to modify the file  PyInstaller/depend/dylib.py and to comment the following lines:
    * r'/libxcb.*\.so\..*': 1,
    * r'/libxcb\.so\..*': 1,
    * r'/libxcb-dri.*\.so\..*': 1,
3. Run the following command:  'pyinstaller --windowed qt_dash_app.spec`.
You get then two directories build and dir. The dir directory is the one you have to share whereas the build directory.
4. Launch the app: `../dist/qt_dash_app/qt_dash_app `


