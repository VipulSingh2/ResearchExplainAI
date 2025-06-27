# ResearchExplainAI

![ResearchExplainAI](https://img.shields.io/badge/AI-Powered-blue) ![Status](https://img.shields.io/badge/Status-Active-green) ![Streamlit](https://img.shields.io/badge/Built%20With-Streamlit-orange)

**ResearchExplainAI** is an AI-powered application designed to simplify and personalize the process of understanding complex research papers. By leveraging Google's Gemini-1.5-pro model, this app provides detailed explanations tailored to different expertise levels, styles, and lengths.

## 🌟 Key Features
- **Customizable Explanations**: Choose the style (e.g., beginner-friendly, intermediate, or advanced) and length of the explanation to suit your needs.
- **AI-Driven Analysis**: Uses Google Generative AI for fast and accurate results.
- **User-Friendly Interface**: Built with Streamlit, ensuring an intuitive and interactive user experience.
- **Flexible Input**: Just provide the research paper name, and the app does the heavy lifting for you.

## 🚀 How It Works
1. Enter the research paper name in the input field.
2. Specify the style (e.g., beginner-friendly, advanced) and desired explanation length.
3. Click the **"Explain it!"** button to receive a tailored explanation powered by AI.

The app uses:
- **LangChain Prompts**: For creating structured, reusable prompt templates.
- **Google Generative AI**: To process and generate explanations.
- **Streamlit**: For a responsive web-based interface.

## 🛠️ Installation and Setup

### Prerequisites
- [Python 3.8+](https://www.python.org/downloads/)
- [Streamlit](https://streamlit.io/)
- API key for [Google Generative AI](https://cloud.google.com/ai)

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/VipulSingh2/ResearchExplainAI.git
   cd ResearchExplainAI
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your Google API key to the `.env` file:
   ```plaintext
   GOOGLE_API_KEY=<your_api_key>
   ```

4. Run the app:
   ```bash
   streamlit run main.py
   ```

## 🎯 Use Cases
- **Students**: Quickly grasp complex papers for assignments or projects.
- **Researchers**: Gain concise overviews or in-depth insights tailored to specific needs.
- **Educators**: Simplify research concepts for teaching purposes.

## 🧠 Example Inputs
- **Paper Name**: "Attention is All You Need"
- **Style**: Beginner-friendly
- **Length**: Short summary

## 🤝 Contributing
We welcome contributions to enhance **ResearchExplainAI**! Here's how you can get involved:
1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

## ⚠️ Troubleshooting
- Ensure your Google API key is valid and added to the `.env` file. The app will stop and show an error if the key is missing.


## 🌐 Connect
Have questions or feedback? Feel free to reach out:
- [GitHub Issues](https://github.com/VipulSingh2/ResearchExplainAI/issues)
- Email: vipulsingh2@example.com

---

Thank you for using **ResearchExplainAI**! We hope this tool makes exploring research papers a more enjoyable and productive experience.
