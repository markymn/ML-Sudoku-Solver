import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video capture.")
    exit()

print("Press 'q' to quit.")

frame_rate = 30

cap.set(3, 1000)
cap.set(4, 800)

cap.set(10, 100)

while True:
    # Capture each frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Unable to capture video frame.")
        break

    # Display the frame
    cv2.imshow('Video Capture', frame)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
