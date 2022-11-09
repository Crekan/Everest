import { createApp } from 'vue'
import App from './js/App'
import router from "@/js/router/router";
import store from "./js/store";

createApp(App)
    .use(store)
    .use(router)
    .mount('#app')

// const app = new Vue({
//     el: '#app',
//     store,
//     router
// })