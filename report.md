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


#### Title: [Feature Request]: Sort by Filename #822

URL: https://github.com/TagStudioDev/TagStudio/issues/822

Summary of issue: Add a dropdown category to the main window that sorts the files according to the name of the file.

Testing: Because this was a feature request, there were no existing tests related to the issue when we started.

#### Title: [Bug]: The app freezes for a time when clicking on a GIF image #816
URL: https://github.com/TagStudioDev/TagStudio/issues/816

Summary of the issue: There is a preview window and when a user clicks on a gif file, there is a delay that lasts a few seconds before the gif file can be seen in 
in the preview. During this time, the app freezes and the user can not interact with the app in any way. Fixing this issue should not reintroduce the
problem which the pause fixed, namely that files playing in the preview should still be deletable, which they were not previously.

Scope: Fixing the bug involved making changes in the function _update_animation so that we still can do other things when clicking on a .gif file or files with similar formats. 
 
Testing: There were no tests for this part of the code before we started so the tests for the expected functionality had to be added. 

#### Title: [Feature Request]: Add the ability to open the URL in the URL field #506
URL: https://github.com/TagStudioDev/TagStudio/issues/506

Summary of issue: The user is able to create “fields”, each field has a text-line. The feature requested is that links in the text-line of a field should be clickable and opened in the browser. The issue specifies that this should be the case for the URL type of field, but in the comments of the issue, it is requested that this functionality should extend to all the fields with text-line.

Scope: Fixing the issue involved changes in the FieldContainers class and in the TextWidget class. In the FieldContainers I had to add a function for matching and replacing URLs with the correctly formatted URL in the user given input. In the TextWidget I had to set the flags concerning clicking links and opening the browser to true.

Testing: There existed some testing for creating fields, and those tests passed before. I added tests for validating that the users input would be formatted and displayed in the GUI correctly.

#### Title: [Feature Request]: Shortcut customization #814

URL: https://github.com/TagStudioDev/TagStudio/issues/814

Summary of issue: The current shortcut Ctrl + Shift +T is quite long and not that accessible for me when I have to add hundreds of tags every hour while tagging my library. I'd like to have a shortcuts config where the user can choose these binds.

Scope: For this issue resolution, I refactored the code that defines the keyboard shortcut for the “Add Tag” action in TagStudio. Previously, the shortcut was hardcoded as "Ctrl+Shift+T," but now the action dynamically retrieves its shortcut from persistent settings (using QSettings) defaults to "T" if the user hasn't changed the shortcut before. In addition, I implemented a dedicated ShortcutSettingsPanel that allows users to modify and save their desired key sequences via a QKeySequenceEdit widget. This panel updates the QSettings and immediately applies changes to the corresponding QAction. A simple unit tests was also added using pytest and pytest‑qt to ensure that the new shortcut customization works correctly and that the changes persist across sessions.

Testing: Because this was a feature request, there were no existing tests related to the issue when we started.


## Requirements for the new feature or requirements affected by functionality being refactored

### Requirements for [Feature Request]: Sort by Filename #822

#### Requirement 1: Add the feature sort by filename to dropdown menu
- The new sorting option "FILENAME" is defined and can be sorted in ascending or descending order

#### Requirement 2: Sort the files by name
- Sort the filenames according to alphabetical order by their filenames

### Title: [Bug]: The app freezes for a time when clicking on a GIF image #816

#### Requirement 1: Clicking on a gif should not prevent the user from interacting with the app. 
- When the user clicks on a gif icon should we still be able to use the other functionalities in the app. 

#### Requirement 2: A gif playing in the preview should be deletable.
- The bug was introduced because the developers wanted the users to be able to delete a gif that was playing in the preview and fixing this bug should not reintroduce that behaviour. 


### Requirements for [Feature Request]: Shortcut customization #814

#### Requirement 1: Configurable shortcut
- The “Add Tag” action must allow users to set their keyboard shortcut, which defaults to T.

#### Requirement 2: Persistence
- Any changes to the shortcut must be saved via QSettings and reloaded on application start.

#### Requirement 3: Dedicated UI panel
- ShortcutSettingsPanel provides a QKeySequenceEdit for editing the shortcut.

#### Requirement 4: Immediate application
- The updated shortcut is applied instantly to the QAction without needing to restart the application.


## Code changes

### Patch

#### Patch for [Feature Request]: Sort by Filename #822
https://github.com/DD2480-Group-26/TagStudioClone/blob/main/0006-Closes-issue-number-8.patch


#### Patch for [Bug]: The app freezes for a time when clicking on a GIF image
https://github.com/DD2480-Group-26/TagStudioClone/blob/main/0002-Added-the-patch-for-issue-1.patch

#### Patch for [Feature Request]: Add the ability to open the URL in the URL field #506
https://github.com/DD2480-Group-26/TagStudioClone/blob/main/0001-Added-the-patch-for-issue-3.patch


#### Patch for [Feature Request]: Shortcut customization #814
https://github.com/DD2480-Group-26/TagStudioClone/blob/main/0001-feat-closes-issue-5.patch


All the patches we applied pass the repository's automated tests during our pull requests.

## Test results

[Tests before addition](https://dd2480-group-26.github.io/TagStudioReports/report_before_addtions.html?sort=result)

[Tests after addition](https://dd2480-group-26.github.io/TagStudioReports/report_after_addtions.html?sort=result)


## UML class diagram and its description

[UML diagram for [Feature Request]: Add the ability to open the URL in the URL field #506](https://www.plantuml.com/plantuml/png/bLLjR-Cs3FwUNq7qm-fYkTvtunRShjTY1nJ5RirUW64GQ8jnXCXI9j5fUkl--oHBhk70QB02ZINouGiV4jH7p-YuQ_NYyjqRVujB-1dh7JPKmgzVu7Sb6s8FnHgRH-waibTdxFV96Ywygw__vkkdvE42_bai06gDtiET8Yrlh65KXfm7EZ8PwU5h2XUW4Fw-XmqUh5DCejjBP98bFAh6e2ugQ_LL1g6hj-f0yWrGIAl_W5PL2VUgSkYUiqYwOEnA-CgV-rCMAwDOeLRVeiFeQP1xOVTa9hBQjgqrOXEhycK8uZbhMdKaEQUeiTu63HbsYhBgmssuFQy6n43Fe9sIDi3sQ4YBgX6rrNP8tjVEQYqqFjkEGsc_VRB7-_uo1Q0Z3Eh7_lPZk6IsChE9KB5njXKKSolwNw429ShmSW1KA1loYHBu0TQkewiI3bR9gQF6eUaqkko6iGb6dlX36AxL4dhfXAmFdz1JN_VgVmTZspIQP8nIXFynwQGG1zGT9JTJ-wsI94RsYwcs8OukHOrCZOtDAwPr1BXKDVyPpYyFrj3oLVDNTk6ejGTAXOfz87VFXS6MWWzsL_rlHgAK6SPMUD9KCyaYII8_YQLfWj4cPZGnYOA-_9UUrd1OJQsUd68QgowKaNJCXFNnIdZjnHAK5_raltRX3hMd6O-9gbclfzrFXAQnA65WB_YEd_CXJuajJhEU7P9vw19YocGuTMGkHalUOqEYiiUYRs72nZAqhi8ABE4cdB3I9pbIgpZDiF3zcl9fEjF8vzwyU4g7PS9R8x3oCQ7viVztNArhEdBUeiDMxMkQRDPtKA6dSJ_yTBeVEDW6TKKwQE_ZTxePX8ZxKOY25MlAfGUZp5X6UM8HXSMecQPy2UijzRb0UYPo4Rn5dgdaEbSvLz8b5B5_MI-9KMaFnZBuhNqoLtt84FJSutSRGZc36jx3dSEMdgpRmNVmsRQe3Dn4x-JFU4avv6SctSRd9RS9ctGQfsunzpOcuQH3IPAwShwUNqWZAslyLktFvNtwB5zVhuOge8Gk53uB6Kfx2pEL1MJj29dy-nODDlD68pK1ltUs9k_daP7EW1bsyhU06gSd0Z9TGuQdof7T0H6OUx1C9Pn6KwRMdIGFQC8vpygcCtKa6TZ2HOix4bgPdHUrLlKkxe0Bs5W7wzi_rkB-oyDjMgbXdZ-IaLsh5_y1)

[UML diagram for [Feature Request]: Shortcut customization #814](https://www.plantuml.com/plantuml/png/TLHDRzim3BthLn2zfCKGxEv3qUxZjClQ5DZHu2J65g18daWd-zZ--_IX6EaotopoyV7naV032qQP3qw95KUm6qCKFGkydrd2mVv4iS73C-rHIuZM3qfju1qomOIU79oi6KX0HXG8SmHTwcgIWRuBUQFmAqjC1A0TCiFddFnI2t-fFvdnPIJmT6ga-n21Z9NK3hWfObMA5uKxafpdGfPe002sOA8zKeGEFfIF5aLZUi6XFtFrcJo1dZxHZnrzcybh-fX21Vu668-qOFdsBY6FmPggDFK_bN5Nb5W_KhJ2i8_XS3cg-Zz-k_rz_mhMt6YJt8O8E4tEwhe97Rp4u1p5kwfY3CumSEC4z2R52L1dUFEich6Oj82J0sSn_pWbeMTof8LCNwao-B6I5X-UQOh4vEkIme7WITerCCnC1gm76TkTD25NXhVmegA-MwFQnfN1URGJTsgpulhCn81N_FcISYw2zTEyleBxwygkM8tMysfJr9gOQV5N0WmaR-V9eD35uQvtROLTqQysxPrV5wPateaYMvPbTQeXCya2lEAfjo4ZdHqjVjmy6WClEDoy8cc0hXOfzK3UvF_2Nm00)

[UML diagram for [Feature Request]: Sort by Filename #822](https://www.plantuml.com/plantuml/png/TPBVQeCm5CRlynIvj8Wl4CQecoaCwc1qiCiGasmDonz8Jcd7sBlF654HwuNaVFdEpoydxYFm01Tha30yHamTX1_yYt3_L5XBWhM3iNBSAe8ZXB6M71JZKYf9XZLegz0VGifTB3xv0DfzjLugckgCREftokgceSrG7bwEzBLkQUhAtpze0ogSeCTDAM96CTkpo1eyUdWKoibU9xZptWngYQyQpcpPNgJNRcjNwg04QE-A7hMR0nrr5_WqaX97nOCuCvFbudF8k_2tNBiFxQI_RkPdmjlET_v6yDjpMZxvssHR9RdhBLT8Rap7nNSn7co3D5jIqdp93rMr7kQuKrMFouj0UGQvOqDFzldOQA-SJ3_KFm00)

[UML diagram for  [Bug]: The app freezes for a time when clicking on a GIF image]
(//www.plantuml.com/plantuml/png/bPHFRniX4CNlV8evEggZzepIA8tKGwIsSjAgFI8MPdUHMLWDitRTgj-zi5vl_2Vgdmi6vlSUp4FUkyIQUEYyI6iNUasw0-DrIk-OoLK3uuE9uRFxWV16YB42AyADm-sNTkWg-2a00Ax1TOtAECUWKgObyD1xl761bv27sndJ3IhIxAA4saVDKw7Vcwhi8-5nDQJsVdJxHhhlaSwenjMP-g0hz5Cbx-Jpwnef5-xpv4ApSLR2LsSnhhpUpMKkRIZ2O96AU6phQLpEJ8VMQTMFCWaVo-h4Gvc1iWCh7LnNUWkgTXvxpQs4LHv7xXKaP7MKmE8uXwk96Ngh6IUiHBbuCSyb78lXBNoA0GyUQUlOj6hgV37zIaXC1qHPbqf3gjRULzgizoSkJk-z1FpEUvq4wmmVrFCj_rypP_Gt7TpS4DRQS2IqjxTdDfloaifZeytkpEdbSyT7_2Ev1-VO_gsjrjbdoVm077jLz6f8EEyIbgTyly702ooZXCUdvxqhyKk841c1NDConFhahoRbHO82u6bEw39Ww93RQ6N6hZEeRO9o9wXsZ0ci8pJiTr1JxF8ghKVkeUizTXWu0SLgI0n850bQ7QnteO6junQOTg-DPjCk1GOBvTP2tELf-PJy1W00)
## Overall experience

What are your main take-aways from this project? What did you learn?

How did you grow as a team, using the Essence standard to evaluate yourself?

The experience we gained during the project is being comfortable using git and always writing tests to support your written code. 

By working with the issues we have gained insights about the construction of the project and how to improve other projects in the future.

We are currently in the “In-place” state, which is the same state as we were in the last project. We are comfortable in our communication and conscious of what we can expect from one another.  
