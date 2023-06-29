import streamlit as st
import requests
import json


def main():
    st.title("API Frontend")
    url_API =st.text_input("inserisci url dell'api","http://localhost:8000/predict")
    rdspend = st.number_input("Inserisci rdspend")
    administration = st.number_input("Inserisci administration")
    marketing = st.number_input("Inserisci marketing")



    if st.button("Predict with GET"):
        url = url_API
        url2 = f"?rdspend={rdspend}&administration={administration}&marketing={marketing}"
        link = url+url2
        st.write('"{}"'.format(link))
        response = requests.get(link)
        result =response.json()
        st.success(f"The result is: {result}")





    if st.button("Predict with POST"):
        url = url_API
        response =requests.post(url,
                                headers={"Content-Type": "application/json"},
                                data = json.dumps({
                                                   "rdspend":rdspend,
                                                   "administration":administration,
                                                   "marketing":marketing,
                                                   })
                                )
        result =response.json()
        st.success(f"The result is: {result}")



if __name__ == "__main__":
    main()