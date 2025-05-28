# import streamlit as st

# st.title("Unit Convertor App")
# st.markdown("### Convert Length, Weight & Time Instantly")
# st.write("Welcome. Select a Catagory, Enter a value & Get The Converted Result in Real-Time")

# category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])

# def convert_units(category, value, unit):
#     if category == "Length":
#         if unit == "Kilometers to Miles":
#             return value * 0.621371
#         elif unit == "Miles to Kilometers":
#             return value / 0.621371
        
#     elif category == "Weight":
#         if unit == "Kilograms to Pounds":
#             return value * 2.20462
#         elif unit == "Pounds to Kilograms":
#             return value / 2.20462
        
#     elif category == "Time":
#         if unit == "Seconds to Minutes":
#             return value / 60
#         elif unit == "Minutes to Seconds":
#             return value * 60
#         elif unit == "Hours to Minutes":
#             return value * 60
#         elif unit == "Minutes to Hours":
#             return value / 60
#         elif unit == "Hours to Days":
#             return value / 24
#         elif unit == "Days to Hours":
#             return value * 24
        
# if category == "Length":
#     unit = st.selectbox("Select Conversation", ["Kilometers to Miles", "Miles to Kilometers"])

# elif category == "Weight":
#     unit = st.selectbox("Select Conversation", ["Kilograms to Pounds", "Pounds to Kilograms"])

# elif category == "Time":
#     unit = st.selectbox("Select Conversation", ["Seconds to Minutes", "Minutes to Seconds", "Hours to Minutes", "Minutes to Hours", "Hours to Days", "Days to Hours"])

# value = st.number_input("Enter the Value to Convert")
# if st.button("Convert"):
#     result = convert_units(category, value, unit)
#     st.success(f"The result is {result:.2f}")


import streamlit as st

# --- App Title and Intro ---
st.title("🌐 Unit Converter App")
st.markdown("### 📏 Convert Length, ⚖️ Weight, ⏱️ Time & 🌡️ Temperature Instantly")
st.write("Welcome! Select a category, enter a value, and get the converted result in real-time.")

# --- Initialize session history ---
if "history" not in st.session_state:
    st.session_state.history = []

# --- Conversion Function ---
def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371, "Miles"
        elif unit == "Miles to Kilometers":
            return value * 1.60934, "Kilometers"

    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462, "Pounds"
        elif unit == "Pounds to Kilograms":
            return value / 2.20462, "Kilograms"

    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60, "Minutes"
        elif unit == "Minutes to Seconds":
            return value * 60, "Seconds"
        elif unit == "Hours to Minutes":
            return value * 60, "Minutes"
        elif unit == "Minutes to Hours":
            return value / 60, "Hours"
        elif unit == "Hours to Days":
            return value / 24, "Days"
        elif unit == "Days to Hours":
            return value * 24, "Hours"

    elif category == "Temperature":
        if unit == "Celsius to Fahrenheit":
            return (value * 9/5) + 32, "°F"
        elif unit == "Fahrenheit to Celsius":
            return (value - 32) * 5/9, "°C"
        elif unit == "Celsius to Kelvin":
            return value + 273.15, "K"
        elif unit == "Kelvin to Celsius":
            return value - 273.15, "°C"
        elif unit == "Fahrenheit to Kelvin":
            return (value - 32) * 5/9 + 273.15, "K"
        elif unit == "Kelvin to Fahrenheit":
            return (value - 273.15) * 9/5 + 32, "°F"

    return None, None  # Fallback

# --- Category and Unit Selection ---
category = st.selectbox("Choose a category", ["Length", "Weight", "Time", "Temperature"])

unit_options = {
    "Length": ["Kilometers to Miles", "Miles to Kilometers"],
    "Weight": ["Kilograms to Pounds", "Pounds to Kilograms"],
    "Time": [
        "Seconds to Minutes", "Minutes to Seconds",
        "Hours to Minutes", "Minutes to Hours",
        "Hours to Days", "Days to Hours"
    ],
    "Temperature": [
        "Celsius to Fahrenheit", "Fahrenheit to Celsius",
        "Celsius to Kelvin", "Kelvin to Celsius",
        "Fahrenheit to Kelvin", "Kelvin to Fahrenheit"
    ]
}
unit = st.selectbox("Select Conversion", unit_options[category])

# --- Value Input ---
value = st.number_input("Enter the Value to Convert", format="%.4f")

# --- Conversion Trigger ---
if st.button("🔁 Convert"):
    result, result_unit = convert_units(category, value, unit)
    if result is not None:
        input_unit = unit.split(" to ")[0]
        output_text = f"✅ {value:.2f} {input_unit} is equal to {result:.2f} {result_unit}."
        st.success(output_text)
        # Store in session history
        st.session_state.history.append(output_text)
    else:
        st.error("⚠️ Conversion failed. Please check your input and selected units.")

# --- Show History ---
if st.session_state.history:
    st.markdown("### 📜 Conversion History")
    for item in reversed(st.session_state.history):
        st.write("•", item)
