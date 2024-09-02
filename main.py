import streamlit as st
from scraper import scrape_website
from parser import parse_with_mistral
from scraper import (extract_body_content
                      , clean_html
                      , split_dom_content)

st.title("AI Scraper")
url = st.text_input("Enter full URL,include https://")
if st.button("Scrape"):
    st.write(f"Scraping {url}")
    # Call the scraper function here
    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_html(body_content)

    st.session_state.dom_content = cleaned_content

    with st.expander("View DOM content"):
        st.text_area("DOM content", cleaned_content, 300)

    print(cleaned_content)

if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe how you want to parse the content eg in Table format")

    if st.button("Parse"):
        if parse_description:
            st.write("Parsing content...")

        dom_chunks  = split_dom_content(st.session_state.dom_content)
       #parsed_results = parse_with_ollama(parse_description, dom_chunks)
        parsed_results = parse_with_mistral(parse_description, dom_chunks)

        st.write(parsed_results)