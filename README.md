# 🌍 World Religion Insights

A premium, interactive Streamlit application designed to explore the complex demographics, growth patterns, and global impact of major world religions.

![App Preview](assets/stunning_cathedral_glassmorphism_1768282680392.png)

## ✨ Features

- **📊 Dynamic Dashboard**: High-level overview of global religious populations and growth trends.
- **💓 The Belief Pulse**: Real-time simulation of estimated follower increases worldwide.
- **🛰️ Global Impact Scorecard**: Detailed analysis of religions across dimensions like Economy, Education, and Philanthropy using interactive radar charts.
- **🏛️ Architecture Gallery**: A curated visual journey through the sacred architectural heritage of different faiths.
- **🔮 Future Projections**: Interactive simulator to project religious demographics up to the year 2100.
- **🌙 Premium Dark Mode**: Deeply immersive UI with glassmorphism effects and sophisticated gradients.

## 🛠️ Tech Stack

- **Framework**: [Streamlit](https://streamlit.io/)
- **Data Visualization**: [Plotly](https://plotly.com/python/), [Pydeck](https://deckgl.github.io/pydeck/)
- **Styling**: Custom CSS with Glassmorphism
- **Language**: Python 3.12+

## 🚀 Getting Started

### Prerequisites

- Python 3.12 or higher
- [uv](https://github.com/astral-sh/uv) (recommended for dependency management)

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd world_religion
   ```

2. **Install dependencies**:
   Using `uv`:
   ```bash
   uv sync
   ```
   Using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

### Running the App

Execute the following command in your terminal:

```bash
uv run streamlit run main.py
```
or
```bash
streamlit run main.py
```

## 🌐 Deployment

This application is optimized for deployment on **Streamlit Cloud**.

1. Push your code to a GitHub repository.
2. Sign in to [share.streamlit.io](https://share.streamlit.io).
3. Connect your repository and select `main.py` as the entry point.

The repository includes a `.streamlit/config.toml` file to ensure the dark theme is enforced upon deployment.

## 📁 Project Structure

```text
world_religion/
├── .streamlit/          # Streamlit configuration
├── assets/              # Image assets for the gallery
├── main.py              # Main application logic
├── style.css            # Custom glassmorphism styles
├── requirements.txt     # Dependency list
└── README.md            # You are here!
```

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).
