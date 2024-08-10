# News Headlines and Topic Searcher

This Python application allows users to either fetch the latest news headlines or search for news articles by specific topics. The headlines are fetched using the [NewsAPI](https://newsapi.org/) and are displayed in English from sources in India. If the full content of an article is unavailable, the application provides a link to the article so the user can read it online.

## Features

- Fetch the latest news headlines from India.
- Search for news articles by specific topics.
- Display article descriptions and full content when available.
- Provide a URL to the full article if the content is not available.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/news-headlines-topic-searcher.git
    cd news-headlines-topic-searcher
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Obtain a NewsAPI key by signing up at [NewsAPI](https://newsapi.org/register).

5. Create a `.env` file in the project directory and add your API key:

    ```bash
    NEWS_API_KEY=your_newsapi_key_here
    ```

## Usage

1. Run the application:

    ```bash
    python main.py
    ```

2. When prompted, choose whether to search for a specific topic or get the latest headlines:

    - **Topic**: Enter a keyword or phrase to search for related articles.
    - **Headlines**: Get the latest news headlines from India.

3. The application will display the headlines and descriptions. You can choose to read the full article or get a link to the article if the content is not available.

## Example

Do you want to search for a specific topic or get the latest headlines? (topic/headlines): headlines

USA vs. Australia score, live updates: A'ja Wilson and Co. look to advance to Paris Olympics gold medal game - Yahoo Sports
Description: None
Do you want to read full article? (yes/no): yes
Sorry, content is not available for this article.
You can read the full article here: https://sports.yahoo.com/usa-vs-australia-score-live-170001234.html
Do you want to see more headlines? (yes/no): yes

## Requirements

- Python 3.6+
- `newsapi-python` package

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [NewsAPI](https://newsapi.org/) for providing access to news data.
