"""
services.py
author: Averill Cate, Jr acatejr@gmail.com

Example query for a repos issues
query {
  repository(name: "book", owner: "cloudmesh") {
    issues(first: 100) {
      totalCount
      nodes {
        author {
          login
        }
        body
        assignees(first:100) {
          edges {
            node {
              id
              name
            }
          }
        }
      }
    }
  }
}
"""
import requests
import json
import os
import dotenv

dotenv_path = os.path.join(os.path.abspath('..'), '.env')
dotenv.load_dotenv(dotenv_path)

GITHUB_API_TOKEN = os.getenv('GITHUB_API_TOKEN')
GITHUB_HEADERS = {'Authorization': 'token %s' % GITHUB_API_TOKEN}

REPOSITORIES = [
    {"owner": "cloudmesh", "name": "book"},
    {"owner": "pallets", "name": "flask"},
]

GITHUB_API_URL="https://api.github.com/graphql"

def github_issue_count(repo):
    """Queries the githup graphql api for a repo issue count.
    """
    json_query = {'query': '{ repository(owner: "%s", name: "%s") { issues(first: 1) { totalCount } } }' % (repo['owner'], repo['name'])}
    r = requests.post(url=GITHUB_API_URL, json=json_query, headers=GITHUB_HEADERS)
    data = json.loads(r.text)
    repo['issue_count'] = data['data']['repository']['issues']['totalCount']
    return repo

if __name__ == '__main__':
    for r in REPOSITORIES:
        count = github_issue_count(r)
        print(r)
