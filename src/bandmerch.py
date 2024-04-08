import requests
import webbrowser
import time
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from tempfile import NamedTemporaryFile
from webdriver_manager.chrome import ChromeDriverManager


def load_page(label):
    if not label:
        raise Exception("Please input an artist/label's name.")

    url = f"https://{label}.bandcamp.com/merch"
    if requests.get(url, allow_redirects=False).status_code != 200:
        raise Exception(
            f"Failed to find merch page for artist/label '{label}'. Is the name correct? Does the label have a merch page?"
        )

    options = Options()
    options.add_argument("--headless=new")
    driver = Chrome(options=options, service=Service(ChromeDriverManager().install()))
    driver.get(url)

    # scroll page slowly so all of the images get loaded
    total_height = int(driver.execute_script("return document.body.scrollHeight"))
    for i in range(1, total_height, 100):
        driver.execute_script("window.scrollTo(0, {});".format(i))
    time.sleep(0.1)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    return soup


def scrape_merch(label, soup):
    merch_list = []
    lis = soup.find(attrs={"id": "merch-grid"}).find_all("li")
    for li in lis:
        # fix hrefs so that they lead to the correct merch page
        a = li.find("a")
        href = a.attrs["href"]
        a.attrs["href"] = f"https://{label}.bandcamp.com{href}"

        merch = {"li": li}
        merch["title"] = li.find(attrs={"class": "title"}).contents[0]
        artist_tag = li.find(attrs={"class": "artist-override"})
        if artist_tag is not None:
            merch["artist"] = artist_tag.text
        tp_tag = li.find(attrs={"merchtype secondaryText"})
        if tp_tag is not None:
            merch["type"] = tp_tag.text.strip()
        price_tag = li.find("span", attrs={"class": "price"})
        if price_tag is not None:
            merch["price"] = float(price_tag.text[1:])
        merch_list.append(merch)
    return merch_list


def apply_filters(merch_list, options):
    if not options["include_sold_out"]:
        merch_list = [merch for merch in merch_list if "price" in merch]
    if options["merch_types"]:
        merch_list = [
            merch for merch in merch_list if merch["type"] in options["merch_types"]
        ]
    return merch_list


def sort(merch_list, options):
    if options["sort_by"] == "Nothing":
        return [merch for merch in merch_list if "price" in merch] + [
            merch for merch in merch_list if "price" not in merch
        ]
    return sorted(
        [merch for merch in merch_list if options["sort_by"].lower() in merch],
        key=lambda merch: merch[options["sort_by"].lower()],
        reverse=options["sort_order"] == "Descending",
    ) + [merch for merch in merch_list if options["sort_by"].lower() not in merch]


def create_new_page(soup, merch_list):
    cols = soup.find(attrs={"class": "leftMiddleColumns"})
    ol = cols.find("ol")
    ol.clear()
    for merch in merch_list:
        ol.append(merch["li"])

    page_body = soup.new_tag(
        "div",
        attrs={
            "id": "pgBd",
            "class": "yui-skin-sam",
            "style": "overflow: hidden; width: fit-content; margin-top: 40px; min-height: auto; padding-bottom: 5px",
        },
    )
    page_body.insert(0, soup.find(attrs={"id": "custom-design-rules-style"}))
    page_body.insert(1, cols)

    new_soup = BeautifulSoup(str(soup.head) + "<body></body>", "html.parser")
    new_soup.body.insert(0, page_body)

    with NamedTemporaryFile(
        suffix=".html", mode="w", encoding="utf-8", delete=False
    ) as file:
        file.write(str(new_soup))
        file.close()
        webbrowser.get().open(file.name)


def execute(options):
    soup = load_page(options["label"])
    merch_list = scrape_merch(options["label"], soup)
    merch_list = apply_filters(merch_list, options)
    merch_list = sort(merch_list, options)
    create_new_page(soup, merch_list)
