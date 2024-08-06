import pandas as pd

from src.image import generate_image
from src.normalize import normalize_metrics, prepare_normalized_metrics_for_readme
from src.ranking import rank_metrics, prepare_ranked_metrics_for_readme


def write_markdown_to_file(file_path, markdown_content):
    with open(file_path, mode='w') as file:
        file.write(markdown_content)


def generate_readme(owner, repo, input_file, readme_file):
    metrics = pd.read_csv(input_file)
    row = metrics[(metrics['owner'] == owner) & (metrics['repo'] == repo)].iloc[0]

    # <center><img src="../images/grade_f.svg" width="100px" height="100px"></center>
    #
    # This grade is based on the percentile rankings of the 3 trust component scores below, which are compared with the top 1000 most-downloaded npm libraries.

    markdown_content = f"""
# {repo}’s Trust Percentiles

Note: This is a forked repo. The original repo is [here](https://github.com/{owner}/{repo}).
*Data as of January 31, 2024*

<details>
<summary><span style="font-size: 20px;"><strong>Community Activity and Integrity -- </strong>Beats <strong><span style="color: blue;">{float(row['Community Activity and Integrity'])}%</span></strong> Other Repos</summary>
<div>
<div align=center>
  <img src="../images/{owner}_{repo}/Community Activity and Integrity.png" width="500px" height="170px">
</div>
Activity and usage by this project’s consumers and contributors. More people using and contributing to this project increases these metrics.<br><br>
</div>
<table>
  <tr>
    <td>
      <div>
        <strong>Usage Popularity:</strong> Beats <strong>{float(row['Usage Popularity'])}%</strong>
        <p>How much consumers use this project: stars, watches, forks, downstream dependents.</p>
      </div>
      <div>
        <strong>Code Contribution:</strong> Beats <strong>{float(row['Code Contribution'])}%</strong>
        <p>Activity which adds to the codebase: commits and PRs.</p>
      </div>
    </td>
    <td>
      <div>
        <strong>Contributor Participation:</strong> Beats <strong>{float(row['Contributor Participation'])}%</strong>
        <p>Activity in discussion and participation: number of contributors, comments made, quality of comments.</p>
      </div>
      <div>
        <strong>Contributor Growth:</strong> Beats <strong>{float(row['Contributor Growth'])}%</strong>
        <p>How the project is scaling in size: change in contributors, PRs.</p>
      </div>
    </td>
  </tr>
</table>
</details>


<details>
<summary><span style="font-size: 20px;"><strong>Maintenance and Goodwill -- </strong>Beats <strong><span style="color: blue;">{float(row['Maintenance and Goodwill'])}%</span></strong> Other Repos</summary>
<div>
<div align=center>
  <img src="../images/{owner}_{repo}/Maintenance and Goodwill.png" width="500px" height="170px">
</div>
Activity and involvement by this project’s maintainer(s) for the benefit of the project community. Maintainers could increase these metrics by extending documentation and being more responsive to community participation (especially issues and PRs).<br><br>
</div> 
<table>
  <tr>
    <td>
      <div>
        <strong>Issues Maintenance:</strong> Beats <strong>{float(row['Issues Maintenance'])}%</strong>
        <p>How efficiently issues are addressed: issues closed and comments on issues.</p>
      </div>
      <div>
        <strong>Community Documentation:</strong> Beats <strong>{float(row['Community Documentation'])}%</strong>
        <p>Support for the community to participate: issue and PR templates, code of conduct, governance, etc.</p>
      </div>
    </td>
    <td>
      <div>
        <strong>Code Maintenance:</strong> Beats <strong>{float(row['Code Maintenance'])}%</strong>
        <p>How efficiently code changes are addressed: commits and PRs closed, commit standards.</p>
      </div>
      <div>
        <strong>Maintainer History:</strong> Beats <strong>{float(row['Maintainer History'])}%</strong>
        <p>Maintainer experience: maintainers' other projects.</p>
      </div>
    </td>
  </tr>
</table>
</details>


<details>
<summary><span style="font-size: 20px;"><strong>Code Quality -- </strong>Beats <strong><span style="color: blue;">{float(row['Code Quality'])}%</span></strong> Other Repos</summary>
<div>
<div align=center>
  <img src="../images/{owner}_{repo}/Code Quality.png" width="500px" height="170px">
</div>
Security and scalability of the project’s code. Contributors can increase these metrics by maintaining the dependencies and setting up automated testing and procedural reviews.<br><br>
</div> 
<table>
  <tr>
    <td>
      <div>
        <strong>Dependencies Health:</strong> Beats <strong>{float(row['Dependencies Health'])}%</strong>
        <p>Mitigation of dependency vulnerability risk: dependency versions, reported vulnerabilities.</p>
      </div>
      <div>
        <strong>Review Coverage:</strong> Beats <strong>{float(row['Review Coverage'])}%</strong>
        <p>Scale of manual code reviews: contributors and reviewers per code portion, commit sizes.</p>
      </div>
    </td>
    <td>
      <div>
        <strong>Testing Quality:</strong> Beats <strong>{float(row['Testing Quality'])}%</strong>
        <p>Scale of automated tests: workflow runs, check runs, code authors.</p>
      </div>
      <div>
        <strong>Project Maturity:</strong> Beats <strong>{float(row['Project Maturity'])}%</strong>
        <p>Size and age of repo: lines of code, creation time, versions.</p>
      </div>
    </td>
  </tr>
</table>
</details>



***
        """
    write_markdown_to_file(readme_file, markdown_content)
    print(f"Readme.md has been successfully written to {readme_file}")



def get_trustPercentile_readme_file(owner, repo):
    normalize_metrics('../output/merged_raw_metrics.csv', '../output/normalized_metrics.csv')
    prepare_normalized_metrics_for_readme('../output/normalized_metrics.csv', '../output/readme_normalized_metrics.csv')
    generate_image(owner, repo, '../output/readme_normalized_metrics.csv', )
    rank_metrics('../output/normalized_metrics.csv', '../output/ranked_metrics.csv')
    prepare_ranked_metrics_for_readme('../output/ranked_metrics.csv', '../output/readme_ranked_metrics.csv')
    generate_readme(owner, repo,'../output/readme_ranked_metrics.csv', f'../docs/README_{repo}.md' )
