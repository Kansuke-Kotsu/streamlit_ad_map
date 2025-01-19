import requests
import streamlit as st
import streamlit_authenticator as sa

# Using Streamlit for a better user interface 
st.title("Ad Search")
 

def invoke_lambda(api_gateway_url, payload):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url=api_gateway_url, json=payload, headers=headers)
    response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
    result = response.json()
    print(result)
    try:
        for i in range(3):
            # AWSから情報を取得
            name = result[f"ad_name_{i+1}"]
            detail = result[f"as_detail_{i+1}"]
            st.write(name)
            st.write(detail)
            st.write("")
    except:
        st.write(result["message"])


input_1 = st.text_input("ID")
input_2 = st.text_input("Password")

if st.button("Search"): # 検索ボタンを追加
        # リクエストペイロード (必要に応じて)
        payload = {
            "key1": input_1,
            "key2": input_2,
        }

        invoke_lambda(
            api_gateway_url = "https://11l79ngo06.execute-api.ap-northeast-1.amazonaws.com/dev/instagram_test",
            payload=payload
            )