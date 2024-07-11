# ParcelHive Project

## Setup Instructions

---

1. Create a directory for the project and navigate to it:
   
     ```mkdir parcelhive_test```
   
     ```cd parcelhive_test```
   
2. Clone the project:
   
   ```git clone https://github.com/BlackRock17/parcelhive-project.git```
   
   ```cd parcelhive-project```

3. Create a virtual environment:

   - Windows:
     
     ```python -m venv venv```

   - Linux ubunto:
  
     ```python3 -m venv venv```

4. Activate the virtual environment:

   - Windows:
    
     ```venv\Scripts\activate```
    
   - Linux ubunto:
  
     ```source venv/bin/activate```

5. Install dependencies:

   ```pip install -r requirements.txt```

6. Apply migrations:

   ```python manage.py migrate```

7. Start the server:

   ```daphne parcelhive.asgi:application```

## Testing the Application

1. Open a browser and navigate to http://localhost:8000

2. Test the functionality:
- Move the mouse within the canvas element
- Left-click to take a picture with the webcam (you can do this multiple times within the canvas element)

3. Stop the server with Ctrl+C

4. In the main directory (parcelhive-project), a new 'media' directory will be created dynamically, and within it, a 'mouse_clicks' directory. You can find the pictures you've taken there.

5. In the database, in the 'mouse_tracker_mouseclick' table, you can find the information you need for the mouse coordinates at the moment each picture was taken ('x', 'y'), 'photo' contains the path to the picture, 'timestamp' contains the time the picture was taken.

If you have any questions or difficulties with starting up, please contact me at tel. 0895028398 or email: lyyubo@gmail.com

Thank you!


