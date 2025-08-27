# VulnGPT 🛡️

**VulnGPT** is an AI-powered vulnerability analysis tool that combines the intelligence of GPT-4 with comprehensive cybersecurity databases to provide actionable insights about CVE vulnerabilities. By leveraging Retrieval-Augmented Generation (RAG), VulnGPT delivers context-aware vulnerability analysis, remediation guidance, and risk assessment.

## 🚀 Features

- **Intelligent Vulnerability Analysis**: Get comprehensive insights about any CVE with natural language queries
- **Multi-Source Data Integration**: Combines NVD API, Nessus scan results, and curated vulnerability databases
- **Interactive Web Interface**: User-friendly Streamlit application for real-time vulnerability analysis
- **Automated Risk Assessment**: Answers critical questions:
  - 🎯 **Am I affected?** - Identifies vulnerable systems and versions
  - ⚠️ **What could go wrong?** - CVSS scores, exploit availability, and impact analysis
  - 🔧 **What can I do about it?** - Patch availability and mitigation strategies
  - 🚨 **What are the risks of patching?** - Side effects and compatibility concerns
- **Nessus Integration**: Detailed analysis of vulnerability scan results
- **Vector Search**: Semantic search across vulnerability databases for relevant context

## 🏗️ Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Streamlit UI  │───▶│   VulnGPT Core   │───▶│   OpenAI GPT-4  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │   Data Sources   │
                    │                  │
                    │ • NVD API        │
                    │ • AstraDB        │
                    │ • Nessus Scans   │
                    │ • Web Scraping   │
                    └──────────────────┘
```

## 🛠️ Technology Stack

- **AI/ML**: OpenAI GPT-4, LangChain, Vector Embeddings
- **Database**: AstraDB (Vector Database)
- **Web Framework**: Streamlit
- **Data Processing**: pandas, BeautifulSoup, html2text
- **APIs**: NVD (National Vulnerability Database)
- **Containerization**: Docker, DevContainers

## 📋 Prerequisites

- Python 3.11+
- OpenAI API Key
- AstraDB Account and API Token
- NVD API Key (optional, for enhanced data)

## 🚀 Quick Start

### Option 1: Using DevContainers (Recommended)

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/vulngpt.git
   cd vulngpt
   ```

2. **Open in VS Code with DevContainers**
   - Install the "Dev Containers" extension
   - Open the project in VS Code
   - Click "Reopen in Container" when prompted

3. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

4. **The application will start automatically on port 8501**

### Option 2: Local Installation

1. **Clone and install dependencies**
   ```bash
   git clone https://github.com/yourusername/vulngpt.git
   cd vulngpt
   pip install -r requirements.txt
   ```

2. **Set up environment variables**
   ```bash
   # Create .env file with the following variables:
   OPENAI_API_KEY=your_openai_api_key
   ASTRA_DB_TOKEN=your_astra_token
   ASTRA_DB_ENDPOINT=your_astra_endpoint
   ASTRA_DB_COLLECTION=your_collection_name
   ASTRA_DB_NAMESPACE=your_namespace
   NVD_API_KEY=your_nvd_api_key
   ```

3. **Run the application**
   ```bash
   streamlit run vul_app.py
   ```

## 💻 Usage

### Web Interface

1. Navigate to `http://localhost:8501`
2. Enter a vulnerability query with a CVE identifier:
   ```
   Tell me about CVE-2021-34527
   ```
3. Get comprehensive analysis including:
   - Vulnerability description and impact
   - Affected systems and versions
   - CVSS scores and severity ratings
   - Available patches and mitigations
   - Nessus scan correlations

### Example Queries

- `What is CVE-2023-23397 and how can I protect my Exchange servers?`
- `Is CVE-2022-30190 being actively exploited?`
- `Show me mitigation steps for CVE-2021-44228 (Log4j)`
- `What are the Nessus findings for CVE-2023-21554?`

## 📁 Project Structure

```
vulngpt/
├── .devcontainer/          # DevContainer configuration
├── astra_database.py       # AstraDB integration
├── client.py              # OpenAI API client
├── html_scraper.py        # Web scraping utilities
├── main.py                # Core application logic
├── nvd_api.py             # NVD API integration
├── processor.py           # Text processing and chunking
├── vul_app.py             # Streamlit web interface
├── requirements.txt       # Python dependencies
└── README.md             # Project documentation
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | OpenAI API key for GPT-4 access | ✅ |
| `ASTRA_DB_TOKEN` | AstraDB authentication token | ✅ |
| `ASTRA_DB_ENDPOINT` | AstraDB endpoint URL | ✅ |
| `ASTRA_DB_COLLECTION` | Main vulnerability collection name | ✅ |
| `ASTRA_DB_NAMESPACE` | AstraDB keyspace/namespace | ✅ |
| `NVD_API_KEY` | National Vulnerability Database API key | ⚪ |

### Database Setup

1. Create an AstraDB account at [astra.datastax.com](https://astra.datastax.com)
2. Create a new vector database
3. Note your endpoint, token, and namespace
4. Collections will be created automatically

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [National Vulnerability Database (NVD)](https://nvd.nist.gov/) for vulnerability data
- [OpenAI](https://openai.com/) for GPT-4 API
- [DataStax Astra](https://astra.datastax.com/) for vector database services
- [LangChain](https://langchain.com/) for RAG framework
- [Streamlit](https://streamlit.io/) for the web interface

## 📞 Support

If you encounter any issues or have questions, please:
1. Check the [Issues](https://github.com/yourusername/vulngpt/issues) page
2. Create a new issue with detailed information about your problem
3. Contact: [your-email@example.com]

---

**⚠️ Disclaimer**: VulnGPT is designed to assist with vulnerability analysis but should not be the sole source for security decisions. Always verify findings with official sources and consult security professionals for critical systems.

