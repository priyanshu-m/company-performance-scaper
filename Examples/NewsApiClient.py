from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='0bfec681c60e46bb93851e3788c3c58f')

# /v2/top-headlines
#top_headlines = newsapi.get_top_headlines(q='google')

#print(top_headlines)

# /v2/everything
all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)

print(all_articles)
# /v2/sources
#sources = newsapi.get_sources()

