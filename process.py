import math

E2_FREQUENCY = 82
A_FREQUENCY = 110
D_FREQUENCY = 146
G_FREQUENCY = 195
B_FREQUENCY = 246
E4_FREQUENCY = 329

# def determine_plucked_string(frequency):
#     print("detected frequency: ", frequency, "Hz")
#     detected_string = "No String Detected"
#     if int(frequency) in range(72,92):
#         detected_string = "E2"
#     if int(frequency) in range(100,120):
#         detected_string = "A"
#     if int(frequency) in range(136,156):
#         detected_string = "D"
#     if int(frequency) in range(185,205):
#         detected_string = "G"
#     if int(frequency) in range(236,256):
#         detected_string = "B"
#     if int(frequency) in range(319, 339):
#         detected_string = "E4"
#     return detected_string

def E2(frequency):
    if abs(int(frequency) - E2_FREQUENCY) < 3:
        print("E2 is tuned correctly!")
    else:
        if int(frequency) > E2_FREQUENCY:
            print("tune down by " + str(abs(int(frequency) - E2_FREQUENCY)) + "hz")
        else:
            print("tune up by " + str(abs(int(frequency) - E2_FREQUENCY)) + "hz")

def A(frequency):
    if abs(int(frequency) - A_FREQUENCY) < 3:
        print("A is tuned correctly!")
    else:
        if int(frequency) > A_FREQUENCY:
            print("tune down by " + str(abs(int(frequency) - A_FREQUENCY)) + "hz")
        else:
            print("tune up by " + str(abs(int(frequency) - A_FREQUENCY)) + "hz")

def D(frequency):
    if abs(int(frequency) - D_FREQUENCY) < 3:
        print("D is tuned correctly!")
    else:
        if int(frequency) > D_FREQUENCY:
            print("tune down by " + str(abs(int(frequency) - D_FREQUENCY)) + "hz")
        else:
            print("tune up by " + str(abs(int(frequency) - D_FREQUENCY)) + "hz")

def G(frequency):
    if abs(int(frequency) - G_FREQUENCY) < 3:
        print("G is tuned correctly!")
    else:
        if int(frequency) > G_FREQUENCY:
            print("tune down by " + str(abs(int(frequency) - G_FREQUENCY)) + "hz")
        else:
            print("tune up by " + str(abs(int(frequency) - G_FREQUENCY)) + "hz")

def B(frequency):
    if abs(int(frequency) - B_FREQUENCY) < 3:
        print("B is tuned correctly!")
    else:
        if int(frequency) > B_FREQUENCY:
            print("tune down by " + str(abs(int(frequency) - B_FREQUENCY)) + "hz")
        else:
            print("tune up by " + str(abs(int(frequency) - B_FREQUENCY)) + "hz")

def E4(frequency):
    if abs(int(frequency) - E4_FREQUENCY) < 3:
        print("E4 is tuned correctly!")
    else:
        if int(frequency) > E4_FREQUENCY:
            print("tune down by " + str(abs(int(frequency) - E4_FREQUENCY)) + "hz")
        else:
            print("tune up by " + str(abs(int(frequency) - E4_FREQUENCY)) + "hz")
