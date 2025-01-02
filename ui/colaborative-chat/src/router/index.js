import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import CreateView from "@/views/CreateView.vue";
import RoomView from "@/views/RoomView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/create",
      name: "Create",
      component: CreateView,
    },
    {
      path: "/room/:name",
      name: "Room",
      component: RoomView,
    },
  ],
});

export default router;
