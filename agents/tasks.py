from crewai import Task
from agents import agents

from crewai import Task

# Market Research Task
market_task = Task(
    description="Discover top competitors in Indian women's formal wear using browser search and fashion retail websites.",
    expected_output="A ranked list of 5-10 competitors with brand names, brief descriptions, and website URLs, market share of the companies, do they serve only women.Do not include ethnic brands like fabIndia, biba etc.",
    agent=agents["competitor_discovery"], output_file= "task_outputs/market_task_v4.txt"
)

# Data Extraction Task
intel_task = Task(
    description="Scrape product categories and price ranges in INR from the identified competitor websites.",
    expected_output="Product categories, all kinds of products offered, and price ranges per category per competitor.",
    agent=agents["data_extraction"],
    context=[market_task], output_file= "task_outputs/intel_task_v4.txt"
)

# Differentiation Analysis Task
differentiator_task = Task(
    description="Identify unique selling propositions of each competitor using reviews, social media, and PR.",
    expected_output="USPs for each competitor.",
    agent=agents["analysis"],
    context=[market_task], output_file= "task_outputs/differentiator_task_v4.txt"
)

marketplace_task = Task(
    description=(
        "For each major Indian and international women's formalwear brand (e.g., Van Heusen, W for Woman, Mango, Zara, H&M, etc.), "
        "find out which online fashion marketplaces (like Amazon, Myntra, Flipkart, AJIO, Nykaa Fashion, TataCliq) they are sold on. "
        "Provide a table with marketplace availability per brand and include direct links to brand or product listings when available. "
        "Ignore brand-owned D2C websites unless the brand is also selling through a marketplace model on those sites."
    ),
    expected_output=(
        "A markdown table listing brands vs. availability on marketplaces, e.g.:\n\n"
        "| Brand         | Amazon | Myntra | Flipkart | Nykaa Fashion | AJIO | TataCliq |\n"
        "|---------------|--------|--------|----------|----------------|------|----------|\n"
        "| Van Heusen    | ✅ [Link](...) | ✅ [Link](...) | ✅ [Link](...) | ❌ | ✅ [Link](...) | ✅ [Link](...) |\n"
        "| W for Woman   | ✅ [Link](...) | ✅ [Link](...) | ✅ [Link](...) | ✅ [Link](...) | ❌ | ❌ |\n"
        "Also mention if any brand has exclusive marketplace presence or marketplace-specific offers."
    ),
    agent=agents["marketplace"],
    context=[market_task],
    output_file="task_outputs/market_place_task_v4.txt"
)


# Strategy Summary Task
summary_task = Task(
    description="Combine competitor intelligence and USPs into a whitespace analysis for the Indian market.",
    expected_output="A market gap matrix and brand strategy proposal.",
    agent=agents["strategy"],
    context=[intel_task, differentiator_task], output_file= "task_outputs/summary_task_v4.txt"
)








consumer_sentiment_task = Task(
    description="Analyze online reviews and customer feedback for Indian women's formalwear brands. Identify common pain points, praised features, and emotional triggers (comfort, confidence, professionalism, etc.).",
    expected_output="A brand-wise summary of top complaints, appreciated features, and emotional sentiment themes- positive and negative sentiments",
    agent=agents["consumer_sentiment_agent"],
    context=[market_task], output_file= "task_outputs/sentiment_task_v4.txt"
)

trendwatch_task = Task(
    description="Identify current and emerging trends in women's workwear globally and in India, including fabrics, design elements, sustainability, and work-leisure crossovers.",
    expected_output="A list of key trends with brief explanations and their potential relevance to the Indian market.",
    agent=agents["trendwatch_agent"], output_file= "task_outputs/trends_task_v4.txt"
)
pricing_task = Task(
    description="Analyze how Indian formalwear brands price their products across different categories and platforms. Recommend an optimal pricing strategy for a new brand targeting middle to upper-middle-class women.",
    expected_output="A suggested pricing band for each product category, with rationale based on competitor pricing and value positioning.",
    agent=agents["pricing_agent"],
    context=[intel_task], output_file= "task_outputs/pricing_task_v4.txt"
)
brand_voice_task = Task(
    description="Review the visual identity and brand language (website copy, logos, packaging) of 5–10 Indian women's formalwear brands. Suggest a differentiated look and tone of voice for a modern, confident brand.",
    expected_output="Analysis of competitor brand voices and visuals, followed by recommendations for distinct brand expression.",
    agent=agents["brand_voice_agent"],
    context=[market_task], output_file= "task_outputs/brand_voice_task_v4.txt"
)

fit_inclusivity_task = Task(
    description="Evaluate how current Indian formalwear brands address sizing and fit. Identify common customer complaints around fit, inclusivity (sizes, body types, comfort), and mobility. Suggest best practices.",
    expected_output="Insights into current gaps in fit and inclusivity, and recommendations for product development.",
    agent=agents["fit_inclusivity_agent"],
    context=[consumer_sentiment_task], output_file= "task_outputs/fit_task_v4.txt"
)


global_brands_task = Task(
    description="Identify top foreign women’s workwear brands (e.g., M.M.LaFleur, Theory, Argent, Uniqlo) and analyze their unique selling propositions (USPs), target customers, and factors behind their success. Highlight what makes them stand out in terms of design, fit, fabric, branding, or distribution.",
    expected_output=(
        "A structured comparison of 5-7 global brands with: \n"
        "- Brand Name\n"
        "- Country of Origin\n"
        "- Core USP(s)\n"
        "- Target Segment\n"
        "- Distribution Channels\n"
        "- Key reasons for success"
    ),
    agent=agents["global_brand"], output_file= "task_outputs/global_brands_task_v4.txt"
)


# Dashboard Generation Task
dashboard_task = Task(
    description=(
        "Using the outputs from the summary and analysis tasks, generate a Streamlit dashboard to visualize:"
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
        summary_task,
        intel_task,
        differentiator_task,
        pricing_task,
        consumer_sentiment_task,
        trendwatch_task,
        global_brands_task,
        fit_inclusivity_task,
        brand_voice_task
    ],
    output_file="task_outputs/dashboard_code_v4.py"
)

brand_architecture_task = Task(
    description="Integrate trend, sentiment, pricing, branding, and fit insights to propose a holistic brand positioning and initial product strategy for a new Indian women's workwear brand.",
    expected_output="A brand blueprint covering positioning, core customer segment, visual language, and product direction.",
    agent=agents["strategy"],
    context=[
        summary_task,
        consumer_sentiment_task,
        trendwatch_task,
        pricing_task,
        brand_voice_task,
        fit_inclusivity_task,
        global_brands_task
    ], output_file= "task_outputs/brand_arch_v4.txt"
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
    expected_output = "A final quality review document with specific observations, improvement suggestions, and a summary verdict on whether the outputs are ready for stakeholder presentation.",
    agent=agents["manager"],
context=[market_task, intel_task, differentiator_task, summary_task, dashboard_task]
, output_file= "task_outputs/manager_task_v4.txt"
)


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
summary_task,                   # Use as context: intel, differentiator, global_brands, pricing, etc.
                   # Context = All previous tasks (or at least summary, dashboard, intel, differentiator)
dashboard_task,
    manager_task # Context = summary_task


]
