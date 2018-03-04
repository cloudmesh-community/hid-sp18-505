## Resources
Server:  
[GitHub Developer GraphQL API v4 Docs](https://developer.github.com/v4/)  
[GitHub GraphQL API Explorer](https://developer.github.com/v4/explorer/)  

Client:  
[Poi](https://github.com/egoist/poi)  
[Poi Example](https://github.com/egoist/poi)  
https://kofoedanders.com/vue-poi-suave/  

Developer Tools:  
https://github.com/apollographql/apollo-client-devtools  

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
# Example curl requests
curl -X POST -H "Content-Type: application/json" --data '{ "query": "{ status }" }' http://localhost:5000/graphql
curl -X POST -H "Content-Type: application/json" --data '{ "query": "{ allRaingages {edges{node{id code name }}}}"}' http://localhost:5000/graphql
# Example link requests
http://localhost:5000/graphql?
