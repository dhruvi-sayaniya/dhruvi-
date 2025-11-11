import streamlit as st

st.set_page_config(page_title="Streamlit Launcher", layout="centered")

st.title("Streamlit App Launcher")
st.write("Use this simple page to create a big, friendly button that opens your deployed Streamlit app in a new tab.")

# Let the user paste their deployment URL (or a placeholder)
deployment_url = st.text_input("Deployment URL (paste your Streamlit app URL here)", "https://your-deployment-url.example")

st.write("\n")

# Large clickable button that opens the URL in a new tab
if deployment_url and deployment_url.strip() != "":
    html_button = f"""
    <div style='text-align:center; margin-top:20px;'>
      <a href="{deployment_url}" target="_blank" rel="noopener noreferrer">
        <div style='display:inline-block; padding:18px 36px; border-radius:12px; box-shadow:0 6px 18px rgba(0,0,0,0.12); font-weight:700; font-size:18px;'>
          Click Here To Visit Streamlit Web App
        </div>
      </a>
    </div>
    """
    st.markdown(html_button, unsafe_allow_html=True)
else:
    st.warning("Please enter your deployment URL above to enable the button.")

st.markdown("---")

st.header("Preview / Quick info")
st.write("When you click the button it will open the deployment URL in a new tab. If you don't have a deployed URL yet, you can run this app locally and preview features here.")

st.subheader("How to run locally")
st.code("pip install streamlit\nstreamlit run streamlit_app.py")

st.subheader("Deployment tips")
st.write("Deploy on Streamlit Community Cloud or any hosting that supports Python/Flask apps. Once deployed, paste the deployed URL into the box above so the button will open it.")

st.write("\n")

st.caption("Created with ❤️ — replace the placeholder URL with your real app link.")
