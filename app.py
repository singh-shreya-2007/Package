import streamlit as st
import joblib

model=joblib.load('placement.pkl')

def main():
    st.title("welcome to placement predictor")
    cgpa=st.slider("Choose your cgpa from slider",min_value=0.0, max_value=10.0,step=0.1)
    st.write("entered cgpa",cgpa)

    if st.button("Predict"):
        result=model.predict([[cgpa]])
        st.success(f"your package will be {result}")


if __name__=='__main__':
    main()