import streamlit as st
from PIL import Image
from rag.retriever import retriever_context
from image_generation.generator import generate_image


# PAGE CONFIG
st.set_page_config(
    page_title="AI Image Generator",
    page_icon="🎨",
    layout="wide"
)


# CUSTOM CSS
st.markdown("""
<style>

/* Main Background */
.stApp {
    background-color: #f8fafc;
}

/* Title */
.title {
    text-align: center;
    font-size: 52px;
    font-weight: bold;
    color: #2563eb;
    margin-bottom: 10px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 20px;
    color: #475569;
    margin-bottom: 35px;
}

/* Section Headings */
h3 {
    color: #1e293b !important;
    font-weight: 700 !important;
}

/* Text Area */
.stTextArea textarea {
    background-color: white !important;
    color: black !important;
    border: 2px solid #2563eb !important;
    border-radius: 12px !important;
    padding: 12px !important;
    font-size: 16px !important;
}

/* File Uploader */
[data-testid="stFileUploader"] {
    background-color: white;
    border-radius: 12px;
    border: 2px solid #e2e8f0;
    padding: 10px;
}

/* Generate Button */
.stButton > button {
    width: 100%;
    background-color: #2563eb;
    color: white;
    font-size: 18px;
    font-weight: bold;
    border-radius: 12px;
    height: 55px;
    border: none;
}

.stButton > button:hover {
    background-color: #1d4ed8;
}

/* Images */
img {
    border-radius: 15px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: white;
}

/* Remove Footer */
footer {
    visibility: hidden;
}

/* Better Labels */
label {
    color: #1e293b !important;
    font-weight: 600 !important;
}

</style>
""", unsafe_allow_html=True)


# HEADER
st.markdown(
    '<div class="title">🎨 AI IMAGE GENERATOR</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Generate Stunning AI Images using RAG + Stable Diffusion</div>',
    unsafe_allow_html=True
)


# LAYOUT
left, right = st.columns([1, 1])


# LEFT SIDE
with left:

    st.subheader("📝 Enter Prompt")

    prompt = st.text_area(
        "",
        height=150,
        placeholder="Example: Create a futuristic city with flying cars and neon lights"
    )

    st.subheader("🖼️ Upload Reference Image (Optional)")

    uploaded_file = st.file_uploader(
        "",
        type=["png", "jpg", "jpeg"]
    )

    image = None

    if uploaded_file is not None:

        image = Image.open(uploaded_file)

        st.image(
            image,
            caption="Uploaded Image",
            use_container_width=True
        )

    generate_btn = st.button("🚀 Generate Image")


# RIGHT SIDE
with right:

    st.subheader("✨ Generated Result")

    if generate_btn:

        if not prompt.strip():

            st.warning("Please enter a prompt.")

        else:

            with st.spinner("Creating masterpiece..."):

                try:

                    # Retrieve context from RAG
                    context = retriever_context(prompt)

                    # Create final prompt
                    final_prompt = f"""
                    User Prompt:
                    {prompt}

                    Style Guide:
                    {context}
                    """

                    # Generate image
                    result = generate_image(final_prompt)

                    # Display result
                    st.image(
                        result,
                        caption="Generated Image",
                        use_container_width=True
                    )

                except Exception as e:

                    st.error(f"Error: {e}")