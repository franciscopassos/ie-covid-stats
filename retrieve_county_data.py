import bs4
import requests
import sys

DOMAIN = 'https://www.hpsc.ie'
INDEX_PAGE = 'https://www.hpsc.ie/a-z/respiratory/coronavirus/novelcoronavirus/casesinireland/epidemiologyofcovid-19inireland/'


def get_month_pages():
    results = []
    resp = requests.get(INDEX_PAGE)
    if not resp.ok:
        print(f'Could not get index page. ({resp.status_code}: {resp.text})', sys.stderr)
        sys.exit(1)
    soup = bs4.BeautifulSoup(resp.text, 'html.parser')
    headers = soup("header")
    for header in headers:
        if 'Epidemiology of COVID-19 in Ireland' in header.text:
            for li in header.find_next_sibling("ul").find_all("li"):
                results.append(f"{DOMAIN}{li.a['href']}")
    return results
    

def main():
    page_urls = get_month_pages()
    print(page_urls)
    # date_urls = get_date_urls(page_urls)
    # fetch_page_urls()


if __name__ == "__main__":
    main()
