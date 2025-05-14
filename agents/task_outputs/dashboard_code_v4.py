```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data for visualization
brands = ['Van Heusen', 'Allen Solly', 'W for Woman', 'Bossini', 'Vero Moda', 'Chemistry', 'FableStreet', 'Forever 21', 'Mango', 'Promod']
market_share = [15, 12, 10, 9, 8, 7, 6, 5, 3, 2]
price_ranges = {'Van Heusen': [799, 4999], 'Allen Solly': [799, 5999], 'W for Woman': [820, 4999], 'Bossini': [399, 3499], 'Vero Moda': [599, 4999], 'Chemistry': [699, 3999], 'FableStreet': [1200, 8000], 'Forever 21': [599, 4500], 'Mango': [1490, 5999], 'Promod': [1200, 3600]}

# Market Share Visualization
st.title('Competitor Analysis Dashboard')

st.header('Top Indian Brands Market Share')
market_share_df = pd.DataFrame({'Brand': brands, 'Market Share (%)': market_share})
fig, ax = plt.subplots()
sns.barplot(x='Brand', y='Market Share (%)', data=market_share_df, ax=ax)
plt.xticks(rotation=45)

st.pyplot(fig)

# Product Categories vs Pricing Visualization
st.header('Product Categories vs Pricing')
for brand in brands:
    st.write(f'**{brand} Price Range:** INR {price_ranges[brand][0]} - INR {price_ranges[brand][1]}')

# Dummy USPs for each brand
usp_text = {
    'Van Heusen': 'Superior quality and innovation in fabric technology.',
    'Allen Solly': 'Versatile, trendy, and well-known for Friday Dressing.',
    'W for Woman': 'Ethnic with a modern twist, relatable to Indian culture.',
    'Bossini': 'Casual, colorful, and a youthful appeal.',
    'Vero Moda': 'Fast-fashion with trendy garments.',
    'Chemistry': 'Unique contemporary designs for modern wear.',
    'FableStreet': 'Customized workwear that is stylish and comfortable.',
    'Forever 21': 'Fast fashion aimed at younger demographics.',
    'Mango': 'Mediterranean elegance and contemporary style.',
    'Promod': 'Femininity and contemporary styles with an edge.'
}

st.header('Unique Selling Propositions')
for brand, usp in usp_text.items():
    st.write(f'**{brand}:** {usp}')

# Example Customer Sentiment Analysis Visualization
sentiment_data = {'Positive': [30, 45, 20], 'Negative': [10, 5, 15]}
fig, ax = plt.subplots()
sns.barplot(x=list(sentiment_data.keys()), y=[sum(v) for v in sentiment_data.values()], ax=ax)
plt.title('Customer Sentiment Analysis')
st.pyplot(fig)

# Trends Visualizations
trends = {'Sustainable Fashion': 40, 'Versatility': 35, 'Work-Leisure Crossover': 25}
fig, ax = plt.subplots()
sns.barplot(x=list(trends.keys()), y=list(trends.values()), ax=ax)
plt.title('Trends in Women\'s Workwear')
st.pyplot(fig)

# Output the final dashboard
```