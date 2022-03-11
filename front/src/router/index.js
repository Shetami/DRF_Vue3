import { createRouter, createWebHistory } from 'vue-router'
import Home from "../views/Home";
import SignIn from "../views/SignIn";
import SignUp from "../views/SignUp";


const routes = [
    {
    path: '/',
    name: 'Home',
    component: Home
    },
    {
    path: '/sign-in',
    name: 'SignIn',
    component: SignIn
    },
    {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
    },
]
const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router