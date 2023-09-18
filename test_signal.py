import numpy as np
import matplotlib.pyplot as plt

# Time values for the x-axis
time = np.linspace(0, 10, 1000)  # Generating 1000 time points from 0 to 10

# Create a sine wave signal with some frequency and amplitude
frequency = 2  # Adjust this for different frequencies
amplitude = 1  # Adjust this for different amplitudes
sine_wave = amplitude * np.sin(2 * np.pi * frequency * time)
print("time",time)
print("sine_wave",sine_wave)



'''import numpy as np
import matplotlib.pyplot as plt

# Time values for the x-axis
time = np.linspace(0, 10, 1000)  # Generating 1000 time points from 0 to 10

# Create a sine wave signal with some frequency and amplitude
frequency = 2  # Adjust this for different frequencies

# Varying amplitude over time
amplitude = np.linspace(0.5, 2.0, len(time))  # Vary amplitude from 0.5 to 2.0 over time
sine_wave = amplitude * np.sin(2 * np.pi * frequency * time)

# Plot the sine wave
plt.plot(time, sine_wave)
plt.title("Sine Wave Signal Variation")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()'''


import numpy as np
import cv2

# Parameters for the sine wave
frequency = 2
time_duration = 10  # seconds
frame_rate = 30  # frames per second
num_frames = int(frame_rate * time_duration)

# Create a video writer
output_filename = "sine_wave_with_varying_amplitude.avi"
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter(output_filename, fourcc, frame_rate, (640, 480))

# Generate sine wave with varying amplitude
time = np.linspace(0, time_duration, num_frames)
amplitude = np.linspace(0.5, 2.0, num_frames)
sine_wave = amplitude * np.sin(2 * np.pi * frequency * time)

for amp, value in zip(amplitude, sine_wave):
    #Create a frame
    frame = np.ones((480, 640, 3), dtype=np.uint8) * 255
    y_position = int((value + 2) * 100)  # Scale amplitude for visualization
    cv2.putText(frame, f"Amplitude: {amp:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    cv2.line(frame, (0, 240), (640, 240), (0, 0, 0), 2)  # Draw x-axis
    cv2.line(frame, (320, 0), (320, 480), (0, 0, 0), 2)  # Draw y-axis
    cv2.circle(frame, (320, y_position), 5, (0, 0, 255), -1)  # Draw point on sine wave
    out.write(frame)

out.release()
cv2.destroyAllWindows()







