
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sample Data - Replace this with your actual data
brands = ['Van Heusen', 'Allen Solly', 'W for Woman', 'The Label Life']
market_share = [12, 10, 7, 2]
product_categories = ['Tops, Bottoms, Dresses, Suits', 'Shirts, T-Shirts, Blazers, Pants, Dresses', 'Kurta Sets, Kurtas, Tops, Dresses, Bottoms', 'Tops, Dresses, Skirts, Co-ords, Accessories']
usps = ['Premium quality fabrics', 'Trendy and vibrant dressing', 'Contemporary ethnic wear', 'Curated collections by celebrity style editors']

# Create DataFrame
competitor_data = pd.DataFrame({'Brand': brands, 'Market Share (%)': market_share, 'Product Categories': product_categories, 'USP': usps})

st.title('Competitor Analysis - Fashion Brands in India')

# Visualize Market Share
st.header('Top Indian Brands with Market Share')
fig, ax = plt.subplots()
ax.bar(competitor_data['Brand'], competitor_data['Market Share (%)'], color='blue')
ax.set_xlabel('Brands')
ax.set_ylabel('Market Share (%)')
ax.set_title('Market Share of Top Indian Fashion Brands')
st.pyplot(fig)

# Visualize Product Categories vs Pricing (Fake Data)
st.header('Product Categories vs. Pricing')
price_ranges = pd.DataFrame({'Brand': brands, 'Price Low': [1200, 1000, 800, 1424], 'Price High': [5000, 4000, 4500, 2890]})
st.line_chart(price_ranges.set_index('Brand'))

# Unique Selling Propositions
st.header('USPs and Brand Positioning')
for index, row in competitor_data.iterrows():
    st.markdown(f"**{row['Brand']}** - {row['USP']}")

# Customer Sentiment Analysis Results (Similar Dummy Data)
st.header('Customer Sentiment Analysis Results')
sentiment_data = {'Sentiment': ['Positive', 'Negative'], 'Counts': [70, 30]}  
sentiments = pd.DataFrame(sentiment_data)
fig, ax = plt.subplots()
ax.bar(sentiments['Sentiment'], sentiments['Counts'], color=['green', 'red'])
ax.set_ylabel('Counts')
ax.set_title('Customer Sentiment Ratings')
st.pyplot(fig)

# Trends and Style Analysis
st.header('Trends and Style Analysis')
trends = ['Sustainability', 'Comfort', 'Style Fusion']
trend_popularity = [60, 75, 50]
fig, ax = plt.subplots()
ax.bar(trends, trend_popularity, color='purple')
ax.set_ylabel('Popularity %')
ax.set_title('Trending Attributes')
st.pyplot(fig)

# Inclusivity Score Comparison
st.header('Inclusivity Score Comparisons')
inclusivity_scores = [80, 75, 90, 65]
fig, ax = plt.subplots()
ax.bar(brands, inclusivity_scores, color='orange')
ax.set_ylabel('Inclusivity Score')
ax.set_title('Inclusivity Scores of Brands')
st.pyplot(fig)
