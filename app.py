import streamlit as st
from ai_email_generator import generate_email
from fallback_templates import fallback_email
from email_sender import send_email

st.set_page_config(page_title="AI Email Replyer", layout="centered")

st.title("📧 AI Email Replyer & Sender")

# -------------------------------
# Email Generation Section
# -------------------------------

context = st.text_area("Email context / requirement", height=120)

tone = st.selectbox(
    "Select Email Tone",
    ["Professional", "Formal", "Friendly", "Follow-up", "Apology", "Request"]
)

extra = st.text_input("Extra instructions (optional)")

# Generate Email
if st.button("Generate Email"):
    if context.strip():
        with st.spinner("Generating email..."):
            email_text = generate_email(context, tone, extra)

            # If AI busy or fails → fallback template
            if email_text.startswith("⚠️") or not email_text.strip():
                st.info("AI busy. Using smart template instead.")
                email_text = fallback_email(context, tone, extra)

            # Always store email so it shows
            st.session_state["email_body"] = email_text
    else:
        st.warning("Please enter email context.")

# -------------------------------
# Show Generated Email
# -------------------------------

st.subheader("Generated Email")

email_preview = st.text_area(
    "Email Content (You can edit before sending)",
    value=st.session_state.get("email_body", ""),
    height=260
)

# -------------------------------
# Send Email Section
# -------------------------------

st.subheader("Send Email")

sender = st.text_input(
    "Your Gmail address",
    placeholder="example@gmail.com"
)

password = st.text_input(
    "Gmail App Password (NOT your Gmail password)",
    type="password"
)

receiver = st.text_input(
    "Receiver Email",
    placeholder="hr@company.com"
)

subject = st.text_input(
    "Email Subject",
    placeholder="Job Application – Software Developer"
)

# Attachment (optional)
attachment = st.file_uploader(
    "Attach file (Optional – Resume / Document)",
    type=["pdf", "docx", "txt"]
)

# Send Email
if st.button("Send Email"):
    if not email_preview.strip():
        st.warning("Please generate or write email content first.")
    elif not (sender and password and receiver and subject):
        st.warning("Please fill all email sending fields.")
    else:
        try:
            send_email(
                sender,
                password,
                receiver,
                subject,
                email_preview,
                attachment
            )
            st.success("✅ Email sent successfully!")
        except Exception as e:
            st.error(f"❌ Failed to send email: {e}")
