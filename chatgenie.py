import google.generativeai as genai
import streamlit as st

# Configure the API key
genai.configure(api_key="AIzaSyAQKuYgRUUYyJiiqrXLoW0Hmx-UVb_OcsA")

# Initialize the Generative Model
model = genai.GenerativeModel('gemini-1.5-flash')

# Function to get response from the model
def getResponseFromModel(user_input):
    response = model.generate_content(user_input)
    return response.text

# Streamlit UI
st.set_page_config(page_title="ChatGenie", page_icon=":robot:", layout="wide")
st.title("🧞‍♂️ ChatGenie 🧞‍♂️")
st.write("**Welcome to ChatGenie!** Your personal chatbot powered by the Gemini LLM Model.")

# Define a sidebar for additional features and information
st.sidebar.header("ChatGenie Features")
st.sidebar.write("""
- **Real-time responses**: Get instant answers to your queries.
- **Multi-turn conversations**: Continue your chat seamlessly.
- **Customization options**: Adjust the model's behavior through settings.
""")

# Create a chat history container
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Function to handle user input and responses
def handle_input(user_input):
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        response = getResponseFromModel(user_input)
        st.session_state.messages.append({"role": "assistant", "content": response})

# Display the chat history
for message in st.session_state.messages:
    if message['role'] == 'user':
        st.markdown(f"<div style='text-align: right; background-color: #e1f5fe; border-radius: 10px; padding: 10px;'><strong>You:</strong> {message['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='text-align: left; background-color: #f1f8e9; border-radius: 10px; padding: 10px;'><strong>ChatGenie:</strong> {message['content']}</div>", unsafe_allow_html=True)

# Streamlit form for user input
with st.form(key='Chat_Form', clear_on_submit=True):
    user_input = st.text_input("Type your message here:", max_chars=2000)
    submit_button = st.form_submit_button("Send ➡️")

    if submit_button:
        handle_input(user_input)

# Optional: Add a button to clear chat history
if st.button("Clear Chat History"):
    st.session_state.messages = []
    st.experimental_rerun()
