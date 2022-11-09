import {createRouter, createWebHistory} from "vue-router/dist/vue-router";
import HomePage from "@/js/pages/HomePage";
import CatalogPage from "@/js/pages/CatalogPage";

const routes = [
    {
        path: '/',
        component: HomePage
    },
    {
        path: '/catalog/:id',
        component: CatalogPage
    }
]

const router = createRouter({
    routes,
    history: createWebHistory(process.env.BASE_URL)
})

export default router;