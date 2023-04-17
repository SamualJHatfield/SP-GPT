# SP-GPT
A GPT 3.5-turbo powered multi-lingual Standardized Patient. This is intended for medical students looking to practice clinical scenarios in a multi-lingual context. 

The current version of this code simply labels you as "The Doctor" and the Bot as "The Patient."
It uses Google translate's gTTs for text to speech along with pygame for voice rendering. 
Google translate is the engine for multi-lingual applications. Future updates may include the use of Google Cloud services for more accurate translations. 

Please follow the instructions below to get the bot up and running:

First, install the most recent copy of Python from here: https://www.python.org/downloads/
Next, you will need your own OpenAI API key to operate the bot. This can be accquired here:  https://platform.openai.com/account/api-keys
From the main page of the SP-GPT github, select the green "code" box, and download the code. 
Navigate to the location the file was saved and identify the "interview_bot.py" file. 
Right click on interview_bot.py, select "open in notepad" or your prefered .txt file editor (not word processor).
Within the code near the top under the list of "import" files, you will see a statement that says "Your OpenAI API key here." 
Paste your API key into this spot between the quotation marks, ensuring not to have any extra spaces or punctuations
After saving the API key, open your command-line navigator (Type "Windows powershell" or "Command line" into your device's search menu)
Within the command-line navigator, navigate to the location of the downloaded SP-GPT file 
 - To navigate to the location in the command-line, right click on the SP-GPT folder (not the files within, the actual folder), select "Copy as path".
 - Within the command line, type "cd" then paste the path to the SP-GPT folder into the navigator after cd (it should look something like "cd User://Path"
Once in the folder location in the command line, type "pip install -r requirements.txt" (Without the quotations) and press enter. This will install all packages necessary to run the bot. 

From here, the bot should be ready to run! Double click on the Interview_bot.py folder and get started talking to your SP in whatever language you choose!

"user language" is the language you intend on speaking to the bot.
"Bot language" is the language you would like it to speak to you. 
"Would you like it to speak slowly?" is case sensitive. 

This bot is still in its infancy and may not always say exactly what a patient may say. 
As standard google translate is being used, there may be differences in words used by the bot versus what a patient may use, particularly in less commonly spoken languages. 
If the bot fails to start, the directions above are insufficient, or an error occurs within the first few messages, let me know what happened so I can work on it! samual-hatfield@uiowa.edu

If you would like to change the role from "the patient" or give it a specific cheif complaint, navigate to the interview.py file in the same way that was done for the OpenAI API key. 
Near the bottom of the .txt file, you will find "Bot role" and "user role". These can be changed to whatever you need!
