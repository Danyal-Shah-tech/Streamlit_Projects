import streamlit as st

# Set the title of the app
st.title("🧮 Simple Calculator")

# Set up the layout with columns
col1, col2 = st.columns(2)

# Create input fields for numbers in separate columns
with col1:
    number1 = st.number_input("Enter the first number", value=0.0, format="%.2f")

with col2:
    number2 = st.number_input("Enter the second number", value=0.0, format="%.2f")

# Create a horizontal line
st.markdown("---")

# Create a row of buttons for each operation
operation = st.selectbox(
    "Choose an operation",
    ("Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)")
)

# Calculate the result based on the selected operation
if operation == "Addition (+)":
    result = number1 + number2
elif operation == "Subtraction (-)":
    result = number1 - number2
elif operation == "Multiplication (×)":
    result = number1 * number2
elif operation == "Division (÷)":
    if number2 != 0:
        result = number1 / number2
    else:
        result = "Error: Division by zero"

# Display the result in a highlighted box
st.markdown("### Result:")
st.success(f"{result}")

# Add a footer
st.markdown("""
    ---
    Created by: Danyal Shah
""")

