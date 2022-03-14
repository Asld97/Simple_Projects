import pprint
import requests
from bs4 import BeautifulSoup


def site_info(num_sites):
    # Make request and get site info
    if num_sites == 0:
        num_sites = 1
    hn = []
    for site in range(1, num_sites + 1):
        res = requests.get(f'https://news.ycombinator.com/news?p={site}')
        soup = BeautifulSoup(res.text, 'html.parser')  # It is html to parse with BS
        links = soup.select('.athing')
        subtext = soup.select('.subtext')
        hn.extend(create_custom_hn(links, subtext))
    return sort_stories_by_votes(hn)


def sort_stories_by_votes(hn_list):
    return sorted(hn_list, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].select('.titlelink')[0].getText()
        href = links[idx].select('.titlelink')[0].get('href', None)
        vote = subtext[idx].select('.score')
        post_num = links[idx].select('.rank')[0].getText()
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points, 'post number': post_num})

    return hn


pprint.pprint(site_info(0))
