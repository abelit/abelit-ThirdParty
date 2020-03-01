import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";

Vue.use(Router);

export default new Router({
  // mode: "history",
  base: process.env.BASE_URL,
  routes: [{
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/about",
      name: "about",
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () =>
        import( /* webpackChunkName: "about" */ "./views/About.vue")
    },
    {
      path: "/eq/dce",
      name: "dce",
      component: () => import("@/views/question/EqDce.vue")
    },
    {
      path: "/eq/tto",
      name: "tto",
      component: () => import("@/views/EqTtoExam.vue")
    },
    {
      path: "/eq/nstptto",
      name: "nstptto",
      component: () => import("@/views/question/EqNonStpTto.vue")
    },
    {
      path: "/eq/ttofeedback",
      name: "ttofeedback",
      component: () => import("@/views/question/EqTtoFeedback.vue")
    },
    {
      path: "/eq/opened",
      name: "opened",
      component: () => import("@/views/question/EqOpened.vue")
    },
    {
      path: "/eq",
      name: "start",
      component: () => import("@/views/EqStartPage.vue")
    },
    {
      path: "/eq/user",
      name: "user",
      component: () => import("@/views/EqUserInfo.vue")
    },
    {
      path: "/eq/tip",
      name: "tip",
      component: () => import("@/views/EqTip.vue")
    },
    {
      path: "/eq/end",
      name: "end",
      component: () => import("@/views/EqEndPage.vue")
    },
    {
      path: "/eq/question/setting",
      name: "setting",
      component: () => import("@/views/QuestionSetting.vue")
    },
  ]
});