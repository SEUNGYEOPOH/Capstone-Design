import Vue from "vue";
import VueRouter from 'vue-router'
import Detect from './views/Detect';
import map from "./views/map";
import mapping from './views/mapping'

Vue.use(VueRouter);

/* eslint-disable */
const router = new VueRouter({
    mode: 'history',
    routes: [
        {path:"/Detect",
        component: Detect},
        {path:"/",
        component: map},
        {path:'/mapping',
        component:mapping}
    ]
});
export default router;