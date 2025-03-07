# Report for assignment 4


## Project

Name: TagStudio

URL: https://github.com/TagStudioDev/TagStudio

One or two sentences describing it: The repository we chose is a application for file and media managment, with a tag-based system focused on flexability and freedom for the user.

## Onboarding experience

Did you choose a new project or continue on the previous one?
For the assignment did we choose a different project. The experience was similar to the previous one. The tagstudio program is
in a relativly early stage of development and there is not a significant amount of information which made it hard to understand 
how the code worked, but that is similar to the previous project which also did not have a lot of documentation. 


## Effort spent

For each team member, how much time was spent in

1. plenary discussions/meetings;
- Love: 2 hours.
- Filip: 2 hours.
- Adam: 2 hours.
- Robin: 2 hours.

2. discussions within parts of the group;
- Love: 2 hours.
- Filip: 2 hours.
- Adam: 2 hours.
- Robin: 2 hours.

3. reading documentation;
- Love: 1 hour.
- Filip: 1 hours.
- Adam: 2 hours.
- Robin: 1 hour.

4. configuration and setup;
- Love: 3 hours. Since I had to change to python 3.12 which broke my python install and making it work again took some time. The developers provided a requirements file which installed almost all of the required dependencies. We only had to download FFMPEG separely.

- Filip: 2 Hours. I also had some problems when setting up the project, there seemed to be some modules missing in the virtual enviroments requirement.txt which installed all the necessary modules so I hade to manually install some of the modules, there was also a windows specific problem for running the tests, see issue here `https://github.com/TagStudioDev/TagStudio/issues/770` which halted the process of setting up the application for me.

- Adam: 2 hours.

- Robin: 3 hours. I had some problem with pyenv. When I created my virtual environment it didn't use 3.12 even if I specified that it should. I solved it by using the python3.12 bin when creating the venv instead of the python3 bin.

5. analyzing code/output;
- Love: 1 hour.
- Filip: 2 hours.
- Adam: 4 hours.
- Robin: 4 hours.

6. writing documentation;
- Love: 2 hours.
- Filip: 3 hours.
- Adam: 3 hours.
- Robin: 2 hours.

7. writing code;
- Love: 15 hours
- Filip: 10 hours.
- Adam: 8 hours.
- Robin: 10 hours.

8. running code?
- Love: 2 hours, first to find out what was wrong with the code and then to make sure that my changes did not break any other part of the code.
- Filip: 3 hours, I include the time I spent bug searching the code I wrote and not just the run-time.
- Adam: 2 hours.
- Robin: 1 hour.

For setting up tools and libraries (step 4), enumerate all dependencies you took care of and where you spent your time, if that time exceeds 30 minutes.

## Overview of issue(s) and work done.


##### Title: [Feature Request]: Sort by Filename #822

URL: https://github.com/TagStudioDev/TagStudio/issues/822

Summary of issue: Add a dropdown category to the main window that sorts the files according to the name of the file.

Testing: Because this was a feature request, there were no existing tests related to the issue when we started.

##### [Bug]: The app freezes for a time when clicking on a GIF image
URL: https://github.com/TagStudioDev/TagStudio/issues/816

Summary of the issue: There is a preview window and when a user click on a gif file is there a delay that lasts a few seconds before the gif file can be seen in 
in the preview. During this time does tha app freeze and the user can not interact with the app in any way.  Fixing this issue should not reintroduce the
problem which the pause fixed, namely that files playing in the preview should still be deletable, which they were not previously.

Scope: Fixing the 

Testing: There were no tests for this functionality before 

##### Title: [Feature Request]: Add the ability to open the URL in the URL field #506
URL: https://github.com/TagStudioDev/TagStudio/issues/506

Summary of issue: The user is able to create “fields”, each field has a text-line. The feature requested is that links in the text-line of a field should be clickable and opened in the browser. The issue specifies that this should be the case for the URL type of field, but in the comments of the issue, it is requested that this functionality should extend to all the fields with text-line.

Scope: Fixing the issue involved changes in the FieldContainers class and in the TextWidget class. In the FieldContainers I had to add a function for matching and replacing URLs with the correctly formatted URL in the user given input. In the TextWidget I had to set the flags concerning clicking links and opening the browser to true.

Testing: There existed some testing for creating fields, and those tests passed before. I added tests for validating that the users input would be formatted and displayed in the GUI correctly.

##### Title: [Feature Request]: Shortcut customization #814

URL: https://github.com/TagStudioDev/TagStudio/issues/814

Summary of issue: The current shortcut Ctrl + Shift +T is quite long and not that accessible for me when I have to add hundreds of tags every hour while tagging my library. I'd like to have a shortcuts config where the user can choose these binds.

Scope: For this issue resolution, I refactored the code that defines the keyboard shortcut for the “Add Tag” action in TagStudio. Previously, the shortcut was hardcoded as "Ctrl+Shift+T," but now the action dynamically retrieves its shortcut from persistent settings (using QSettings) defaults to "T" if the user hasn't changed the shortcut before. In addition, I implemented a dedicated ShortcutSettingsPanel that allows users to modify and save their desired key sequences via a QKeySequenceEdit widget. This panel updates the QSettings and immediately applies changes to the corresponding QAction. A simple unit tests was also added using pytest and pytest‑qt to ensure that the new shortcut customization works correctly and that the changes persist across sessions.

Testing: Because this was a feature request, there were no existing tests related to the issue when we started.


## Requirements for the new feature or requirements affected by functionality being refactored


Optional (point 3): trace tests to requirements.

## Code changes

### Patch

#### Patch for [Feature Request]: Shortcut customization #814
https://github.com/DD2480-Group-26/TagStudioClone/blob/main/0001-feat-closes-issue-5.patch

git diff ...

Optional (point 4): the patch is clean.

Optional (point 5): considered for acceptance (passes all automated checks).

## Test results

[Tests before addition](https://dd2480-group-26.github.io/TagStudioReports/report_before_addtions.html?sort=result)

[Tests after addition](https://dd2480-group-26.github.io/TagStudioReports/report_after_addtions.html?sort=result)


## UML class diagram and its description

### Key changes/classes affected

Optional (point 1): Architectural overview.

Optional (point 2): relation to design pattern(s).

## Overall experience

What are your main take-aways from this project? What did you learn?

How did you grow as a team, using the Essence standard to evaluate yourself?

The experience we gained during the project is being comfortable using git and always writing tests to support your written code. 

By working with the issues we have gained insights about the construction of the project and how to improve other projects in the future.

We are currently in the “In-place” state, which is the same state as we were in the last project. We are comfortable in our communication and conscious of what we can expect from one another.  

Optional (point 6): How would you put your work in context with best software engineering practice?

Optional (point 7): Is there something special you want to mention here?
