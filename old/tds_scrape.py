data = []
article_id = 0
years = range(2015,2023)
i = 0
n = len(selected_days)
for year in years:
    for d in selected_days:
        i += 1
        month, day = convert_day(d)
        date = '{0}-{1:02d}-{2:02d}'.format(year, month, day)
        print(f'{i} / {n} ; {date}')
        for publication, url in urls.items():
            response = requests.get(url.format(year, month, day), allow_redirects=True)
            if not response.url.startswith(url.format(year, month, day)):
                continue
            page = response.content
            soup = BeautifulSoup(page, 'html.parser')
            articles = soup.find_all(
                "div",
                class_="postArticle postArticle--short js-postArticle js-trackPostPresentation js-trackPostScrolls")
            for article in articles:
                title = article.find("h3", class_="graf--title")
                if title is None:
                    continue
                title = title.contents[0]
                article_id += 1
                subtitle = article.find("h4", class_="graf--subtitle")
                subtitle = subtitle.contents[0] if subtitle is not None else ''
                #image = article.find("img", class_="graf-image")
                #image = '' if image is None else get_img(image['src'], 'images', f'{article_id}')
                article_url = article.find_all("a")[3]['href'].split('?')[0]
                number_sections, number_paragraphs, section_titles, story_text = get_article_text(article_url)
                buttons = article.find_all("button")
                claps = get_claps(buttons[1].contents[0]) if len(buttons) > 0 else None
                reading_time = article.find("span", class_="readingTime")
                reading_time = 0 if reading_time is None else int(reading_time['title'].split(' ')[0])
                responses = article.find_all("a")
                if len(responses) == 7:
                    responses = responses[6].contents[0].split(' ')
                    if len(responses) == 0:
                        responses = 0
                    else:
                        responses = responses[0]
                else:
                    responses = 0

                data.append([article_id, article_url, title, subtitle,
                             number_sections, number_paragraphs, section_titles, story_text,
                             claps, responses,
                             reading_time, publication, date,year])
