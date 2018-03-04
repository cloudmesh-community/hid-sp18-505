<template>
  <div>
      <div>
          <button @click="message = serverStatus()">GraphQL Server Status</button>
          <input type="text" readonly v-bind:value="message" placeholder="click for server status"/>
      </div>
  </div>
</template>

<script>

module.exports = {
    data: () => {
        return {
            message: ''
        }
    },   
    methods: {
        serverStatus: function(event) {
            let query = '{status}'            
            const self = this;            
            this.axios.post('http://127.0.0.1:5000/graphql', {query : query})
            .then((response) => {                
                self.message = response.data.data.status
            })
        }
    }
}
</script>

<style scoped></style>