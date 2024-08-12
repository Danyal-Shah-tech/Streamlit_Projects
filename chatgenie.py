import streamlit as st
import google.generativeai as genai

# Configure the Generative AI model
genai.configure(api_key="AIzaSyAQKuYgRUUYyJiiqrXLoW0Hmx-UVb_OcsA")

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-flash')

# Function to generate a response from the model
def generate_response(prompt):
    response = model.generate_content(prompt)
    return response.text

# Streamlit UI
st.title("🤖 ChatGenie with Google Gemini")

st.sidebar.header("ChatGenie Features")
st.sidebar.write("""
- **Real-time responses**: Get instant answers to your queries.
- **Multi-turn conversations**: Continue your chat seamlessly.
- **Customization options**: Adjust the model's behavior through settings.
""")

# Define session state variables
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "user_input" not in st.session_state:
    st.session_state.user_input = ""
if "form_submitted" not in st.session_state:
    st.session_state.form_submitted = False

# Custom CSS for styling
st.markdown("""
    <style>
    .input-box {
        position: fixed;
        bottom: 0;
        width: calc(100% - 20px);
        padding: 10px;
        background-color: #fff;
        border-top: 1px solid #e0e0e0;
        box-shadow: 0 -2px 5px rgba(0,0,0,0.1);
        border-radius: 8px;
    }
    .message {
        border-radius: 8px;
        padding: 8px 12px;
        margin-bottom: 10px;
        max-width: 80%;
        display: inline-block;
    }
    .bot-message {
        background-color: #007bff;
        color: white;
        align-self: flex-start;
    }
    .user-message {
        background-color: #28a745;
        color: white;
        align-self: flex-end;
    }
    </style>
    """, unsafe_allow_html=True)

# Display chat history
st.markdown('<div class="chat-box">', unsafe_allow_html=True)
for speaker, message in st.session_state.chat_history:
    if speaker == "You":
        st.write(f"👤 **{speaker}:** {message}", unsafe_allow_html=True)
    else:
        st.write(f"🤖 **{speaker}:** {message}", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Input box at the bottom
with st.container():
    with st.form(key='chat_form', clear_on_submit=True):
        st.session_state.user_input = st.text_input("Type your message here... 💬", max_chars=1000)
        submit_button = st.form_submit_button("Send 📤")
        
        if submit_button:
            if st.session_state.user_input:
                st.session_state.form_submitted = True
            else:
                st.warning("Please enter a message before sending. 🚫")

if st.session_state.form_submitted:
    response = generate_response(st.session_state.user_input)
    st.session_state.chat_history.append(("You", st.session_state.user_input))
    st.session_state.chat_history.append(("ChatBot", response))
    st.session_state.form_submitted = False  # Reset flag after handling

# Button to clear chat history
if st.button("Clear Chat 🧹"):
    st.session_state.chat_history = []
