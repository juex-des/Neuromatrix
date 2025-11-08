# Neuromatrix 
Information & Communication Technologies  
School-Based Assessment   

Recommended compiler: Visual Studio Code  
Required extensions: Python, Pylance  

**Please retain your userdata folder and use it to replace the updated version's userdata folder in order to keep your user data**  
*Please refer to this [link](https://docs.github.com/en/get-started/start-your-journey/downloading-files-from-github#downloading-a-repositorys-files) for instructions on how to download the source files*  


## [1.1.0] - 2025-10-29
### Patches
- The version number display has been corrected.  
- For clarity, on the profile interface, 'Streak' has been changed to 'Daily Streak' to avoid confusion with the game streak.  
- For clarity, it is mentioned that a goal in goal tracker does not necessarily have to be in this game in the introduction of the function.  
- For clarity, it is mentioned the time elapsed is 'for this session' or 'for today' in the main menu.  
- The number of initial attempts for the demo quiz: Basic Arithmetic Operation changed to 0 instead of 1.  
- Patched the issue when a quiz is played for the first time, ‘user_choice’ was not initialised and if the user died in playing that quiz, a key error will be raised.  
- Patched the issue when user died in the middle of a quiz, the remaining questions' user choice was incorrectly inherited from previous attempts.  
- Patched the unexpected behaviors in upgrading abilities.  

### UX Improvement (as followup of UAT) 
- A reminder for the user to put the terminal in full screen ('Maximize Panel Size') before entering the game would be added before entering the game.<br>However, this would only be displayed once daily (when claiming daily reward) to avoid redundant reminders.  
- Widened the column 'name' (26 -> 45 char) & 'category' (16 -> 25 char) for the table of available quizzes could be wider in order to display the info of the quiz.  
- The option to view archived quizzes has been changed to restore archived quizzes as the function was trivial.  
- When the user incorrectly answers a question, display the answer immediately.  
- When updating the program to newer versions, the user is reminded to retain their userdata and replace the folder in the source code in README.md at respiratory.
- The introduction to goal tracker shall be printed at once instead of using typingPrint() if the user haven't set a goal before.  
- A reminder for user that they could go to Shop > Potion to buy a potion when they're out of HP to play a quiz has been added.  
- The formula for reward in quiz is changed to [original reward * (1 / (attempts+1))] to prevent farming of coins.  
- When the user is out of both HP and coins, they could buy a mercy potion (Shop > Mercy Potion) so that they can continue to play quizzes.  
- It would now return to the upgrade ability menu instead of main menu, in the case that the user wants to unlock or upgrade abilities several times after unlocking or upgrading an ability.   

## [1.1.1] - 2025-11-08
### Patches
- Updated fileHandler.py in order to fix the encoding system to avoid error.  

### Improvement
- Added more default quizzes.  
- An extra line is printed after every question before showing options.  

## [Coming Soon]
- A built-in function for the user to add a quiz with Artificial Intelligence may be added.  