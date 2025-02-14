import streamlit as st
import os
from openai import OpenAI

def show_chat_section():
    st.markdown("---")
    st.subheader("💬 Ask a Question")
    
    # Initialize chat history in session state if not present
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Display chat history
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Chat input
    if prompt := st.chat_input("Ask a question about your health insurance options..."):
        # Add user message to chat history
        st.session_state.chat_history.append({"role": "user", "content": prompt})

        # Display user message
        with st.chat_message("user"):
            st.write(prompt)

        # Get AI response
        try:
            client = OpenAI(api_key="")
            
            system_prompt = """You are a friendly and supportive chat assistant for the 'Metro-Montessori Group Medical Assistance App.' Your primary goal is to guide Montessori employees through selecting or changing their medical plan, explaining coverage details, and answering other health insurance-related questions. Please be clear, approachable, and use simple language to help them understand their options.

            Keep in mind:
            • You represent Metro Insurance and should reference this branding when appropriate.
            • This information is for demonstration and illustrative purposes only. Always remind users to refer to their employee packet and official health plan documents for complete details.
            • If questions are highly specific or require legal/medical advice, suggest they consult a licensed professional or their HR representative.

            Please maintain a warm, patient, and friendly tone, given the audience is primarily preschool teachers and administrative staff. Provide concise yet thorough answers to their application and coverage inquiries, ensuring they feel supported throughout the process."""

            messages = [
                {"role": "system", "content": system_prompt}
            ]
            
            # Add chat history
            for msg in st.session_state.chat_history:
                messages.append({"role": msg["role"], "content": msg["content"]})

            # Get response
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0.7,
                max_tokens=500
            )

            # Display assistant response
            with st.chat_message("assistant"):
                message = response.choices[0].message.content
                st.write(message)

            # Add assistant response to chat history
            st.session_state.chat_history.append({"role": "assistant", "content": message})

        except Exception as e:
            st.error(f"Sorry, I couldn't process your question. Please try again later. Error: {str(e)}")

    # Add clear chat button
    if st.session_state.chat_history and st.button("Clear Chat"):
        st.session_state.chat_history = []
        st.rerun() 