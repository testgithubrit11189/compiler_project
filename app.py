import streamlit as st
import traceback
from converterfunc import C_Code_Generator, Input

st.title("🧠 NLP-based Pseudocode to C Code Translator")
st.write("Enter your pseudocode below:")

# Input box
user_input = st.text_area("Pseudocode", height=300)

# Button to convert
if st.button("🔁 Convert to C Code"):
    if user_input.strip() == "":
        st.warning("Please enter some pseudocode.")
    else:
        try:
            result = C_Code_Generator(Input(message=user_input))
            st.subheader("✅ Generated C Code:")
            st.code(result.c_code, language='c')
        except Exception as e:
             st.error("❌ An error occurred while converting your pseudocode.")

             if "Undeclared variables used:" in str(e):
                undeclared = str(e).split(":")[1].strip()
                st.warning(f"🚫 Undeclared variables detected: `{undeclared}`")
                st.markdown("**💡 Hint:** Make sure all variables are declared using `assign(var type)` or similar.")
             else:
                st.markdown("**💡 Possible issues:**")
                st.markdown("""
                - Make sure **all variables are declared** before they are used.
                - Check that **keywords like `assign`, `if`, `print`, `read`, `for`** are present or similar.
                - Avoid unsupported structures like nested functions.
                """)
                with st.expander("🔍 View error details"):
                    st.text(traceback.format_exc())
