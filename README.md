# WikiGames
WikiGames is a website created to be a encyclopedia of Games.
Here anyone can contribuite providing games and your stories.

## REQUIREMENTS
*  VAGRANT
*  VIRTUALBOX
*  FACEBOOK APP AT FACEBOOK DEVELOPERS
*  GOOGLE APP AT GOOGLE DEVELOPERS

## INSTALL
1. PREPARE THE FLASK APP TO RUN PROPERLY
    1. After create your Facebook and Google APPs and take the necessary data to use the login functionality do:
        1. At /templates/login.html put your FACEBOOK APP ID in the placeholders, do the same for GOOGLE APP ID
        1. At /fb_secrets.json put your FACEBOOK APP ID and your FACEBOOK CLIENT SECRET
        1. Get your client_credentials.json at google developers in your app, rename it to "gplus_client_secret.json" or only get the content and put in the placeholders at /gplus_client_secret.json

1. PREPARE THE VM TO RUN THE FLASK APP
    1. At the folder that has the "Vagrantfile" open the terminal (or cmd at windows) and run:
    ```
        vagrant up

        vagrant ssh
    ```
    * This will run the vagrant, it will read the Vagrantfile and prepare the vms (virtual machines) that will run our app and will enter at vagrant console through the vagrant ssh.
    1. At the vagrant console go to /vagrant and run:
    ```
        python3 app.py
    ```
1. IF EVERYTHING WAS OK YOU CAN ACCESS THE WEBSITE FROM YOUR BROWSER AT http://localhost:5000

## HOW TO CONTRIBUTE 
You can find more instructions, if you're a beginner, of **how to contriute** in this project: https://github.com/GabrielSlima/WikiGames/blob/develop/CONTRIBUTING.md

## LICENSE

All files within this repo are released under the MIT (OSI) License - https://en.wikipedia.org/wiki/MIT_License