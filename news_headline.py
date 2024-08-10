# Python program that gives the user an option to either search for a specific topic or fetch the latest headlines
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key = 'Your Api Key')

# # to get top headline
def get_top_headlines(page=1):
    top_headlines = newsapi.get_top_headlines(language='en', page=page, page_size=5)
    return top_headlines.get('articles', [])

# # to get news by topic
def get_news_by_topic(topic, page=1):
    news = newsapi.get_everything(q=topic, language='en', sort_by='relevancy', page=page, page_size=5)
    return news.get('articles', [])

# function to display headlines and discription
def disp_article(articles):
    for index, article in enumerate(articles):
        print(f"{index + 1}. {article['title']}")
        print(f"Description: {article.get('description', 'No description available.')}")
        read_more = input("Do you want to read the full article? (yes/no): ").strip().lower()
        if read_more == 'yes':
            if article.get('content'):
                print(f"Content: {article['content']}\n")
            else:
                print("Sorry, content is not available for this article.\n")
                print(f"You can read the full article here: {article.get('url', 'No URL available')}\n")
        print("-" * 80)


def main():
    choice = input("Do you want to search for a specific topic or get the latest headlines? (topic/headlines): ").strip().lower()

    if choice == 'headlines':
        page = 1
        while True:
            articles = get_top_headlines(page=page)
            if not articles:
                print("No more articles available.")
                break
            disp_article(articles)
            more = input("Do you want to see more headlines? (yes/no): ").strip().lower()
            if more != 'yes':
                break
            page += 1
    
    elif choice == "topic":
        topic = input("Enter the topic you want to search for: ").strip()
        page = 1
        while True:
            articles = get_news_by_topic(topic=topic, page=page)
            if not articles:
                print("No more articles available or no articles found for this topic.")
                break
            disp_article(articles)
            more = input("Do you want to see more articles? (yes/no): ").strip().lower()
            if more != 'yes':
                break
            page += 1
    
    else:
        print("Invalid choice. Please choose either 'topic' or 'headlines'.")

if __name__ == "__main__":
    main()