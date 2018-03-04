<template>
  <div id="app">
    <h1>Advanced Cloud Computing Project</h1>
    <server-status />
  </div>
</template>

<script>
import ServerStatus from './ServerStatus.vue'

export default {
  components: {
    'server-status': ServerStatus
  }
}
</script>

<!--
<style>
  #app {
    background: black;
  }
</style>

<style lang="stylus">
  h1
    background: red
    color: white
</style>

<style lang="scss">
  #app {
    h1 {
      border-bottom: 5px solid gold;
    }
  }
</style>
-->