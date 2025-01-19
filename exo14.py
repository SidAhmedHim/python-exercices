word = str(input("Word: "))
frame_width = 30
padding = (frame_width - len(word)) // 2

print("*" * frame_width)     # Top border
print("*" + " " * (frame_width - 2) + "*")  # Empty row
print("*" + " " * (padding-1)+ word + " " * (frame_width - len(word) - padding - 1) + "*")  # Centered row
print("*" + " " * (frame_width - 2) + "*")  # Empty row
print("*" * frame_width)                # Bottom border
