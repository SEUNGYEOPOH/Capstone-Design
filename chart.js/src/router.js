import Vue from "vue";
import VueRouter from 'vue-router'
import Detect from './views/Detect';
import mapping from './views/mapping'


Vue.use(VueRouter);

/* eslint-disable */
const router = new VueRouter({
    mode: 'history',
    routes: [
        {path:"/Detect",
        component: Detect,
        meta: {
            title: "Detect",
        }},
        {path:'/',
        component:mapping,
        meta: {
            title: "Main",
        }}
    ]
});

router.afterEach((to, from) => {
    //nextTick은 Dom이 업데이트 된 후 실행됩니다.
    Vue.nextTick(() => {
        document.title = to.meta.title;
    });
});

const makeTitle = (title) =>
    title ? `CrowdGuard | ${title}` : "CrowdGuard";

router.afterEach((to, from) => {
    Vue.nextTick(() => {
    document.title = makeTitle(to.meta.title);
    });
});
export default router;