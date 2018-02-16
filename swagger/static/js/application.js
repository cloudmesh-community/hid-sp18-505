Vue.component('map-component', {
    template: `<div>Map</div>`,
    data() {
        return {
            msg: "Map Message"
        }
    }
});

new Vue({
    delimiters: ['[[', ']]'],
    el: '#app',
    template: `
        <map-component />
    `,
    data() {
        return {
            title: "The title"
        }
    }    
});