import streamlit as st
from scraper import scrape_website, extract_body_content, clean_html, split_dom_content
from parser import parse_with_mistral
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

st.title("AI Scraper")
url = st.text_input("Enter full URL, include https://")

if st.button("Scrape"):
    st.write(f"Scraping {url}")
    
    try:
        result = scrape_website(url)
        
        if result and not result.startswith("Error"):
            st.success("Website scraped successfully")
            body_content = extract_body_content(result)
            cleaned_content = clean_html(body_content)

            st.session_state.dom_content = cleaned_content

            with st.expander("View DOM content"):
                st.text_area("DOM content", cleaned_content, height=300)

            logger.info("Content cleaned and stored in session state")
        else:
            st.error(f"Failed to scrape the website: {result}")
            st.error("Please check the URL and try again.")
            logger.error(f"Scraping failed: {result}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {str(e)}")
        logger.exception("Unexpected error in scraping process")

if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe how you want to parse the content e.g., in Table format")

    if st.button("Parse"):
        if parse_description:
            st.write("Parsing content...")

        dom_chunks = split_dom_content(st.session_state.dom_content)
        parsed_results = parse_with_mistral(parse_description, dom_chunks)

        st.write(parsed_results)