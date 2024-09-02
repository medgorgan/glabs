import cv2
import datetime

# Load the Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize the camera
camera = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = None  # VideoWriter object, initialized when face is detected

recording = False  # Flag to indicate if recording has started

while True:
    # Capture frame-by-frame
    ret, frame = camera.read()
    if not ret:
        break
    
    # Convert frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    # If a face is detected, start recording
    if len(faces) > 0:
        if not recording:
            # Start recording when a face is detected
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            out = cv2.VideoWriter(f'face_detected_{timestamp}.avi', fourcc, 20.0, (frame.shape[1], frame.shape[0]))
            recording = True
        
        # Write the frame into the file
        out.write(frame)
    else:
        # Stop recording when no faces are detected
        if recording:
            recording = False
            out.release()
            out = None
    
    # Display the resulting frame
    cv2.imshow('Video Feed', frame)
    
    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close windows
camera.release()
if out is not None:
    out.release()
cv2.destroyAllWindows()
