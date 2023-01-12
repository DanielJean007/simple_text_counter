# Simple Word Counter Application
This application allows to type in any text and after you press the `Count` button you will see just how many words you have entered.
Pretty cool, huh?

## Running
If you have Python installed in your Windows machine, you can use the .exe in the 'dist' folder of this repo to run this application.

## Features
- `Go Back` button to redirect you to the main page after counting your words.
- A warning message, in case you forget to type in some text, will appear bellow the text box.

## Making changes and Running from source
If you have pipenv installed on a Windows machine, just type:
```
pipenv install 
```
This will create the virtual environment and install all packages and dependencies so you can modify this app.

After creating the environment you can type the following to run the application from source:
```
pipenv run python .\count_words.py
```

After making any changes your heart desires you can generate another executable by typing:
```
pyinstaller --onefile .\count_words.py
```

## Closing
If you want to setup pyenv and pipenv in your machine, please chech out: ![Robot Framework Setup](https://bit.ly/RF-setup)
This is probably enough to trobleshoot and get your pyenv and pipen setup in your machine.
