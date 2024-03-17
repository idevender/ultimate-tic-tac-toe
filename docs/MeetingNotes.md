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
| Long End Of Spring Meeting | Conducted a long meeting to fix issues, make required documents, and update files |
