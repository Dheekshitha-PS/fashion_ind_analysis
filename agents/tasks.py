from crewai import Task
from agents import agents

from crewai import Task

# Market Research Task
market_task = Task(
    description="Discover top competitors in Indian women's formal wear using browser search and fashion retail websites.",
    expected_output="A ranked list of 5-10 competitors with brand names, brief descriptions, and website URLs, market share of the companies, "
                    "do they serve only women.Do not include ethnic brands like fabIndia, biba etc.Give in JSON format only",
    agent=agents["competitor_discovery"], output_file= "task_outputs/v5/market_task_v5.txt"
)

# Data Extraction Task
intel_task = Task(
    description="Scrape product categories and price ranges in INR from the identified competitor websites.",
    expected_output="Product categories, all kinds of products offered, and price ranges per category per competitor.Give in JSON format only",
    agent=agents["data_extraction"],
    context=[market_task], output_file= "task_outputs/v5/intel_task_v5.txt"
)

# Differentiation Analysis Task
differentiator_task = Task(
    description="Identify unique selling propositions of each competitor using reviews, social media, and PR.",
    expected_output="USPs for each competitor.Give in JSON format only",
    agent=agents["analysis"],
    context=[market_task], output_file= "task_outputs/v5/differentiator_task_v5.txt"
)

marketplace_task = Task(
    description=(
        "For each major Indian and international women's formalwear brand (e.g., Van Heusen, W for Woman, Mango, Zara, H&M, etc.), "
        "find out which online fashion marketplaces (like Amazon, Myntra, Flipkart, AJIO, Nykaa Fashion, TataCliq) they are sold on. "
        "Provide a table with marketplace availability per brand and include direct links to brand or product listings when available. "
        "Ignore brand-owned D2C websites unless the brand is also selling through a marketplace model on those sites."
    ),
    expected_output=(
        "In JSON format only- listing brands vs. availability on marketplaces"
        "Also mention if any brand has exclusive marketplace presence or marketplace-specific offers."
    ),
    agent=agents["marketplace"],
    context=[market_task],
    output_file="task_outputs/v5/market_place_task_v5.txt"
)


# Strategy Summary Task
summary_task = Task(
    description="Combine competitor intelligence and USPs into a whitespace analysis for the Indian market.",
    expected_output="A market gap matrix and brand strategy proposal.Give in JSON format only",
    agent=agents["strategy"],
    context=[intel_task,marketplace_task, differentiator_task], output_file= "task_outputs/v5/summary_task_v5.txt"
)








consumer_sentiment_task = Task(
    description="Scrape reviews from marketplaces and brand websites. Summarize top positive and negative themes (fit, material quality, delivery, price satisfaction, return policies).",
    expected_output="Sentiment breakdown by brand with supporting quotes and a pain-point heatmap.Give in JSON format only",
    agent=agents["consumer_sentiment_agent"],
    context=[market_task], output_file= "task_outputs/v5/sentiment_task_v5.txt"
)

trendwatch_task = Task(
    description="Identify current and emerging trends in women's workwear globally and in India, including fabrics, design elements, sustainability, and work-leisure crossovers.",
    expected_output="A list of key trends with brief explanations and their potential relevance to the Indian market.Give in JSON format only",
    agent=agents["trendwatch_agent"], output_file= "task_outputs/v5/trends_task_v5.txt"
)
pricing_task = Task(
    description="Analyze how Indian formalwear brands price their products across different categories and platforms. Recommend an optimal pricing strategy for a new brand targeting middle to upper-middle-class women.",
    expected_output="A suggested pricing band for each product category, with rationale based on competitor pricing and value positioning.Give in JSON format only",
    agent=agents["pricing_agent"],
    context=[intel_task], output_file= "task_outputs/v5/pricing_task_v5.txt"
)
brand_voice_task = Task(
    description="Review the visual identity and brand language (website copy, logos, packaging) of 5–10 Indian women's formalwear brands."
                "Analyze the language, tone, and visuals on brand websites and Instagram pages. Identify each brand's personality and audience targeting strategy",
    expected_output="Table summarizing tone (empowering, chic, professional), visual aesthetic, and messaging keywords for each brand.Give in JSON format only",
    agent=agents["brand_voice_agent"],
    context=[market_task], output_file= "task_outputs/v5/brand_voice_task_v5.txt"
)

fit_inclusivity_task = Task(
    description="Analyze sizing and fit strategies of Indian formalwear brands. Are plus sizes offered? Are diverse models featured? What are common complaints around sizing, fit, comfort, and mobility?",
    expected_output="Table with brand, size range, model diversity, key customer complaints (fit, comfort, body type exclusion).Give in JSON format only",
    agent=agents["fit_inclusivity_agent"],
    context=[consumer_sentiment_task], output_file= "task_outputs/v5/fit_task_v5.txt"
)


global_brands_task = Task(
    description="Identify top foreign women’s workwear brands (e.g., M.M.LaFleur, Theory, Argent, Uniqlo) and analyze their unique selling propositions (USPs), target customers, and factors behind their success. Highlight what makes them stand out in terms of design, fit, fabric, branding, or distribution.",
    expected_output=(
        "A structured comparison of 5-7 global brands in JSON format only with: \n"
        "- Brand Name\n"
        "- Country of Origin\n"
        "- Core USP(s)\n"
        "- Target Segment\n"
        "- Distribution Channels\n"
        "- Key reasons for success"
    ),
    agent=agents["global_brand"], output_file= "task_outputs/v5/global_brands_task_v5.txt"
)


# Dashboard Generation Task
dashboard_task = Task(
    description=(
        "Using the outputs in JSON format from the differnt analysis tasks, generate a Streamlit dashboard to visualize:"
        "\n\n1. **Top Indian brands** with market share (bar chart or pie chart)."
        "\n2. **Product categories vs. pricing** for each brand (box plot or heatmap)."
        "\n3. **USPs and brand positioning** (textual section with highlights, could use tag clouds)."
        "\n4. **Foreign brand USPs** and how they compare to Indian brands."
        "\n5. **Customer sentiment analysis results** (bar chart or word cloud showing sentiment trends)."
        "\n6. **Trends and style analysis** (timeline or bar chart of trending attributes)."
        "\n7. **Inclusivity score or fit range** comparisons among brands (bar chart)."
        "\n\nEnsure the dashboard has a clean, intuitive layout with clear section titles and legends."
    ),
    expected_output="A complete `dashboard.py` file using Streamlit that reads from the structured data and generates the visualizations mentioned.",
    agent=agents["dashboard"],
    context=[
        intel_task,
        differentiator_task,
        pricing_task,
        consumer_sentiment_task,
        trendwatch_task,
        global_brands_task,
        fit_inclusivity_task,
        brand_voice_task
    ],
    output_file="task_outputs/v5/dashboard_code_v5.py"
)

brand_architecture_task = Task(
    description="Integrate trend, sentiment, pricing, branding, and fit insights to propose a holistic brand positioning and "
                "initial product strategy for a new Indian women's workwear brand.",
    expected_output="A brand blueprint covering positioning, core customer segment, visual language, and product direction.Give in JSON format only",
    agent=agents["strategy"],
    context=[
        summary_task,
        consumer_sentiment_task,
        trendwatch_task,
        pricing_task,
        brand_voice_task,
        fit_inclusivity_task,
        global_brands_task
    ], output_file= "task_outputs/v5/brand_arch_v5.txt"
)
# Manager Review Task
manager_task =Task(
    description = """Review all outputs generated by the agents (including summaries, trend analyses, and the dashboard). 

Ensure the following:
- all the agents are giving responses as per the requirement and expected output format
- The content is accurate, clear, and aligned with the business goal of launching a formalwear brand for Indian women.
- Visualizations in the dashboard are meaningful and properly labeled.
- Insights are coherent, not repetitive, and free of inconsistencies or hallucinations.
- The tone and format are professional, suitable for a business decision document.

Give specific feedback or suggestions for improvement where needed. Do NOT attempt to delegate work to others unless you're absolutely sure of the tool format.""",
    expected_output = "A final quality review document with specific observations, improvement suggestions, and a summary verdict on whether the outputs are ready for stakeholder presentation.Give in JSON format only",
    agent=agents["manager"],
context=[market_task, intel_task, differentiator_task, summary_task, dashboard_task
         ]
, output_file= "task_outputs/v5/manager_task_v5.txt"
)

oppurtunity_task = Task(
description = "Use data from other agents to summarize what’s missing — like lack of affordable blazers for interns, or formalwear with pockets. Identify areas for innovation.",

expected_output= "List of unmet needs, suggested product ideas like jumpsuits, and potential differentiation strategies.Give in JSON format only",
    agent =agents["opportunity"],
    context =[market_task,                      # Indian brand discovery
global_brands_task,              # Foreign brand discovery
intel_task,                      # Extract categories, prices, USPs from Indian brands
differentiator_task,            # Identify Indian brand USPs via reviews/social
pricing_task,

brand_voice_task,
trendwatch_task,
consumer_sentiment_task,
fit_inclusivity_task,
summary_task,                   # Use as context: intel, differentiator, global_brands, pricing, etc.
],
    output_file="task_outputs/v5/opp_task_v5.txt")


# Export all tasks
tasks = [
market_task,                      # Indian brand discovery
global_brands_task,              # Foreign brand discovery
intel_task,                      # Extract categories, prices, USPs from Indian brands
differentiator_task,            # Identify Indian brand USPs via reviews/social
pricing_task,
brand_voice_task,
trendwatch_task,
consumer_sentiment_task,
fit_inclusivity_task,
marketplace_task,

summary_task,                   # Use as context: intel, differentiator, global_brands, pricing, etc.
brand_architecture_task,
dashboard_task,
oppurtunity_task,
manager_task # Context = summary_task


]
