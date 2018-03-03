## Resources
Server:  
[GitHub Developer GraphQL API v4 Docs](https://developer.github.com/v4/)  
[GitHub GraphQL API Explorer](https://developer.github.com/v4/explorer/)
Client:  
[Poi](https://github.com/egoist/poi)

## Example GitHub GraphQL Queries

Retrieve the Cloudmesh organization's issues
```
query { 
  organization(login: "cloudmesh") {     
    members(first: 100) {
      edges {
        node {
          id
          name
          issues {
            totalCount
          }
        }
      }
    }
  }
}
```
Retrieve the Cloudmesh-Community organization's issues
```
query { 
  organization(login: "cloudmesh-community") {     
    members(first: 100) {
      edges {
        node {
          id
          name
          issues {
            totalCount
          }
        }
      }
    }
  }
}
```

Retrieve a repository's issues
```
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
```