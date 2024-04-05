# Meeting Notes Team G

## February 8, 2024

**Recorded by:** Devender Singh

**Notes submiited on:** February 13, 2024

**Venue:** Discord 

**Source:** Discord voice

**Time:**  7:00 to 9:00pm

**Attendance:** Cameron Selci, Devender Singh, , Mohd Ali Bin Naser, Evan Best Jager Cooper 

Team G successfully adopted the follwoing decisions for the term project and following tasks were assigned:

AppLogic: Cameron Selci 

UserSession : Devender Singh 

ServerAPI : Jager Cooper  

FrontEnd : Mohd Ali Bin Naser  

DataStorage : Evan Best 

Bottle will handle all green parts of the diagram, (session management, templating engine etc.) , Also studied past challenges (8) in detail, and bottle framework to gain more insights.


## February 12, 2024
**Scrum Master:** Mohd Ali Bin Naser

**Recorded by:** Devender Singh

**Notes submiited on:** February 13, 2024

**Venue:** Class  

**Source:** Class discussion  

**Time:** 2:00 to 2:50pm

**Attendance:**  Devender Singh, Cameron Selci, Mohd Ali Bin Naser , Evan Best, Jager Cooper

Decided on several other decisions, including creating a pipeline outlining the approach to individual tasks for the team project. Mohd Ali Bin Naser was nominated as the Scrum Master.

Additionally, Python was adopted as the primary tool for implementing logic.

## Februaru 14,2024
**Scrum Master:** Mohd Ali Bin Naser

**Recorded by:** Devender Singh

**Notes submiited on:** February 17, 2024

**Venue:** Discord

**Source:** Discord Voice

**Time:** 7:00 to 9:00 pm

**Attendance:**  Devender Singh, Cameron Selci, Mohd Ali Bin Naser , Evan Best, Jager Cooper

In this meeting, Team G discussed the selection of a UML diagram tool to be used for the project. Team studied about UML diagrams.
Further discussions were held regarding the overall project development, including strategy and implementation phases. Specific roles and responsibilities of team members in relation to this new phase were also elaborated. 
Team Members successfully demonstrated how they have worked on their parts specifically the stub implementation:

serverAPI.py: Jager Cooper

user.py: Devender Singh

applogic.py: Cameron Selci

store.py :Evan Best

html.py: Mohd Ali Bin Naser

## February 28, 2024
**Scrum Master:** Jager Cooper

**Recorded by:** Cameron Selci

**Notes submiited on:** February 17, 2024

**Venue:** EN 2036

**Time:** 2:00pm to 3:00pm

**Attendance:**  Devender Singh, Cameron Selci, Mohd Ali Bin Naser , Evan Best, Jager Cooper

Discussed sprint activities.

Discussed implementations.  

Discussed KanBan/issue tracking as posted in notes.

## March 1, 2024

**Scrum master rotation:** Mohd Ali Bin Naser -> Jager Cooper -> Cameron Selci -> Devender Singh -> Evan Best

**Note taker Rotation:** Jager Cooper -> Evan Best -> Mohd Ali Bin Naser -> Devender Singh -> Cameron Selci

**Scrum Master:** Cameron Selci

**Recorded by:** Jager Cooper

**Venue:** EN 2036

**Time:** 2:00pm to 3:00pm

**Attendance:**  Devender Singh, Cameron Selci, Mohd Ali Bin Naser , Evan Best, Jager Cooper

Breakdown of tasks into subtask and addition of them in to the kanban board  

- Making a move in a game
  - Front-end send move data
  - API receive move data and verify with game logic
  - Game logic send game state to DB and API
  - DB update game state and turn
  - API call to update front-end
  - Front-end sends new display
- User login
  - Front-end login button
  - get form submit
  - verify login info
  - load user from db
- Recording a players win loss history
  - applogic on game end - get user info from db - send info to server
  - send winner and loser to user manager and html
  - user manager update win/loss in DB
  
Discussed implementation of much of these tasks and interoperability

## March 6th, 2024

**Scrum master rotation:** Mohd Ali Bin Naser -> Jager Cooper -> Cameron Selci -> Devender Singh -> Evan Best

**Note taker Rotation:** Jager Cooper -> Evan Best -> Mohd Ali Bin Naser -> Devender Singh -> Cameron Selci

**Scrum Master:** Devender Singh

**Recorded by:** Jager Cooper

**Venue:** EN 2036

**Time:** 2:00pm to 3:00pm

**Attendance:**  Devender Singh, Mohd Ali Bin Naser, Jager Cooper, Cameron Selci, Evan Best

Discussed:

- where we went wrong on our group Assignment 1 grade
- grading scheme for sprint 1
- using PR's and branches going forward for meetingNotes.md
- how we will be handling code review process: we will be using the review assignee feature and go through videos of code reviews.

decided that our last meeting for the sprint will be the 15th of March.

## March 8th, 2024

**Scrum master rotation:** Mohd Ali Bin Naser -> Jager Cooper -> Cameron Selci -> Devender Singh -> Evan Best

**Note taker Rotation:** Jager Cooper -> Evan Best -> Mohd Ali Bin Naser -> Devender Singh -> Cameron Selci

**Scrum Master:** Devender Singh

**Recorded by:** Evan Best

**Venue:** Discord

**Time:** 2:30pm to 3:30pm

**Attendance:**  Devender Singh, Mohd Ali Bin Naser, Jager Cooper, Cameron Selci, Evan Best

Discussed:

- session management, need to implement multiple users.
- refactoring modules for better implementation.
- everyone should start working on their assigned TODO's on the project board.
- doing code review for currently open PR's.

## March 9th, 2024

**Scrum master rotation:** Mohd Ali Bin Naser -> Jager Cooper -> Cameron Selci -> Devender Singh -> Evan Best

**Note taker Rotation:** Jager Cooper -> Evan Best -> Mohd Ali Bin Naser -> Devender Singh -> Cameron Selci

**Scrum Master:** Evan Best

**Recorded by:** Mohd Ali Bin Naser

**Venue:** Discord voice call meeting

**Time:** 7:30pm to 8:45pm

**Attendance:**  Devender Singh, Mohd Ali Bin Naser, Jager Cooper, Cameron Selci, Evan Best

| Agenda Item | Brief Description |
|-----|-----|
| Code Review for current PRs | Did a bunch of code reviews during our discord meeting on March 9th. During the review process, Devender's PR from a feature branch named "31-create-game---need-a-function-to-return-list-of-users-from-db" was sent back for changes due a concern brought up during the meeting. The requested changes were quickly made and merged successfully. |
| Current Kanban Board & Issues | The team briefly reviewed the current kanban board and the issues that are currently open to access the progress of the team. A new concern was address during the meeting regarding the current process of username retrevals when the project scales.  |
| Discussion for multiplayer functionality | The team discussed how we are going to implement multiplayer functionality without using advanced topics such as sockets. |
| Sprint 1 Marking Scheme Review | The team briefly reviewed and discussed the sprint 1 marking scheme how the team should proceed in order to comply with some of the requirements mentioned |
| Completion of a task by next meeting | The team members have decided to try and complete a minimum of one task and make PRs before the next team meeting to have some PRs to review and discuss. |
| New Tabular Section in the Meeting Notes | The team agreed that a better way to organize the agenda items and its dicussions of the meeting notes would be to have a tabular format in the notes. |
| Perfomance review  | Touched upon this this topic - will be discussed in detail on the next meeting |

## March 11th, 2024

**Scrum master rotation:** Mohd Ali Bin Naser -> Jager Cooper -> Cameron Selci -> Devender Singh -> Evan Best

**Note taker Rotation:** Jager Cooper -> Evan Best -> Mohd Ali Bin Naser -> Devender Singh -> Cameron Selci

**Scrum Master:** Mohd Ali Bin Naser

**Recorded by:** Devender Singh

**Venue:** EN 2036

**Time:** 2:00pm to 3:10pm

**Attendance:**  Devender Singh, Mohd Ali Bin Naser, Jager Cooper, Cameron Selci, Evan Best

| Agenda Item | Brief Description |
|-----|-----|
| Performance Review |  The team reviewed how the performance review will be conducted for our sprint. This included discussions on metrics and feedback mechanisms to ensure continuous improvement. |
| Code Reviews    | The team briefly performed various Code Reviews specifically discussed and approved Jager Cooper's code. The review focused on adherence to project standards, and integration with existing codebases. |
| Kanban Board Updates  | Updates were made to the kanban board to reflect the latest changes, including completed tasks and newly identified issues. |
| Process Model Documentation Discussion  | The team discussed the process model documentation that the professor uploaded on the webpage on Monday in detail.  |
| Backend Discussion   |A focused discussion between Evan and Devender on backend functionality, covering specific implementations, potential challenges, and strategies for efficient data handling on backend side. |

## March 13th, 2024

**Scrum master rotation:** Mohd Ali Bin Naser -> Jager Cooper -> Cameron Selci -> Devender Singh -> Evan Best

**Note taker Rotation:** Jager Cooper -> Evan Best -> Mohd Ali Bin Naser -> Devender Singh -> Cameron Selci

**Scrum Master:** Jager Cooper

**Recorded by:** Cameron Selci

**Venue:** Discord Voice / Screen Sharing

**Time:** 2:00pm to 3:10pm

**Attendance:**  Devender Singh, Mohd Ali Bin Naser, Jager Cooper, Cameron Selci, Evan Best

| Agenda Item | Brief Description |
|-----|-----|
| Performance Review |  Discussed dabout individual performance reviews. |
| Code Reviews    | Devenders code hashing and unique gameid. Code reviews for Evan and Cameron save board, player turn. Discussed more about code reviews. Ali's code on UI/CSS.  |
| Kanban Board Updates  | Updates were made to the kanban board to reflect the latest changes, including completed tasks and newly identified issues. New tasks posted. |
| Functionality | More talk about interactions. Devender & Cooper mainly gameid, Cameron and Evan mainly saving board. Devender and Ali UI. |

## March 15th, 2024

**Scrum master rotation:** Mohd Ali Bin Naser -> Jager Cooper -> Cameron Selci -> Devender Singh -> Evan Best

**Note taker Rotation:** Jager Cooper -> Evan Best -> Mohd Ali Bin Naser -> Devender Singh -> Cameron Selci

**Scrum Master:** Cameron Selci

**Recorded by:** Jager Cooper

**Venue:** Discord Voice / Screen Sharing

**Time:** 2:00pm to 2:20pm

**Attendance:**  Devender Singh, Mohd Ali Bin Naser, Jager Cooper, Cameron Selci, Evan Best

| Agenda Item | Brief Description |
|-----|-----|
| Plan for submission day | Planned a long meeting for the 16th of march, to compile final documentation needed, address any last minute issues, final code reviews, and step by step walkthrough of the grading scheme|

## March 16th, 2024

**Scrum master rotation:** Mohd Ali Bin Naser -> Jager Cooper -> Cameron Selci -> Devender Singh -> Evan Best

**Note taker Rotation:** Jager Cooper -> Evan Best -> Mohd Ali Bin Naser -> Devender Singh -> Cameron Selci

**Scrum Master:** Jager Cooper

**Recorded by:** Evan Best

**Venue:** Discord Voice / Screen Sharing

**Time:** 7:30pm to 12:00am

**Attendance:**  Devender Singh, Mohd Ali Bin Naser, Jager Cooper, Cameron Selci, Evan Best

| Agenda Item | Brief Description |
|-----|-----|
| Long End Of Sprint Meeting | Conducted a long meeting to fix issues, make required documents, and update files |

## March 20th, 2024

**Scrum master rotation:** Mohd Ali Bin Naser -> Jager Cooper -> Cameron Selci -> Devender Singh -> Evan Best

**Note taker Rotation:** Jager Cooper -> Evan Best -> Mohd Ali Bin Naser -> Devender Singh -> Cameron Selci

**Scrum Master:** Cameron Selci

**Recorded by:** Mohd Ali Bin Naser

**Venue:** Discord Voice / Screen Sharing

**Time:** 2pm to 2:55pm

**Attendance:**  Devender Singh, Mohd Ali Bin Naser, Jager Cooper, Cameron Selci, Evan Best

| Agenda Item | Brief Description |
|-----|-----|
| new expectations for Sprint 2 | The team went over the documentation for new expectations for the Sprint 2 |
| Things that went wrong during Sprint 1 | As part of the team assessment during the meeting today, we went through a bunch of stuff that went wrong during the first iteration of the Sprint and how we'll process to ensure such things don't happen during Sprint 2 |
| Kanban Board and Issues Review | As a team, we went through the project Kanban board to assess our progress and also discussed about the some pending task from Spring 1 that'll be incorporated in Sprint 2 |
| Initial Priorities | As part of the team assessment, we also briefly discussed issues and task that we should prioritize during the initial phase of Sprint 2 so that we're on track |

## March 23rd, 2024

**Scrum master rotation:** Mohd Ali Bin Naser -> Jager Cooper -> Cameron Selci -> Devender Singh -> Evan Best

**Note taker Rotation:** Jager Cooper -> Evan Best -> Mohd Ali Bin Naser -> Devender Singh -> Cameron Selci

**Scrum Master:** Devender Singh

**Recorded by:** Evan Best

**Venue:** Discord Voice / Screen Sharing

**Time:** 10:00pm - 11:30pm

**Attendance:**  Devender Singh, Mohd Ali Bin Naser, Jager Cooper, Cameron Selci, Evan Best

| Agenda Item | Brief Description |
|-----|-----|
| Discuss errors | The team talked about the errors being thrown by our tests. Went over them one by one over screen share, and addressed them as required. |
| Working product | As a team, we went through what we needed to do to get our modules working correctly together, to achieve a working product by March 28. |
| Possible improvements | Discussed possible features that can be added after achieving a working product.|
|Pull request deadline | Set the pull request deadline to be April 4th, 2024.|

## March 25th, 2024

**Scrum master rotation:** Mohd Ali Bin Naser -> Jager Cooper -> Cameron Selci -> Devender Singh -> Evan Best

**Note taker Rotation:** Jager Cooper -> Evan Best -> Mohd Ali Bin Naser -> Devender Singh -> Cameron Selci

**Scrum Master:** Evan Best

**Recorded by:** Devender Singh

**Venue:** Discord Voice / Screen Sharing

**Time:** 2:00pm to 3:30pm

**Attendance:** Devender Singh, Mohd Ali Bin Naser, Jager Cooper, Cameron Selci, Evan Best

| Agenda Item       | Brief Description |
|-------------------|-------------------|
| Code Reviews      | The team conducted code reviews. We reviewed some of the code, focusing particularly on Evan's contributions, which required some changes. After re-evaluation, these changes were approved and merged. |
| Grading Discussion | Discussed the grading criteria and marking in detail for Sprint 1. The team aimed to ensure no points were lost unnecessarily and reviewed the grading scheme closely. |
| Meeting with the Professor | Jager Cooper took the initiative to schedule a meeting with the professor for Wednesday, April 12th, just before our next team meeting. This will help us clarify expectations and get feedback. |
| New Front-End Design | Ali presented a new and improved front-end design that incorporates player stats and a leaderboard on the same page. The team was impressed with the visual appeal and functionality improvements. |

The meeting was productive, with significant progress made on code reviews and strategic planning for Sprint 1 grading. The decision to meet with the professor is expected to provide valuable insights. 

## March 27th, 2024

**Scrum master rotation:** Mohd Ali Bin Naser -> Jager Cooper -> Cameron Selci -> Devender Singh -> Evan Best

**Note taker Rotation:** Jager Cooper -> Evan Best -> Mohd Ali Bin Naser -> Devender Singh -> Cameron Selci

**Scrum Master:** Mohd Ali Bin Naser

**Recorded by:** Jager Cooper

**Venue:** EN2036 + Profs office

**Time:** 12:10pm to 2:00pm

**Attendance:** Devender Singh, Mohd Ali Bin Naser, Jager Cooper

| Agenda Item       | Brief Description |
|-------------------|-------------------|
| Meeting with Prof. | The Team had a meeting with the professor about the grading for group sprint 1, discussed some areas where we had met the requirements, we now need to craft an email outlining the areas where we feel we should have gotten the grades as well as where to look or what arguments we have for this. |
| Code Review | Reviewed open PR's and merged them into the master branch - rejected the PR of a team member who did not attend as per the code review process. |
| Additional features | Discussed possible implementation requirements for leaderboard, and player statistics display on the user's main page. |

## March 29th, 2024

**Scrum master rotation:** Mohd Ali Bin Naser -> Jager Cooper -> Cameron Selci -> Devender Singh -> Evan Best

**Note taker Rotation:** Jager Cooper -> Evan Best -> Mohd Ali Bin Naser -> Devender Singh -> Cameron Selci

**Scrum Master:**  Jager Cooper

**Recorded by:** Cam Selci

**Venue:** Discord/Screen Sharing

**Time:** 11:00am to 5:10pm

**Attendance:** Devender Singh, Mohd Ali Bin Naser, Jager Cooper, Cameron Selci, Evan Best

| Agenda Item       | Brief Description |
|-------------------|-------------------|
| Error Handling | Frontend and applogic coordinate dependency.  |
| Error Handling | Store, user, and server interaction. Focus on errors. |
| Error Handling | Store to remove players in gamestate saves. |
| Code Review | Went over Applogic, added return boolean for server interaction.  |
| Code Review | Getting Applogic and gamepage coordinates to work together. |
| Code Review | Store, user, and server interaction. |
| Code Review | Reset functionality page and functionality. |
| General note | Members reviewed PRs as needed and we merged as necessary. |
| Additional Features | Discussed more implementations such as win and loss storage. Store to create a method for gamestate saving wins and losses. |

## April 2nd, 2024

**Scrum master rotation:** Mohd Ali Bin Naser -> Jager Cooper -> Cameron Selci -> Devender Singh -> Evan Best

**Note taker Rotation:** Jager Cooper -> Evan Best -> Mohd Ali Bin Naser -> Devender Singh -> Cameron Selci

**Scrum Master:**  Cameron Selci

**Recorded by:** Jager Cooper

**Venue:** Discord/Screen Sharing

**Time:** 1:00pm to 3:00pm

**Attendance:** Devender Singh, Mohd Ali Bin Naser, Jager Cooper, Cameron Selci, Evan Best

| Agenda Item       | Brief Description |
|-------------------|-------------------|
| Discussion | discussed trying to test our game on two browsers, and therefore implementing page refresh and board permissions.   |
| New Issue | DB; Add a `create_game()` method for the user module to use, refactor `save_game()` to remove playerid parameters |
| Code Review | Frontend; Implemented dynamic leadboard data on the front, reviewed and accepted by the team. |
| Code Review | User module; Added leaderboard functionality and unit tests, Reviewed, code execution is good, however this PR has been rejected due to new design decisions being currently implemented in the database. |
| Code Review | User module; Gather currently active games, reviewed and accepted by the team.  |
| Code Review | Store; changed path of shelve db, reviewed and accepted by the team. |
| New Issue | Store; need to update the remove_game method to take an extra parameter of the player who won so that the players involved can have their win/loss/draw histories updated |
| New Issue | API/Applogic; need to refactor `check_game_state()` and `make_move()` so that we dont get caught in a trap of trying to load a finished game after its deleted. |
| New Issue | API/Frontend; Implement adding error messages to the front-end when things are incorrect. |
| New Issue | Lock the game for a user whos turn it is not |
| User Stories | Everyone in the team document a user story |
| Game Framework | Everyone take the time between now and our next meeting to reflect on what changes need to be made to their individual modules. |
| Performance Review | Everyone complete the performance reviews for each other member between now and our next meeting |
| Next meeting | Marathon meeting planned for thursday to finalize the requirements for the project submission on friday. |

## April 4th, 2024

**Scrum master rotation:** Mohd Ali Bin Naser -> Jager Cooper -> Cameron Selci -> Devender Singh -> Evan Best

**Note taker Rotation:** Jager Cooper -> Evan Best -> Mohd Ali Bin Naser -> Devender Singh -> Cameron Selci

**Scrum Master:**  Devender Singh

**Recorded by:** Evan Best

**Venue:** Discord/Screen Sharing

**Time:** 1:00pm to 5:00pm

**Attendance:** Devender Singh, Mohd Ali Bin Naser, Jager Cooper, Cameron Selci, Evan Best

| Agenda Item       | Brief Description |
|-------------------|-------------------|
| Discussion | Discussed the final steps in completing the project. Need to focus on finishing up the coding portion of the project, as well as the documents.   |
| Code Review | Frontend; Ali made necessary changes to the frontend. His PR was reviewed and accepted by the team. |
| Code Review | Server API; Jager updated his module, his changes were reviewed and accepted by the team.  |
| Performance Review | Everyone complete the performance reviews today.|
| Documents | Need to complete all required documents for the sprint. |
| Kanban Board | Reviewed what issues are left on the Kanban Board, and adjusted accordingly.|
| Deadline | Decided that no more code will be written, however team members are free to update their documentation as needed. |
