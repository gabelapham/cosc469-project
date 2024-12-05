To run the phishing you need to:
1.  run git clone on https://github.com/gabelapham/cosc469-project
2.  run pip install -r requirements.txt to get the required packages
3.  on the terminal naviagate to the app.py file within the keylogger folder, this can be done through either the terminal or vscode file manager
4.  run the code with either the run button on vscode or the command python app.py in terminal
5. from there click on the link that is produced

To run the phishing detector you need to:
 1. run steps 1 and 2
 2. navigate to updatedchk.py
 3. where it say safe browsing you will need to put in an safe browsing api key to do this first go to this link https://console.cloud.google.com
 4. from there make a new project
 5. then in the search bar search safe browsing api and enable it
 6. after this navigate to credential and make the safe browsing credential
 7. put the credential key you make into the safe browing line within " " ex safeBrowse = SafeBrowsing("this is the new key") # Google Safe Browsing API Key
 8. run through either terminal or vscode run button the same way as steps 3 and 4 of phishing