from crewai import Agent
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, CodeInterpreterTool

# Tools
web_search_tool = SerperDevTool()
scraper_tool = ScrapeWebsiteTool()
coding_tool = CodeInterpreterTool()

# 1. Competitor Discovery Agent
competitor_discovery_agent = Agent(
    role="Competitor Discovery Analyst",
    goal="Identify both top and small brands in women's formal wear in India.",
    backstory="An expert researcher familiar with the Indian fashion landscape.",
    tools=[web_search_tool],
    verbose=True
)


# 2. Data Extraction Agent
data_extraction_agent = Agent(
    role="Data Extraction Agent",
    goal="Scrape brand websites and extract 1. Different product categories offred like knee-lenght dresses, suits, pants etc"
         "Give a price range for each category above"
        "What are the USPs of each brand"

    ,

    backstory="An analyst who is good at finding and structuring unstructured product data.",
    tools=[scraper_tool],
    verbose=True
)


# 1. Competitor Discovery Agent
competitor_discovery_agent = Agent(
    role="Competitor Discovery Analyst",
    goal="Identify both top and small brands in women's formal wear in India. Keep the ethnic brands separate from modern ones. Include the market share of each the brand",
    backstory="An expert researcher familiar with the Indian fashion landscape.",
    tools=[web_search_tool],
    verbose=True
)


# 2. Data Extraction Agent
data_extraction_agent = Agent(
    role="Data Extraction Agent",
    goal="Scrape brand websites and extract 1. Different product categories offred like knee-lenght dresses, suits, pants etc"
         "Give a price range for each category above"
        "What are the USPs of each brand"

    ,

    backstory="An analyst who is good at finding and structuring unstructured product data.",
    tools=[scraper_tool],
    verbose=True
)

# 3. Analysis Agent
analysis_agent = Agent(
    role="Business Analyst",
    goal="Analyze product range, pricing, and positioning from competitor data",
    backstory="A market intelligence expert who draws insights from structured data",
    tools=[],
    verbose=True
)

# 4. Dashboard Generation Agent (Coding Agent)
dashboard_agent = Agent(
    role="Streamlit Dashboard Developer",
    goal="Generate a Streamlit dashboard visualizing competitor analysis",
    backstory="A Streamlit expert who creates data-driven dashboards for fashion analytics.",
    tools=[coding_tool],
    verbose=True
)

# 5. Manager Agent
manager_agent = Agent(
    role="Project Oversight Manager",
    goal="Ensure agents are producing correct and complete outputs and output format for the brand's business plan",
    backstory="A veteran strategy consultant who ensures high quality, and consistency across agents.",
    tools=[],
    verbose=True, allow_delegation=True
)
strategy_agent = Agent(
    role="Strategic Analyst",
    goal="Combine competitor intelligence and USPs into a whitespace analysis for the Indian market",
    backstory="We want to build a work wear brand for women in India."
              "You are A business strategy expert who develops actionable insights from competitor data to help build the brand's positioning.",
    tools=[],
    verbose=True
)

global_brand_agent = Agent(
    role="Global Brand Analyst",
    goal="Identify top foreign women’s workwear brands and explain their USPs and success factors.",
    backstory="An international fashion business expert analyzing brand strategies globally.",
    tools=[web_search_tool],
    verbose=True
)

marketplace_agent = Agent(
    role="Marketplace Availability Analyst",
    goal="Identify which online marketplaces (e.g., Amazon, Myntra, Flipkart, AJIO, Nykaa Fashion, TataCliq) sell Indian and international women's formalwear brands.",
    backstory=(
        "You're an expert in the Indian e-commerce ecosystem. Your job is to discover "
        "where each formalwear brand is sold online, focusing on third-party marketplaces rather than brand websites. "
        "Your output helps businesses understand multi-channel distribution and where customers are shopping."
    ),
    tools=[web_search_tool],
    verbose=True
)




# 3. Analysis Agent
analysis_agent = Agent(
    role="Business Analyst",
    goal="Analyze product range, pricing, and positioning from competitor data",
    backstory="A market intelligence expert who draws insights from structured data",
    tools=[],
    verbose=True
)

# 4. Dashboard Generation Agent (Coding Agent)
dashboard_agent = Agent(
    role="Streamlit Dashboard Developer",
    goal="Generate a Streamlit dashboard visualizing competitor analysis",
    backstory="A Streamlit expert who creates data-driven dashboards for fashion analytics.",
    tools=[coding_tool],
    verbose=True
)

# 5. Manager Agent
manager_agent = Agent(
    role="Project Oversight Manager",
    goal="Ensure agents are producing correct and complete outputs for the brand's business plan",
    backstory="A veteran strategy consultant who ensures high quality, and consistency across agents.",
    tools=[],
    verbose=True, allow_delegation=True
)
strategy_agent = Agent(
    role="Strategic Analyst",
    goal="Combine competitor intelligence and USPs into a whitespace analysis for the Indian market",
    backstory="We want to build a work wear brand for women in India."
              "You are A business strategy expert who develops actionable insights from competitor data to help build the brand's positioning.",
    tools=[],
    verbose=True
)

global_brand_agent = Agent(
    role="Global Brand Analyst",
    goal="Identify top foreign women’s workwear brands and explain their USPs and success factors.",
    backstory="An international fashion business expert analyzing brand strategies globally.",
    tools=[web_search_tool],
    verbose=True
)

marketplace_agent = Agent(
    role="Marketplace Availability Analyst",
    goal="Find out where Indian women’s formalwear brands are selling their products",
    backstory="An expert in e-commerce ecosystems, skilled in tracing brand distribution across platforms.",
    tools=[web_search_tool],
    verbose=True
)
trendwatch_agent = Agent(
    role="Fashion Trend Analyst",
    goal="Identify emerging trends in women's workwear globally and in India, including materials, silhouettes, consumer behavior, and shopping preferences.",
    backstory="A fashion futurist tracking runway shows, fashion weeks, trend reports, and Gen Z behavior.",
    tools=[web_search_tool],
    verbose=True
)
brand_voice_agent = Agent(
    role="Brand Language and Visual Identity Analyst",
    goal="Analyze the visual and verbal branding of top competitors—logos, websites, packaging, and tone of voice. Recommend distinct angles.",
    backstory="A creative strategist trained in branding, semiotics, and D2C storytelling.",
    tools=[web_search_tool],
    verbose=True
)
fit_inclusivity_agent = Agent(
    role="Fit & Body Inclusivity Analyst",
    goal="""Search online to evaluate how current Indian women's formalwear brands address:
    - sizing and fit
    - inclusivity for body types
    - common complaints about comfort or mobility

    Use this to suggest best practices for inclusive formalwear design.""",

backstory="A human-centered fashion expert focused on comfort and fit for all body types.",
    tools=[web_search_tool, scraper_tool],
    verbose=True
)
pricing_agent = Agent(
    role="Pricing Strategist",
    goal="Recommend a price positioning strategy based on competitor pricing, customer expectations, and perceived value.",
    backstory="An expert in retail pricing psychology and value-based pricing models.",
    tools=[],
    verbose=True
)
consumer_sentiment_agent = Agent(
    role="Consumer Sentiment Analyst",
    goal="Analyze online reviews and social media content to understand customer pain points, desires, and satisfaction with existing formalwear brands.",
    backstory="A sentiment analysis expert who uncovers real consumer needs and frustrations from reviews and feedback.",
    tools=[web_search_tool, scraper_tool],
    verbose=True
)


# Define all agents in the dictionary
agents = {
    "competitor_discovery": competitor_discovery_agent,
    "data_extraction": data_extraction_agent,
    "marketplace":marketplace_agent,
    "global_brand":global_brand_agent,
    "analysis": analysis_agent,
    "strategy": strategy_agent,  # Added strategy agent
    "dashboard": dashboard_agent,
    "consumer_sentiment_agent":consumer_sentiment_agent,
    "trendwatch_agent":trendwatch_agent,
    "pricing_agent":pricing_agent,
    "manager": manager_agent,
"brand_voice_agent":brand_voice_agent,
"fit_inclusivity_agent":fit_inclusivity_agent
}
