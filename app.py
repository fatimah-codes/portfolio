import base64
import json
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

# Base directory for the portfolio project
BASE_DIR = Path(__file__).resolve().parent

# Configure Streamlit page
st.set_page_config(
    page_title="Fatima Hamayyun — Portfolio",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom CSS to eliminate Streamlit chrome, paddings, and outer scrollbars
st.markdown(
    """
    <style>
    /* Completely hide Streamlit header, footer, menu and decoration */
    #MainMenu {visibility: hidden; display: none !important;}
    header {visibility: hidden; display: none !important;}
    footer {visibility: hidden; display: none !important;}
    .stDeployButton {display: none !important;}
    [data-testid="stToolbar"] {display: none !important;}
    [data-testid="stDecoration"] {display: none !important;}
    [data-testid="stStatusWidget"] {display: none !important;}
    [data-testid="stHeader"] {display: none !important;}
    .stApp > header {display: none !important;}

    /* Strip all outer margins, padding, and scrollbars */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"], section.main {
        margin: 0 !important;
        padding: 0 !important;
        overflow: hidden !important;
        background-color: #000000 !important;
        height: 100vh !important;
        width: 100vw !important;
    }

    div.block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
        width: 100vw !important;
        height: 100vh !important;
        overflow: hidden !important;
    }

    /* Force the components iframe to occupy exact full viewport */
    iframe {
        border: none !important;
        width: 100vw !important;
        height: 100vh !important;
        display: block !important;
        margin: 0 !important;
        padding: 0 !important;
        overflow: hidden !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def load_portfolio_data():
    """Load extracted CV content from portfolio.json."""
    json_path = BASE_DIR / "data" / "portfolio.json"
    if not json_path.exists():
        raise FileNotFoundError(f"Portfolio data not found at: {json_path}")
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_cv_base64():
    """Load the CV PDF and encode as base64 for one-click download."""
    cv_path = BASE_DIR / "assets" / "Fatima_Hamayyun_CV.pdf"
    if cv_path.exists():
        with open(cv_path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    return ""


def render_portfolio():
    """Inject content into the AXON-style HTML template and render."""
    data = load_portfolio_data()
    cv_base64 = load_cv_base64()

    template_path = BASE_DIR / "templates" / "index.html"
    with open(template_path, "r", encoding="utf-8") as f:
        html_template = f.read()

    # Inject data into template placeholders
    html_rendered = html_template.replace("{{ PORTFOLIO_JSON }}", json.dumps(data))
    html_rendered = html_rendered.replace("{{ CV_BASE64 }}", cv_base64)

    # Render inside single full-screen iframe
    components.html(html_rendered, height=1000, scrolling=False)


if __name__ == "__main__":
    render_portfolio()
