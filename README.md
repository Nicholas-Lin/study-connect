# Study Connect

> Find your next study group

Study Connect is our group project for "Project Option 4: Virtual Study-Buddy Finder" for CS 3240. 

[Try out Study Connect](https://study-buddy-finder.herokuapp.com/)

## Tutorial for Grading
1. Go to your profile and add your information! Try adding some UVA courses to your schedule as well.
2. Go to the discussion board and make a post. Try editing and deleting the post. View some other interesting posts.
3. Go to the group feature and create a group of your own.
4. Go to the finder feature and find a study buddy. See if you can message them or add them to your group.
5. In the finder feature, find a group for one of your classes and join it! 

## Features
1. Profile
    - Users can add UVA courses to their profile
    - Users can customize their profile with their own information
    - Users can view other users' profiles
    - Users can message other users'
2. Groups
    - Users can create their own groups for courses
    - Users can join other groups
    - Users can leave groups
    - Groups auto-generate Google Meet links upon creation
3. Finder
    - Users can find users that are in the same course
    - Users can find groups for a course that they are taking
4. Discussion
    - Users can create, edit, and delete their own discussion posts
    - Users can view other users' posts

## How did we satisfy the requirements?
1. Users shall be able to save their course schedule with their account.
    - Users can add courses to their profile. These courses are validated as a valid course using the [UVA Devhub Schedule API on the "/courses" endpoint](https://devhub.virginia.edu/API).
2. Users shall be able to identify where they need the most help and where they can help others.
    - We made the decision to frame our website around the idea that help is mutually provided by way of a study buddy or studdy group in the same class. Therefore, a user can denote that they want help in a class by adding the course to their schedule. If a user explicitly wanted to identify where they needed the most help or where they can provide help, they may do so using the discussion feature.
3. The system shall automatically generate study buddies or study groups or the system shall allow users to form their own groups.
    - Users can form their own groups by creating a group or using the finder feature to identify a group and join it
4. The system shall provide a mechanism for students to meet up virtually (no in person meet ups for this!). Options could include generating Google Meet links, a Discord bot companion app, managing Zoom IDs, etc.
    - Users can message other users by selecting the "message" button when viewing another user's profile. This allows user's to communicate and discuss when to meet up. Additionally, a unique Google Meet link is generated when a group is created.
    - We leveraged the [Google Calendar API](https://developers.google.com/calendar/v3/reference/events) to automatically generate google meet links for each group.

## Notes
- A list of references can be found in [references.txt](references.txt) file