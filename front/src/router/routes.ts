import { RouteRecordRaw } from 'vue-router';


const routes: RouteRecordRaw[] = [
    {
        name: 'Home',
        path: '/',
        component: () => import('../layout/UserLayout.vue'),
        children: [
            {
                name: 'About',
                path: '/about',
                component: () => import('../views/AboutView.vue'),
            },
            {
                name: 'Resources',
                path: '/resources',
                component: () => import('../views/ResourcesView.vue'),
            },
            {
                name: 'Team',
                path: '/team',
                component: () => import('../views/TeamView.vue'),
            },
            {
                name: 'News',
                path: '/news',
                component: () => import('../views/NewsView.vue'),
            },
            {
                name: 'Calendar',
                path: '/calendar',
                component: () => import('../views/CalendarView.vue'),
            },
        ]
    },
    {
        name: 'Admin-login',
        path: '/admin',
        component: () => import('../views/admin/LoginView.vue'),
    },
    {
        name: 'Admin-panel',
        path: '/admin/panel',
        component: () => import('../layout/AdminLayout.vue'),
        children: [
            {
                name: 'Posts',
                path: 'posts',
                component: () => import('../views/admin/PostView.vue'), 
            },
            {
                name: 'Members',
                path: 'members',
                component: () => import('../views/admin/MemberView.vue'), 
            },
            {
                name: 'Dates',
                path: 'dates',
                component: () => import('../views/admin/DateView.vue'), 
            }
        ]
    }
];

export default routes;
