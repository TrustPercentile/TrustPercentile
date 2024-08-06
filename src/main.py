import csv

from src.generate_detailed_markdown_file import get_detailed_markdown_file
from src.generate_trustPercentile_readme_file import get_trustPercentile_readme_file
from src.get_raw_metrics import get_raw_metrics
from src.scrape import scrape

owner = "chalk"
repo = "chalk"
token = ""

if __name__ == "__main__":

    os.makedirs("../data", exist_ok=True)
    os.makedirs("../output", exist_ok=True)
    os.makedirs("../images", exist_ok=True)
    os.makedirs("../docs", exist_ok=True)

    # 01
    # scrape date for later calculate
    scrape(owner, repo, token)

    # 02
    # calculate raw metrics and saved to '../output'
    # '../output/{owner}_{repo}_raw_metrics.csv' : metrics of target repo
    # '../output/merged_raw_metrics.csv' : metrics combined with other 999 repos
    get_raw_metrics(owner, repo)

    # 03
    # use metrics to generate details.md
    get_detailed_markdown_file(owner, repo)

    # 04
    # use metrics to generate README.md (TrustPercentile)
    get_trustPercentile_readme_file(owner, repo)


