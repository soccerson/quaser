const routes = [
  {
    path: "/",
    component: () => import("layouts/MainLayout.vue"),
    children: [
      { path: "", component: () => import("pages/IndexPage.vue") },
      { path: "contact", component: () => import("pages/ContactUs.vue") },
      { path: "login", component: () => import("pages/LoginPage.vue") },
      { path: "register", component: () => import("pages/RegisterPage.vue") },
      {
        path: "create-recruitment",
        component: () => import("pages/CreateRecruitment.vue"),
      },
      { path: "confirm", component: () => import("pages/FormConfirmPage.vue") },
      { path: "ListPage", component: () => import("pages/ListPage.vue") },
      {
        path:"create_match",
        component: () => import("pages/matchcreate.vue"),
      },
      {
        path: "create-practice-menu",
        component: () => import("pages/CreatePracticeMenu.vue"),
      }
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: "/:catchAll(.*)*",
    component: () => import("pages/ErrorNotFound.vue"),
  },
];

export default routes;
