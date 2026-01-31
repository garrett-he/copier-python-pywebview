import { createRouter, createWebHashHistory, type RouteRecordRaw } from "vue-router";
import HomeView from "@/views/HomeView.vue";

const routes: RouteRecordRaw[] = [
    {
        path: "/",
        name: "home",
        component: HomeView,
    },
];

const router = createRouter({
    history: createWebHashHistory(),
    routes,
});

export default router;
