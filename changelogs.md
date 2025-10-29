# Changelogs

## [1.0.0] - 2025-08-14
- First full release  

## [1.0.1] - 2025-10-17
- Patched the issue of file initialization caused by incorrect naming of source file  

## [1.0.2] - 2025-10-20
- Version will be shown next to the project name, as exemplified by ‘Neuromatrix v1.0.2’  

## [1.0.3] - 2025-10-21
### Patches
- Patched the issue that the screen clear function does not work on mac OS
- Patched the issue that users can create a goal with a deposit exceeding the amount of coins they own, resulting in negative coins
- Patched display of a false broken streak: when a user first registered, they could not ‘break’ a streak
- Removed the ‘Quest’ module from new user introduction
### UI improvement
- Omitted display of 'Review of incorrect answers' if users got all questions correct as followup of UAT

## [1.0.4] - 2025-10-23
### Patches
- Changed the option description from ‘Accolades’ to ‘Tier Upgrade’ to increase coherence of term usage across the program

### UX improvement
- Added a new default quiz in order to demonstrate and allow the user to experience the quiz game without the hustle of creating a new quiz on their own.

## [1.1.0] - 2025-10-29
### Patches
- The version number display has been corrected.  
- For clarity, on the profile interface, 'Streak' has been changed to 'Daily Streak' to avoid confusion with the game streak.  
- For clarity, it is mentioned that a goal in goal tracker does not necessarily have to be in this game in the introduction of the function.  
- The number of initial attempts for the demo quiz: Basic Arithmetic Operation changed to 0 instead of 1.  
- Patched the incorrect display of ‘time elapsed in this session’ as ‘time elapsed for today’ in the main menu.  
- Patched the issue when a quiz is played for the first time, ‘user_choice’ was not initialised and if the user died in playing that quiz, a key error will be raised.  
- Patched the issue when the user died in the middle of a quiz, the remaining questions' user choice was incorrectly inherited from previous attempts.  
- Patched the unexpected behaviors in upgrading abilities.  

### UX Improvement (as followup of UAT) 
- A reminder for the user to put the terminal in full screen ('Maximize Panel Size') before entering the game would be added before entering the game.<br>However, this would only be displayed once daily (when claiming daily reward) to avoid redundant reminders.  
- Widened column 'name' (26 -> 45 char) & 'category' (16 -> 25 char) for the table of available quizzes could be wider in order to display the info of the quiz.  
- The option to view archived quizzes has been changed to restore archived quizzes as the function was trivial.  
- When the user incorrectly answers a question, display the answer immediately.  
- When updating the program to newer versions, the user is reminded to retain their userdata and replace the folder in the source code in README.md at respiratory.
- The introduction to goal tracker shall be printed at once instead of using typingPrint() if the user hasn't set a goal before.  
- A reminder for user that they could go to Shop > Potion to buy a potion when they're out of HP to play a quiz has been added.  
- The formula for reward in quiz is changed to [original reward * (1 / (attempts+1))] to prevent farming of coins.  
- When the user is out of both HP and coins, they could buy a mercy potion (Shop > Mercy Potion) so that they can continue to play quizzes.  
- It would now return to the upgrade ability menu instead of the main menu, in the case that the user wants to unlock or upgrade abilities several times after unlocking or upgrading an ability.  

## [Coming Soon]
- A built-in function for the user to add a quiz with Artificial Intelligence may be added.   