import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import App from './App.vue'
import './main.styl'
import './main.sass'

Vue.use(VueAxios, axios)

new Vue({
  el: '#app',
  render: h => h(App)
})