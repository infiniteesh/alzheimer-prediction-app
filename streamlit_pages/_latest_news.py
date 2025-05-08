import html
import requests
import streamlit as st
from datetime import datetime
from config import DEFAULT_IMAGE, NEWS_API_KEY as API_KEY
from streamlit.runtime.media_file_storage import MediaFileStorageError

# Cache the news fetching to reduce API calls
@st.cache_data(ttl=3600)  # Cache for 1 hour
def _get_news(_cache_buster):
    try:
        # Search for both Alzheimer's and dementia in a single query
        keywords = "Alzheimer's OR dementia"
        url = (
            f"https://newsapi.org/v2/everything?"
            f"q={keywords}&apiKey={API_KEY}&language=en&searchIn=title&sortBy=publishedAt"
        )
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        articles = response.json().get("articles", [])
        # Limit to 10 articles to avoid overwhelming the UI
        return articles[:10], datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    except requests.RequestException as e:
        st.error(f"Error fetching news: {str(e)}")
        return [], datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def news_page():
    st.title("Latest News on Alzheimer’s and Dementia")

    # Refresh button to clear cache and fetch new news
    if "cache_buster" not in st.session_state:
        st.session_state.cache_buster = 0

    if st.button("Refresh News"):
        st.session_state.cache_buster += 1
        st.cache_data.clear()  # Clear the cache to force a new API call

    # Fetch news with a spinner
    with st.spinner("Fetching the latest news..."):
        news_articles, last_updated = _get_news(st.session_state.cache_buster)

    # Display last updated timestamp
    st.write(f"**Last Updated:** {last_updated}")

    # Display news in a grid layout (2 columns)
    if not news_articles:
        st.write("No recent news available for Alzheimer's or Dementia.")
    else:
        # Create a grid of 2 columns
        cols = st.columns(2)
        for idx, news in enumerate(news_articles):
            with cols[idx % 2]:  # Alternate between columns
                # Style each news item as a card
                st.markdown(
                    """
                    <div style='background-color: #f9f9f9; padding: 15px; border-radius: 10px; margin-bottom: 15px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);'>
                    """,
                    unsafe_allow_html=True
                )
                st.write(
                    f"""<h3 style='margin-top: 0;'>{html.unescape(news['title'])}</h3>""",
                    unsafe_allow_html=True
                )
                try:
                    if news["urlToImage"]:
                        st.image(news["urlToImage"], use_container_width=True)
                except MediaFileStorageError:
                    st.image(DEFAULT_IMAGE, use_container_width=True)
                st.write(
                    f"""
                    <h5>{news['description'] if news['description'] else 'No description available'}</h5>
                    Link: <a href="{news['url']}">{news['url'][:80]}...</a><br>
                    Author: {news['author'] if news['author'] else 'Unknown'},  
                    <i>{news['publishedAt'][:10]}</i>
                    """,
                    unsafe_allow_html=True
                )
                st.markdown("</div>", unsafe_allow_html=True)