# Neuromatrix 
Information & Communication Technologies  
School-Based Assessment   

Recommended compiler: Visual Studio Code  
Required extensions: Python, Pylance  

**Please retain your userdata folder and use it to replace the updated version's userdata folder in order to keep your user data**  
*Please refer to this [link](https://docs.github.com/en/get-started/start-your-journey/downloading-files-from-github#downloading-a-repositorys-files) for instructions on how to download the source files*  

## [1.1.2] - 2025-12-03
### Patches
- Patched the issue that an error would be raised if the user returns a string as bet amount in coinflip.
- Patched the issue that the failure message is only shown after entering heads/tails in the case that user enters an amount below/exceed the range of acceptable bet.
- Patched the issue when the user upgraded one of the abilities to the maximum, the ‘next tier’ field may not be defined properly.

## [1.1.3] - 2025-12-05
### Patches
- Patched the issue that the name field when creating a goal could be empty.

### Improvements
- As a followup of UAT, new users are now given 25,000 coins upon registration for them to start with.
- The coins owned can be shown when creating a goal in the goal tracker as a reference to decide the deposit amount.
- In cases of typo, after inputting every question, a confirmation is added. If not confirmed, the user may edit the question/options/answer.

## [Coming Soon]
- A built-in function for the user to add a quiz with Artificial Intelligence may be added.  